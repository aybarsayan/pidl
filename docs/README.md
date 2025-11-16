# Persona in the Loop (PIDL)

## 📖 Proje Hakkında

Persona in the Loop (PIDL), **Dreyfus Model of Skill Acquisition** bazlı 10 yapay zeka persona'sının aynı problem için kod üretip karşılaştırılmasını sağlayan bir akademik araştırma platformudur.

### Özellikler

- 🎓 **5 Eğitim Domain Persona**: Novice → Expert (Dreyfus 5 aşama)
- 💻 **5 Teknoloji Domain Persona**: Novice → Expert (Dreyfus 5 aşama)
- 📊 **Dreyfus Yetkinlik Modeli**: Rule-based → Intuitive mastery
- ⚡ **Paralel Kod Üretimi**: 10 persona eş zamanlı çalışır
- 📊 **Kapsamlı Performans Analizi**: 
  - Güvenlik analizi (Bandit)
  - Kod kalitesi (Pylint, Radon)
  - Performans metrikleri
  - Karmaşıklık analizi
- 🎨 **Modern Streamlit Arayüzü**: Kullanıcı dostu ve görsel zengin

## 🚀 Kurulum

1. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

2. `.env` dosyası oluşturun ve API anahtarlarınızı ekleyin:
```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

3. Uygulamayı çalıştırın:
```bash
streamlit run app.py
```

## 📋 Kullanım

1. Kod yazılmasını istediğiniz problemi/görevi girin
2. "Kodları Üret" butonuna tıklayın
3. 10 persona'nın ürettiği kodları inceleyin
4. Detaylı performans karşılaştırmalarını görüntüleyin
5. En iyi sonucu seçin veya kodları indirin

## 🏗️ Proje Yapısı

```
pidl/
├── app.py                 # Ana Streamlit uygulaması
├── personas.py            # Persona tanımları
├── code_generator.py      # Kod üretim motoru
├── evaluator.py          # Performans değerlendirici
├── requirements.txt       # Bağımlılıklar
└── README.md             # Dokümantasyon
```

## 🎭 Persona'lar - Dreyfus Model (5 Seviye × 2 Domain)

### 📚 Dreyfus Model of Skill Acquisition

Personalar, Dreyfus Brothers'ın yetkinlik kazanım modelinin 5 aşamasına göre tasarlanmıştır:

1. **Novice (Acemi)**: Rule-based, context-free, rigid
2. **Advanced Beginner (İlerleyen)**: Pattern recognition, guideline-based
3. **Competent (Yetkin)**: Prioritization, deliberate planning
4. **Proficient (İleri)**: Holistic understanding, intuitive
5. **Expert (Uzman)**: Transcends rules, innovative

### 🎓 Eğitim Domain Personas

**1. 🔰 Ayşe Yeni Başlayan (Novice)**
   - **Deneyim**: 3-6 ay (ChatGPT ile öğreniyor)
   - **Felsefe**: "Tutorial'ları takip ediyorum. Çalışan kod iyi koddur"
   - **Kod Stili**: Çok basit, bol yorumlu, tek fonksiyon, kopyala-yapıştır
   - **Güçlü Yön**: Yeni başlayanlar için anlaşılır, basit örnekler
   - **Zayıf Yön**: Best practices bilmiyor, güvenlik açıkları, teknik derinlik yok

**2. 📚 Mehmet İlerleyen (Advanced Beginner)**
   - **Deneyim**: 1-2 yıl (Pattern'leri tanımaya başladı)
   - **Felsefe**: "Pattern'ler var, onları kullanıyorum"
   - **Kod Stili**: Pattern-based, örnek adapte eden, modüler düşünmeye başlayan
   - **Güçlü Yön**: Pattern tanıma, örnekleri adapte etme, best practices farkındalığı
   - **Zayıf Yön**: Hala guideline'lara bağımlı, karmaşık problemlerde zorlanır

**3. 🎯 Zeynep Yetkin (Competent)**
   - **Deneyim**: 3-5 yıl (Planlı ve hedef odaklı)
   - **Felsefe**: "Her proje hedef odaklı planlanmalı. Complexity'yi yönetmeyi öğrendim"
   - **Kod Stili**: Hedef odaklı, deliberate (bilinçli), test-driven
   - **Güçlü Yön**: Karmaşık projeleri planlama, önceliklendirme, troubleshooting
   - **Zayıf Yön**: Henüz intuitive değil, yenilikçi çözümler sınırlı

**4. 🎓 Ali Usta (Proficient)**
   - **Deneyim**: 6-10 yıl (Holistic ve intuitive)
   - **Felsefe**: "İyi eğitim teknolojisi görünmezdir. Öğrenci öğrenir, teknolojiyi fark etmez"
   - **Kod Stili**: Holistic, maxim-guided, sophisticated, learner-centered
   - **Güçlü Yön**: Bütünsel bakış, intuitive problem solving, derin pedagojik entegrasyon
   - **Zayıf Yön**: Açıklaması zor (intuitive), junior'lara öğretmekte zorlanabilir

**5. 🚀 Fatma Uzman (Expert)**
   - **Deneyim**: 10+ yıl (Paradigm-shifting, research-based)
   - **Felsefe**: "Geleceği tahmin etmenin en iyi yolu, onu yaratmaktır"
   - **Kod Stili**: Innovative, research-based, paradigm-shifting, cutting-edge
   - **Güçlü Yön**: Kuralları aşar, yeni modeller yaratır, intuitive mastery
   - **Zayıf Yön**: Çok ileri olabilir, experimental, standartları göz ardı edebilir

### 💻 Teknoloji Domain Personas

**6. 🔰 Can Acemi (Novice)**
   - **Deneyim**: 1-3 ay Solidity (Dokümantasyondan kopyalıyor)
   - **Felsefe**: "Kodu çalıştırmaya çalışıyorum. Tutorial ne diyorsa onu yapıyorum"
   - **Kod Stili**: Syntax-odaklı, rule-based, kopyala-yapıştır, çok basit
   - **Güçlü Yön**: Basitlik, syntax kurallara uyma
   - **Zayıf Yön**: Güvenlik bilmiyor, gas optimization yok, best practices yok

**7. 📚 Deniz Gelişen (Advanced Beginner)**
   - **Deneyim**: 6-12 ay (OpenZeppelin patterns kullanıyor)
   - **Felsefe**: "OpenZeppelin'in neden böyle yaptığını anlıyorum"
   - **Kod Stili**: Pattern-based, OpenZeppelin-kullanan, modifier ekliyor
   - **Güçlü Yön**: OpenZeppelin kullanımı, temel design patterns, modifier/event
   - **Zayıf Yön**: Hala örneklere bağımlı, gas optimization sınırlı

**8. 🎯 Elif Yetkin (Competent)**
   - **Deneyim**: 2-4 yıl (Production-ready, gas optimized)
   - **Felsefe**: "Security ve gas optimization planlanmalı. Production'da sürpriz olmaz"
   - **Kod Stili**: Production-ready, gas-optimized, secure, deliberate
   - **Güçlü Yön**: Gas optimization, security best practices, upgradable contracts
   - **Zayıf Yön**: Bazen over-optimization, yenilikçi pattern'lerde sınırlı

**9. 🏗️ Burak İleri (Proficient)**
   - **Deneyim**: 5-8 yıl (Holistic DApp architecture)
   - **Felsefe**: "İyi DApp, on-chain/off-chain dengesini bulur. Holistic bakış gereklidir"
   - **Kod Stili**: Holistic, intuitive, enterprise-grade, maxim-guided
   - **Güçlü Yön**: Holistic system design, intuitive security, advanced optimization
   - **Zayıf Yön**: Açıklaması zor, junior'lara öğretmekte zorlanır

**10. 🚀 Ahmet Uzman (Expert)**
   - **Deneyim**: 10+ yıl (Protocol-level innovation, EVM mastery)
   - **Felsefe**: "EVM'nin sınırlarını zorlamak, yeni tasarım alanları açar. Geleceği yaratalım"
   - **Kod Stili**: Innovative, protocol-level, paradigm-shifting, EVM-mastery
   - **Güçlü Yön**: EVM-level mastery, protocol innovation, cryptographic expertise
   - **Zayıf Yön**: Çok ileri, experimental, standartları göz ardı edebilir

## 📊 Değerlendirme Metrikleri

- **Güvenlik Skoru**: Bandit ile zafiyet tespiti
- **Kod Kalitesi**: Pylint analizi
- **Karmaşıklık**: Cyclomatic complexity (Radon)
- **Maintainability Index**: Bakım kolaylığı skoru
- **Satır Sayısı**: Kod yoğunluğu

## 🤝 Katkıda Bulunma

Bu proje açık kaynaklıdır. Geliştirmeler için pull request gönderebilirsiniz.

## 📝 Lisans

MIT License

