# 🤖 Sekolah Chatbot TFIDF

## Deskripsi Proyek
Chatbot cerdas untuk sistem informasi pendaftaran sekolah menggunakan teknologi TF-IDF dan machine learning. Mendukung antarmuka web dan Telegram untuk memudahkan calon siswa mendapatkan informasi pendaftaran.

### 🌟 Fitur Utama
- Jawaban otomatis seputar pendaftaran sekolah
- Dukungan platform ganda (Web & Telegram)
- Pencarian respons cerdas menggunakan TF-IDF
- Sistem yang dapat diperluas dan disesuaikan

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file `LICENSE` untuk detail lengkap.

### 🔗 Informasi Repository
- **Nama**: sekolah-chatbot-tfidf
- **Versi**: 1.0.0
- **Status**: Aktif Pengembangan

### 👥 Kontributor
- [Nama Anda] - Pengembang Utama

### 🐛 Laporkan Masalah
Silakan buka issue di repositori GitHub untuk melaporkan bug atau saran perbaikan.

## Deskripsi Proyek
Proyek ini mengembangkan chatbot cerdas untuk sistem informasi pendaftaran siswa menggunakan teknologi TF-IDF (Term Frequency-Inverse Document Frequency) dengan dukungan antarmuka web dan Telegram.

## Fitur Utama
- Chatbot berbasis AI untuk menjawab pertanyaan seputar pendaftaran
- Dukungan platform ganda: Web dan Telegram
- Algoritma pencarian cerdas menggunakan TF-IDF
- Pra-pemrosesan teks canggih

## Teknologi yang Digunakan
- Python
- Flask
- Scikit-learn
- Telegram Bot API
- TF-IDF Vectorization

## Statistik Dataset
### Distribusi Intent
| Intent | Jumlah Pertanyaan | Persentase |
|--------|-------------------|------------|
| Sapaan | 9 | 15.25% |
| Proses Pendaftaran | 7 | 11.86% |
| Jadwal Pendaftaran | 5 | 8.47% |
| Informasi Kontak | 7 | 11.86% |
| Lokasi | 5 | 8.47% |
| Biaya Pendaftaran | 5 | 8.47% |
| Batas Akhir Pendaftaran | 7 | 11.86% |
| Persyaratan | 7 | 11.86% |
| Status Pendaftaran | 7 | 11.86% |

## Teknik Pra-pemrosesan
- Normalisasi kata dengan 36 aturan pemetaan
- Penghapusan 28 kata henti
- Normalisasi huruf besar/kecil
- Penghapusan karakter khusus
- Pencocokan fuzzy untuk toleransi kesalahan ketik

## Kinerja Sistem
### Data Training
- **Akurasi**: 100%
- **Rata-rata Kepercayaan**: 100%
- **Jumlah Sampel**: 59 pertanyaan

### Data Uji
- **Akurasi**: 80%
- **Rata-rata Kepercayaan**: 73.13%
- **Jumlah Sampel**: 20 pertanyaan

### Kinerja Keseluruhan
- **Akurasi Total**: 94.94%
- **Skor Kepercayaan Rata-rata**: 93.20%
- **Total Sampel**: 79

## Evaluasi Sistem Mendalam

### 📊 Metrik Evaluasi Chatbot

### Ringkasan Performa

| Data Type | Accuracy | Precision | Recall | F1-Score | Avg Confidence | Samples |
|-----------|----------|-----------|--------|----------|----------------|---------|
| Training  | 100.00%  | 100.00%   | 100.00%| 100.00%  | 100.00%        | 59      |
| Test      | 80.00%   | 95.83%    | 80.00% | 85.23%   | 73.13%         | 20      |
| Overall   | 94.94%   | 97.72%    | 94.94% | 95.99%   | 93.20%         | 79      |

### Analisis Detail Metrik

| Metrik     | Definisi                                                                         | Hasil    | Interpretasi                                                              |
|------------|----------------------------------------------------------------------------------|----------|---------------------------------------------------------------------------|
| Akurasi    | Seberapa tepat chatbot merespons pertanyaan dengan jawaban yang relevan dan benar | 94.94%   | Sistem mampu menjawab 94.94% pertanyaan dengan benar                       |
| Presisi    | Seberapa tepat chatbot memberikan jawaban yang relevan dari semua jawaban        | 97.72%   | 97.72% dari jawaban yang diberikan adalah relevan                         |
| Recall     | Seberapa lengkap chatbot memberikan jawaban dari semua jawaban yang diperlukan   | 94.94%   | 94.94% dari jawaban yang seharusnya diberikan telah diberikan              |
| F1-Score   | Rata-rata harmonik dari presisi dan recall                                       | 95.99%   | Menunjukkan keseimbangan yang sangat baik antara presisi dan recall        |

### 🔍 Interpretasi Mendalam

#### Performa Data Training
- **Akurasi Sempurna**: 100% menunjukkan pengenalan pola yang luar biasa dalam dataset training
- **Kepercayaan Maksimal**: Sistem memiliki keyakinan penuh pada jawaban di dataset training

#### Generalisasi pada Data Uji
- **Penurunan Akurasi yang Wajar**: Penurunan dari 100% ke 80% menandakan kemampuan generalisasi yang sehat
- **Presisi Tetap Tinggi**: 95.83% presisi pada data uji menunjukkan keandalan sistem

