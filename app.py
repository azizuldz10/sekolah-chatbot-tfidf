from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import re
import numpy as np
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Telegram Bot Token
TELEGRAM_TOKEN = ""
# Load data
with open('qa_data.json', 'r', encoding='utf-8') as f:
    qa_data = json.load(f)

with open('normalization_rules.json', 'r', encoding='utf-8') as f:
    normalization_rules = json.load(f)

# Inisialisasi TF-IDF
vectorizer = TfidfVectorizer()
questions = qa_data['questions']
tfidf_matrix = vectorizer.fit_transform(questions)

def preprocess_text(text):
    """Preprocess text dengan rules"""
    try:
        with open('normalization_rules.json', 'r', encoding='utf-8') as f:
            rules = json.load(f)
    except FileNotFoundError:
        return text.lower()
    
    # Lowercase
    text = text.lower()
    
    # Apply word mapping
    words = text.split()
    mapped_words = []
    for word in words:
        if word in rules["word_mapping"]:
            mapped_words.append(rules["word_mapping"][word])
        else:
            mapped_words.append(word)
    
    # Remove stop words
    words = [w for w in mapped_words if w not in rules["stop_words"]]
    
    # Join back
    text = ' '.join(words)
    
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Tambah fuzzy matching untuk toleransi typo
    processed = text.lower()
    
    return processed

def get_best_response(user_message, threshold=0.3):
    try:
        # Preprocess
        processed_message = preprocess_text(user_message)
        processed_questions = [preprocess_text(q) for q in qa_data['questions']]
        
        # Vectorize
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.9
        )
        
        # Handle empty/invalid input
        if not processed_message.strip():
            return {
                'response': 'Maaf, pertanyaan tidak dapat diproses.',
                'confidence': 0,
                'matched_intent': 'unknown',
                'matched_question': None
            }
            
        # Process
        try:
            tfidf_matrix = vectorizer.fit_transform([processed_message] + processed_questions)
            similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            
            # Validasi hasil similarity
            if len(similarities) == 0:
                return {
                    'response': 'Maaf, tidak dapat menemukan kecocokan.',
                    'confidence': 0,
                    'matched_intent': 'unknown',
                    'matched_question': None
                }
            
            max_similarity = np.max(similarities)
            best_match_idx = np.argmax(similarities)
            
            if max_similarity > threshold:
                matched_intent = qa_data['intents'][best_match_idx]
                response = qa_data['responses'][matched_intent]
                return {
                    'response': response[0] if isinstance(response, list) else response,
                    'confidence': float(max_similarity),
                    'matched_intent': matched_intent,
                    'matched_question': qa_data['questions'][best_match_idx]
                }
            
            return {
                'response': 'Maaf, saya tidak menemukan jawaban yang sesuai.',
                'confidence': float(max_similarity),
                'matched_intent': 'unknown',
                'matched_question': None
            }
                
        except Exception as e:
            logger.error(f"Error in similarity calculation: {str(e)}")
            return {
                'response': 'Terjadi kesalahan dalam perhitungan similarity.',
                'confidence': 0,
                'matched_intent': 'error',
                'matched_question': None
            }
            
    except Exception as e:
        logger.error(f"Error in get_best_response: {str(e)}")
        return {
            'response': 'Terjadi kesalahan dalam memproses pertanyaan.',
            'confidence': 0,
            'matched_intent': 'error',
            'matched_question': None
        }

# Telegram Bot Handlers
def start(update, context):
    welcome_message = """
Selamat datang di Bot Pendaftaran Sekolah! 👋

Saya siap membantu Anda dengan informasi seputar:
- Biaya pendaftaran 💰
- Lokasi sekolah 📍
- Jadwal pendaftaran 📅
- Persyaratan 📝
- Cara mendaftar ✍️
- Status pendaftaran 📋
- Kontak informasi ☎️

Silakan ajukan pertanyaan Anda.
    """
    update.message.reply_text(welcome_message)

def help(update, context):
    help_message = """
Panduan penggunaan bot:

1. Tanyakan langsung informasi yang Anda butuhkan
2. Contoh pertanyaan:
   - "Berapa biaya pendaftaran?"
   - "Dimana lokasi sekolah?"
   - "Kapan pendaftaran dibuka?"
   - "Apa saja syarat pendaftaran?"

Butuh bantuan lebih lanjut? Hubungi admin kami.
    """
    update.message.reply_text(help_message)

def handle_message(update, context):
    try:
        user_message = update.message.text
        result = get_best_response(user_message)
        
        confidence = result['confidence'] * 100
        response_text = result['response']
        matched_intent = result['matched_intent']
        
        formatted_response = f"""{response_text}

-------------------
💡 Confidence: {confidence:.2f}%
🎯 Intent: {matched_intent}"""
        
        update.message.reply_text(formatted_response)
        
    except Exception as e:
        logger.error(f"Error handling message: {str(e)}")
        update.message.reply_text(
            "Maaf, terjadi kesalahan dalam memproses pesan Anda. Silakan coba lagi."
        )

# Flask routes untuk web UI
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat-test')
def chat_test():
    return render_template('chat.html')

@app.route('/qa-database')
def qa_database():
    return render_template('qa_database.html')

@app.route('/add_qa')
def add_qa():
    return render_template('add_qa.html')

@app.route('/list_qa')
def list_qa():
    return render_template('list_qa.html')

@app.route('/get_qa_data')
def get_qa_data():
    return jsonify(qa_data)

@app.route('/add_bulk_qa', methods=['POST'])
def add_bulk_qa():
    try:
        data = request.get_json()
        intent = data.get('intent')
        questions = data.get('questions', [])
        response = data.get('response')

        # Tambah ke qa_data
        qa_data['questions'].extend(questions)
        qa_data['intents'].extend([intent] * len(questions))
        
        if intent not in qa_data['responses']:
            qa_data['responses'][intent] = [response]

        # Simpan ke file
        with open('qa_data.json', 'w', encoding='utf-8') as f:
            json.dump(qa_data, f, indent=2, ensure_ascii=False)

        # Re-train model
        global vectorizer, tfidf_matrix
        vectorizer = TfidfVectorizer()
        questions = qa_data['questions']
        tfidf_matrix = vectorizer.fit_transform(questions)

        return jsonify({
            'status': 'success',
            'count': len(questions)
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/update_rules', methods=['POST'])
def update_rules():
    try:
        # Logic untuk update rules
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

# Flask routes
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        result = get_best_response(user_message)
        
        confidence = result['confidence'] * 100
        response_text = result['response']
        matched_intent = result['matched_intent']
        
        formatted_response = f"""{response_text}

-------------------
Confidence: {confidence:.2f}%
Intent: {matched_intent}"""
        
        return jsonify({
            'response': formatted_response,
            'confidence': result['confidence'],
            'intent': matched_intent
        })
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            'response': 'Maaf, terjadi kesalahan dalam memproses pesan Anda.',
            'confidence': 0,
            'intent': 'error'
        })

def setup_telegram_bot():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    return updater

# Buat file terpisah untuk bot Telegram
def run_telegram_bot():
    updater = setup_telegram_bot()
    updater.start_polling()
    print("Telegram Bot is running...")

if __name__ == '__main__':
    # Jalankan bot Telegram
    run_telegram_bot()
    
    # Jalankan Flask app
    app.run(debug=False, port=5000)
