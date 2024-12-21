from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from app import get_best_response
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Ganti dengan token bot Anda
TOKEN = os.getenv('')

def start(update, context):
    """Handler untuk command /start"""
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
    """Handler untuk command /help"""
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
    """Handler untuk pesan user"""
    try:
        user_message = update.message.text
        
        # Dapatkan response dari chatbot
        result = get_best_response(user_message)
        
        # Format response dengan confidence score
        confidence = result['confidence'] * 100
        response_text = result['response']
        matched_intent = result['matched_intent']
        
        # Format pesan response
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

def main():
    """Fungsi utama bot"""
    # Buat updater
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Tambah handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Jalankan bot
    print("Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 
