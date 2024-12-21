import json
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

class ChatbotEvaluator:
    def __init__(self):
        # Load data
        self.qa_data = self.load_json('qa_data.json')
        self.rules = self.load_json('normalization_rules.json')
        
        # Initialize test cases
        self.test_cases = self.prepare_test_cases()
    
    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def prepare_test_cases(self):
        return {
            'ask_biaya': [
                "berapa biaya pendaftarannya?",
                "biaya masuk berapa?",
                "berapa biaya daftar?",
                "biaya pendaftaran berapa?",
                "berapa total biayanya?"
            ],
            'lokasi': [
                "dimana lokasi pendaftaran?",
                "dimana tempat daftarnya?",
                "lokasi pendaftaran dimana?",
                "alamat pendaftaran dimana?",
                "dimana tempat mendaftar?"
            ],
            'jadwal_pendaftaran': [
                "kapan pendaftaran dibuka?",
                "kapan mulai pendaftaran?", 
                "tanggal berapa pendaftaran?",
                "jadwal pendaftaran kapan?",
                "kapan bisa mendaftar?"
            ],
            'penutupan_pendaftaran': [
                "kapan pendaftaran ditutup?",
                "sampai tanggal berapa pendaftaran?",
                "batas akhir pendaftaran kapan?",
                "deadline pendaftaran kapan?",
                "penutupan pendaftaran kapan?"
            ]
        }

    def evaluate_accuracy(self, chatbot):
        results = {
            'true_intent': [],
            'predicted_intent': [],
            'confidence': [],
            'is_correct': [],
            'question_type': []
        }

        # Evaluasi data training
        print("\nEvaluating Training Data:")
        for q, true_intent in zip(self.qa_data['questions'], self.qa_data['intents']):
            response = chatbot.get_response(q)
            predicted_intent = response.get('intent', 'unknown')
            confidence = response.get('confidence', 0)
            
            results['true_intent'].append(true_intent)
            results['predicted_intent'].append(predicted_intent)
            results['confidence'].append(confidence)
            results['is_correct'].append(true_intent == predicted_intent)
            results['question_type'].append('training')

        # Evaluasi test cases formal
        print("\nEvaluating Test Cases:")
        for intent, questions in self.test_cases.items():
            for q in questions:
                response = chatbot.get_response(q)
                predicted_intent = response.get('intent', 'unknown')
                confidence = response.get('confidence', 0)
                
                results['true_intent'].append(intent)
                results['predicted_intent'].append(predicted_intent)
                results['confidence'].append(confidence)
                results['is_correct'].append(intent == predicted_intent)
                results['question_type'].append('test')

        return results

    def print_detailed_results(self, results):
        print("\nDetailed Evaluation Results:")
        print("-" * 80)
        
        # Create DataFrame for metrics calculation
        df = pd.DataFrame(results)
        
        metrics_table = []
        
        # Calculate metrics per question type
        for q_type in ['training', 'test']:
            type_df = df[df['question_type'] == q_type]
            
            if not type_df.empty:
                # Calculate metrics
                accuracy = accuracy_score(type_df['true_intent'], type_df['predicted_intent'])
                report = classification_report(type_df['true_intent'], 
                                            type_df['predicted_intent'],
                                            output_dict=True)
                
                # Calculate weighted averages
                weighted_precision = report['weighted avg']['precision']
                weighted_recall = report['weighted avg']['recall']
                weighted_f1 = report['weighted avg']['f1-score']
                avg_conf = type_df['confidence'].mean()
                
                metrics_table.append({
                    'Data Type': q_type.title(),
                    'Accuracy': f"{accuracy:.2%}",
                    'Precision': f"{weighted_precision:.2%}",
                    'Recall': f"{weighted_recall:.2%}",
                    'F1-Score': f"{weighted_f1:.2%}",
                    'Avg Confidence': f"{avg_conf:.2%}",
                    'Samples': len(type_df)
                })
        
        # Calculate overall metrics
        accuracy = accuracy_score(df['true_intent'], df['predicted_intent'])
        report = classification_report(df['true_intent'], 
                                     df['predicted_intent'],
                                     output_dict=True)
        
        weighted_precision = report['weighted avg']['precision']
        weighted_recall = report['weighted avg']['recall']
        weighted_f1 = report['weighted avg']['f1-score']
        avg_conf = df['confidence'].mean()
        
        metrics_table.append({
            'Data Type': 'Overall',
            'Accuracy': f"{accuracy:.2%}",
            'Precision': f"{weighted_precision:.2%}",
            'Recall': f"{weighted_recall:.2%}",
            'F1-Score': f"{weighted_f1:.2%}",
            'Avg Confidence': f"{avg_conf:.2%}",
            'Samples': len(df)
        })
        
        # Print metrics table
        print("\nMetrik Evaluasi Chatbot:")
        print("-" * 80)
        metrics_df = pd.DataFrame(metrics_table)
        print(metrics_df.to_string(index=False))
        
        # Print detailed analysis table
        print("\nAnalisis Detail Metrik:")
        print("-" * 80)
        analysis_table = [
            ["Akurasi", "Seberapa tepat chatbot merespons pertanyaan dengan jawaban yang relevan dan benar.",
             metrics_table[-1]['Accuracy'], 
             f"Sistem mampu menjawab {metrics_table[-1]['Accuracy']} pertanyaan dengan benar."],
            ["Presisi", "Seberapa tepat chatbot memberikan jawaban yang relevan dari semua jawaban yang diberikan.",
             metrics_table[-1]['Precision'],
             f"{metrics_table[-1]['Precision']} dari jawaban yang diberikan adalah relevan."],
            ["Recall", "Seberapa lengkap chatbot memberikan jawaban yang relevan dari semua jawaban yang seharusnya diberikan.",
             metrics_table[-1]['Recall'],
             f"{metrics_table[-1]['Recall']} dari jawaban yang seharusnya diberikan telah diberikan."],
            ["F1-Score", "Rata-rata harmonik dari presisi dan recall, memberikan ukuran gabungan yang lebih baik.",
             metrics_table[-1]['F1-Score'],
             f"F1-Score menunjukkan keseimbangan yang {metrics_table[-1]['F1-Score']} antara presisi dan recall."]
        ]
        
        analysis_df = pd.DataFrame(analysis_table, 
                                 columns=['Metrik', 'Deskripsi', 'Hasil Pengukuran', 'Analisis'])
        print(analysis_df.to_string(index=False))

    def print_statistics(self):
        print("\nData Statistics:")
        print("-" * 20)
        
        # Count per intent
        intent_counts = {}
        for intent in self.qa_data['intents']:
            if intent not in intent_counts:
                intent_counts[intent] = 0
            intent_counts[intent] += 1
        
        print(f"Total Intents: {len(set(self.qa_data['intents']))}")
        print(f"Total Questions: {len(self.qa_data['questions'])}")
        print("\nPer Intent Distribution:")
        for intent, count in sorted(intent_counts.items()):
            print(f"{intent:20s}: {count:3d} questions")
        
        # Word mapping statistics
        print("\nNormalization Rules:")
        print(f"Word Mappings: {len(self.rules['word_mapping'])} rules")
        print(f"Stop Words: {len(self.rules['stop_words'])} words")