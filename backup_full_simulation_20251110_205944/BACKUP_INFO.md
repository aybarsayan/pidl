# 💾 PIDL Platform Full Backup

**Yedekleme Tarihi:** 2025-11-10 20:59:44
**Durum:** Tam Simülasyon Hazır ✅

---

## 📊 İçerik Özeti

### Database (2.0 MB)
- ✅ **150 Katılımcı** (demografik verilerle)
- ✅ **900 Task Session** (Similar/Complementary counterbalanced)
- ✅ **900 Gerçek Solidity Kodu** (persona-specific)
- ✅ **1,800 Pre/Post Test** (learning gain ölçümü)
- ✅ **900 NASA-TLX** (bilişsel yük)
- ✅ **900 AI Evaluation** (user satisfaction)
- ✅ **900 Technical Metrics** (yazılımcı bakışı)
- ✅ **900 Pedagogical Metrics** (eğitimci bakışı)
- ✅ **900 Task Comparison** (mode karşılaştırma)
- ✅ **150 Final Evaluation** (genel değerlendirme)

**Toplam:** ~10,000+ veri noktası

---

## 🎯 Doğrulanan Hipotezler

| Hipotez | Sonuç | p-value | Effect Size | Durum |
|---------|-------|---------|-------------|-------|
| **H1: Similar > Satisfaction** | 8.70 > 7.83 | <0.001 | d=0.81 | ✅ |
| **H2: Complementary > Learning** | 5.30 > 2.72 | <0.001 | d=0.59 | ✅ |
| **H3: Expert - No Difference** | 7.51 ≈ 7.41 | 0.650 | - | ✅ |
| **H4: Novice - Comp Better** | 8.91 > 7.90 | <0.001 | d=1.47 | ✅ |
| **H5: Negative Correlation** | r = -0.114 | 0.028 | - | ✅ |
| **H6: Dual-Perspective Valid** | Uyumlu | - | α≈0.87 | ✅ |

---

## 📁 Klasör Yapısı

```
backup_full_simulation_20251110_205944/
├── BACKUP_INFO.md                          # Bu dosya
│
├── database/                               # Database (2.0 MB)
│   ├── research_data.db                    # 150 katılımcı × 6 task × formlar
│   ├── models.py                           # 10 tablo tanımı
│   └── database.py                         # SQLAlchemy connection
│
├── pages/                                  # Streamlit sayfalar
│   ├── 1_📊_Yonetim_Paneli.py             # Admin dashboard
│   └── 2_👤_Katilimci_Detay.py            # Katılımcı detay görünümü
│
├── research_modules/                       # Araştırma modülleri
│   ├── persona_selector.py                # 10 persona seçici
│   ├── data_logger.py                     # Database logger
│   ├── code_evaluator.py                  # Otomatik kod değerlendirme
│   ├── technical_evaluation.py            # Teknik metrik formu
│   └── pedagogical_evaluation.py          # Pedagojik metrik formu
│
├── synthetic_data_N150/                    # Sentetik veri (CSV/JSON)
│   ├── README.md                           # Veri seti dokümantasyonu
│   ├── synthetic_data_full.json            # Tüm veri (2.4 MB)
│   ├── participants.csv                    # 150 katılımcı
│   ├── task_sessions.csv                   # 900 session
│   ├── generated_codes.csv                 # 900 Solidity kodu
│   ├── nasa_tlx_responses.csv             # 900 NASA-TLX
│   ├── ai_code_evaluations.csv            # 900 AI eval
│   ├── technical_metrics.csv              # 900 technical
│   ├── pedagogical_metrics.csv            # 900 pedagogical
│   ├── task_comparisons.csv               # 900 comparison
│   └── final_evaluations.csv              # 150 final eval
│
├── src/                                    # Kaynak kod
│   ├── personas.py                        # 10 persona tanımı
│   ├── code_generator.py                  # Kod üretimi
│   ├── evaluator.py                       # Değerlendirme
│   └── content_analyzer.py                # 6-aşamalı analiz
│
├── tasks/                                  # 6 blockchain görevi
│   ├── task1_token_transfer.py
│   ├── task2_voting_system.py
│   ├── task3_escrow.py
│   ├── task4_nft_minting.py
│   ├── task5_staking.py
│   └── task6_auction.py
│
├── formlar/                                # Araştırma formları
│   ├── girisli_onay_formu.py
│   ├── demografik_bilgi.py
│   ├── yetkinlik_testi.py
│   └── ...
│
├── app.py                                 # Ana Streamlit app
├── research_app.py                        # Araştırma app
├── recreate_database.py                   # Database recreator
├── generate_synthetic_data.py             # Veri generator
├── generate_realistic_solidity_codes.py   # Kod generator
├── import_synthetic_data.py               # Import script
└── validate_synthetic_data.py             # Validation script
```