#### Keseimbangan Keseluruhan
- **F1-Score Tinggi**: 95.99% mengindikasikan keseimbangan optimal antara presisi dan recall
- **Konsistensi Tinggi**: Rata-rata kepercayaan 93.20% menunjukkan stabilitas sistem

### 🚀 Implikasi Praktis
1. Sistem sangat andal dalam menjawab pertanyaan seputar pendaftaran
2. Mampu menangani variasi pertanyaan dengan akurasi tinggi
3. Berpotensi mengurangi beban manual dalam layanan informasi

### 🔬 Rekomendasi Lanjutan
1. Perluas dataset untuk meningkatkan kemampuan generalisasi
2. Lakukan validasi berkelanjutan dengan kasus penggunaan baru
3. Pertimbangkan teknik machine learning lanjutan untuk peningkatan performa

## Cara Penggunaan
1. Pastikan Python dan dependencies terinstal
2. Jalankan bot Telegram atau server web
3. Ajukan pertanyaan seputar pendaftaran

## Konfigurasi
- Sesuaikan `qa_data.json` untuk menambah/mengubah data pertanyaan
- Atur `normalization_rules.json` untuk pemetaan kata dan stop words
- Konfigurasikan token Telegram di environment variable

## Rencana Pengembangan
1. Perluas dataset training
2. Implementasi teknik pra-pemrosesan lebih canggih
3. Tambahkan pemahaman kontekstual
4. Optimalkan ambang batas kesamaan

## 🗂 Arsitektur Sistem

### 📊 Flowchart Sistem
![Flowchart Sistem Chatbot](/img/flowchart.png)

### 🏗 Diagram Kelas
![Diagram Kelas Chatbot](/img/class.png)

### 📝 Penjelasan Arsitektur

#### Flowchart Sistem
Flowchart menggambarkan alur kerja sistem chatbot dari input pengguna hingga menghasilkan respons:
1. Penerimaan input teks
2. Pra-pemrosesan teks
3. Pencarian respons terdekat
4. Pemberian respons kepada pengguna

#### Diagram Kelas
Diagram kelas menunjukkan struktur modular sistem:
- **ChatbotApplication**: Kelas utama yang mengintegrasikan seluruh komponen
- **TextPreprocessor**: Bertanggung jawab membersihkan dan mempersiapkan teks
- **ResponseMatcher**: Mengimplementasikan logika pencocokan pertanyaan
- **WebInterface**: Menyediakan rute Flask untuk antarmuka web
- **TelegramBotHandler**: Mengelola interaksi dengan bot Telegram
- **DataManager**: Menangani pembacaan, penyimpanan, dan pembaruan data

## Laporkan Masalah
Silakan buka issue di repositori proyek ini.

## 🛠 Instalasi dan Pengaturan

### Prasyarat
- Python 3.8+
- pip (Python Package Manager)
- Virtual Environment (disarankan)

### Langkah Instalasi

1. Clone Repositori
```bash
git clone https://github.com/anda/chatbot-pendaftaran.git
cd chatbot-pendaftaran
```

2. Buat Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate  # Untuk Linux/Mac
# myenv\Scripts\activate  # Untuk Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

### Konfigurasi Awal

1. Siapkan File Konfigurasi
- Salin `config.example.json` menjadi `config.json`
- Atur token Telegram Anda di `config.json`

2. Persiapkan Dataset
- Edit `qa_data.json` untuk menambahkan/mengubah pertanyaan dan jawaban
- Sesuaikan `normalization_rules.json` untuk aturan normalisasi teks

### Menjalankan Aplikasi

#### Mode Web
```bash
python app.py web
```

#### Mode Telegram Bot
```bash
python app.py telegram
```

### 📦 Requirements

Berikut adalah dependencies utama proyek:

| Paket | Versi | Fungsi |
|-------|-------|--------|
| Flask | 2.1.0+ | Kerangka Web |
| python-telegram-bot | 13.7+ | Integrasi Telegram |
| scikit-learn | 1.0.2+ | Pemrosesan TF-IDF |
| numpy | 1.22.0+ | Komputasi Numerik |
| requests | 2.27.0+ | HTTP Requests |

### 📄 File requirements.txt
```
Flask==2.1.0
python-telegram-bot==13.7
scikit-learn==1.0.2
numpy==1.22.0
requests==2.27.0
```

### 🔧 Troubleshooting
- Pastikan semua dependencies terinstal dengan benar
- Periksa koneksi internet untuk integrasi Telegram
- Verifikasi token bot Telegram
- Gunakan `pip install -r requirements.txt --upgrade` jika ada masalah dependensi

### 🚀 Deployment
- Untuk deployment production, pertimbangkan:
  1. Gunakan server WSGI seperti Gunicorn
  2. Atur variabel environment untuk konfigurasi sensitif
  3. Konfigurasikan firewall dan port
  4. Gunakan reverse proxy (Nginx/Apache)

### 🔒 Keamanan
- JANGAN commit token bot ke repositori publik
- Gunakan variabel environment untuk menyimpan token
- Terapkan pembatasan akses dan autentikasi