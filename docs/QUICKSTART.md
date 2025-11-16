# 🚀 Hızlı Başlangıç Rehberi

## 1. Kurulum

### Otomatik Kurulum (Önerilen)
```bash
chmod +x setup.sh
./setup.sh
```

### Manuel Kurulum
```bash
# Virtual environment oluştur
python3 -m venv venv

# Aktifleştir
source venv/bin/activate  # macOS/Linux
# veya
venv\Scripts\activate  # Windows

# Gereksinimleri yükle
pip install -r requirements.txt
```

## 2. API Anahtarını Ayarla

`.env` dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:

```env
OPENAI_API_KEY=sk-your-api-key-here
DEFAULT_MODEL=gpt-4-turbo-preview
TEMPERATURE=0.7
MAX_TOKENS=2000
```

## 3. Uygulamayı Çalıştır

```bash
# Virtual environment aktif olduğundan emin olun
source venv/bin/activate

# Streamlit uygulamasını başlat
streamlit run app.py
```

Uygulama otomatik olarak tarayıcınızda açılacak: `http://localhost:8501`

## 4. Kullanım

### Adım 1: Görev Tanımla
- "Kod Üret" sekmesinde bir programlama görevi/problemi tanımlayın
- Örnek: "Fibonacci sayılarını hesaplayan bir fonksiyon yaz"

### Adım 2: Persona'ları Seç
- Sidebar'dan hangi persona kategorisini kullanmak istediğinizi seçin:
  - **Tümü**: 10 persona (5 eğitim + 5 teknoloji)
  - **Eğitim Bilimcileri**: Pedagojik yaklaşımlar
  - **Teknoloji Uzmanları**: Teknik mükemmellik

### Adım 3: Kod Üret
- "🚀 Kodları Üret" butonuna tıklayın
- Sistem tüm seçili persona'lardan paralel olarak kod üretecek

### Adım 4: Sonuçları İncele
- **Sonuçlar** sekmesinde üretilen kodları görün
- Her persona'nın ürettiği kodu ve metriklerini inceleyin
- Kodları indirebilirsiniz

### Adım 5: Karşılaştır
- **Sıralamalar** sekmesinde performans karşılaştırmalarını görün
- Grafikler ve tablolarla detaylı analiz

## 5. Persona'lar

### 🎓 Eğitim Bilimcileri
1. **Dr. Ayşe Öğretmen**: Pedagojik, açıklayıcı kod
2. **Prof. Mehmet Didaktik**: Adım adım öğretici
3. **Dr. Zeynep Konstruktivist**: Problem çözme odaklı
4. **Doç. Ali Kolaboratif**: Modüler ve takım dostu
5. **Dr. Fatma Adaptif**: Esnek ve uyarlanabilir

### 💻 Teknoloji Uzmanları
1. **Ahmet Senior Developer**: Clean code ve best practices
2. **Can DevOps Engineer**: Performans ve ölçeklenebilirlik
3. **Elif Security Expert**: Güvenlik odaklı
4. **Deniz Full-Stack Architect**: Mimari tasarım
5. **Burak AI Specialist**: Algoritma optimizasyonu

## 6. Değerlendirme Metrikleri

Kodlar şu kriterlere göre değerlendirilir:

- **Güvenlik (30%)**: Bandit ile zafiyet analizi
- **Kalite (30%)**: Pylint ile kod kalitesi
- **Karmaşıklık (20%)**: Radon ile cyclomatic complexity
- **Maintainability (20%)**: Sürdürülebilirlik indeksi

## 7. İpuçları

✅ **Başarılı Kullanım İçin**:
- Net ve açık görev tanımları yazın
- Farklı persona kategorilerini deneyin
- Üretilen kodları kendi projelerinize uyarlayın
- Metrik sonuçlarını karşılaştırarak en iyi yaklaşımı seçin

⚠️ **Dikkat Edilmesi Gerekenler**:
- API çağrıları ücrete tabidir (OpenAI fiyatlandırması)
- 10 persona ile çalışırken ~20,000 token kullanımı olabilir
- İnternet bağlantısı gereklidir

## 8. Sorun Giderme

### "API Key bulunamadı" hatası
- `.env` dosyasını kontrol edin
- `OPENAI_API_KEY` değişkeninin doğru olduğundan emin olun

### Paket yükleme hataları
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Streamlit çalışmıyor
```bash
# Streamlit'i yeniden yükle
pip uninstall streamlit
pip install streamlit
```

## 9. Örnek Görevler

İşte deneyebileceğiniz bazı görevler:

1. **Kolay**: 
   - "İki sayının toplamını hesaplayan fonksiyon"
   - "Palindrom kontrolü yapan kod"

2. **Orta**:
   - "Binary search algoritması"
   - "JSON dosyasını okuyup filtreleyen script"

3. **Zor**:
   - "REST API ile veri çekme ve işleme"
   - "Veri analizi ve görselleştirme pipeline'ı"

## 10. Destek

- 📖 [README.md](README.md) - Detaylı dokümantasyon
- 🐛 Sorunlar için GitHub Issues
- 💬 Geri bildirimlerinizi bekleriz!

---

**Keyifli Kodlamalar! 🎭**