---

## 🚀 Restore (Geri Yükleme) Adımları

### 1. Database'i Geri Yükle
```bash
cp backup_full_simulation_20251110_205944/database/research_data.db database/
```

### 2. Streamlit Uygulamalarını Başlat
```bash
# Ana app (port 8501)
streamlit run app.py --server.port 8501

# Research app (port 8503)
streamlit run research_app.py --server.port 8503
```

### 3. Yönetim Panelini Aç
```
http://localhost:8501
```
Sol menüden:
- 📊 Yönetim Paneli
- 👤 Katılımcı Detay

---

## ✨ Özellikler

### Yönetim Paneli (1_📊_Yonetim_Paneli.py)
- ✅ Genel istatistikler (4 metrik kartı)
- ✅ Demografik analiz (yaş, cinsiyet, eğitim, dreyfus)
- ✅ Görev performans analizi
- ✅ Öğrenme kazanımı (Pre/Post test)
- ✅ Bilişsel yük analizi (NASA-TLX)
- ✅ AI değerlendirme
- ✅ 6-aşamalı içerik analizi
- ✅ Persona performans karşılaştırması
- ✅ CSV/Excel export

### Katılımcı Detay (2_👤_Katilimci_Detay.py)
- ✅ 150 katılımcı tek tek inceleme
- ✅ Sidebar filtreler (cinsiyet, dreyfus)
- ✅ Özet istatistikler
- ✅ 6 görev detayı (expander)
- ✅ Her görev için 6 TAB:
  - 📝 Prompt & Kod (Solidity kodu indirme)
  - 📊 Pre/Post Test (learning gain)
  - 🧠 NASA-TLX (radar chart)
  - ⭐ AI Değerlendirme (5 metrik)
  - 🔧 Technical Metrics (manuel + otomatik)
  - 📚 Pedagogical Metrics (7 pedagojik metrik)
- ✅ Final evaluation

---

## 🎭 10 Persona Sistemi

**Pedagogical (5 adet):**
1. Dr. Ayşe - Beginner Friendly (Novice)
2. Prof. Mehmet - Academic (Advanced Beginner)
3. Öğretmen Zeynep - Practical (Competent)
4. Ali - Facilitator (Proficient)
5. Mentor Fatma - Supportive (Expert)

**Technical (5 adet):**
6. Ahmet - Smart Contract Beginner (Novice)
7. Elif - Security Aware (Advanced Beginner)
8. Can - Gas Optimizer (Competent)
9. Deniz - DApp Architect (Proficient)
10. Burak - Blockchain Specialist (Expert)

---

## 📊 Demografik Dağılım

**Yaş:** 28.3 ± 4.0 (22-38)
**Cinsiyet:** Erkek 69%, Kadın 31%
**Eğitim:** Lisans 46%, Y.Lisans 34%, Doktora 20%

**Dreyfus Seviyesi:**
- Novice: 18%
- Advanced Beginner: 36%
- Competent: 21%
- Proficient: 17%
- Expert: 9%

---

## ⚠️ Önemli Notlar

1. **ETİK UYARI:** Bu veri sentetiktir, SADECE platform testi içindir!
2. **Database Boyut:** 2.0 MB (900 kod + formlar)
3. **CSV Toplam:** ~500 KB (10 dosya)
4. **JSON Toplam:** 2.4 MB (full dump)

---

## 🔬 Araştırma Tasarımı

- **N = 150 katılımcı**
- **6 task × 150 = 900 session**
- **Counterbalanced design:** Her katılımcı 3 Similar + 3 Complementary
- **10 Persona:** Random assignment based on competency
- **Dual-perspective metrics:** Technical + Pedagogical
- **Otomatik değerlendirme:** Security, Gas, Complexity

---

## 📞 Restore Sorunları

Eğer restore sırasında sorun yaşarsanız:

1. **Database kilidi:** `rm database/research_data.db` → yeniden kopyala
2. **Import hatası:** `python recreate_database.py` → `python import_synthetic_data.py`
3. **Streamlit cache:** Cache'i temizle (sağ üst menü)

---

**Yedekleme Tamamlandı!** ✅
**Tarih:** 2025-11-10 20:59:44
**Toplam Boyut:** ~5 MB
**Veri Noktası:** 10,000+
