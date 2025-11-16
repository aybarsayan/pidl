# Sentetik Araştırma Verisi - N=150

⚠️ **ÖNEMLİ UYARI:** Bu veri seti tamamen sentetik olup SADECE test amaçlıdır!

## 📊 Veri Seti Özellikleri

- **Katılımcı Sayısı:** 150
- **Task Session Sayısı:** 900 (6 task × 150 katılımcı)
- **Toplam Veri Noktası:** ~10,000+
- **Üretim Tarihi:** 2025-11-10
- **Metodoloji:** doktora_tezi_full.html bulgularına dayalı tersine mühendislik

## 🎯 Doğrulanan Hipotezler

### ✅ H1: Similar Mode - Daha Yüksek User Satisfaction
- **Sonuç:** Similar (8.70) > Complementary (7.83)
- **p-value:** < 0.001
- **Cohen's d:** 0.81 (Beklenen: 0.89)
- **Durum:** ✅ Doğrulandı

### ✅ H2: Complementary Mode - Daha Yüksek Learning Outcomes
- **Sonuç:** Complementary (5.30) > Similar (2.72) learning gain
- **p-value:** < 0.001
- **Cohen's d:** 0.59 (Beklenen: 0.76)
- **Durum:** ✅ Doğrulandı

### ✅ H3: Expert Seviyede Mode Farkı Yok
- **Sonuç:** Expert-Similar (7.51) ≈ Expert-Complementary (7.41)
- **p-value:** 0.65 (> 0.05)
- **Durum:** ✅ Doğrulandı (fark yok)

### ✅ H4: Novice Seviyede Complementary Daha Etkili
- **Sonuç:** Novice-Complementary (8.91) > Novice-Similar (7.90)
- **p-value:** < 0.001
- **Cohen's d:** 1.47 (Beklenen: 1.24)
- **Durum:** ✅ Doğrulandı

### ✅ H5: Teknik-Pedagojik Negatif Korelasyon
- **Sonuç:** r = -0.114
- **Beklenen:** r ≈ -0.18
- **Durum:** ✅ Doğrulandı (negatif korelasyon mevcut)

### ✅ H6: Dual-Perspective Metrics Validity
- **Technical Metrics:** Security 6.68±1.73, Gas 6.25±1.86, Quality 6.97±1.54
- **Pedagogical Metrics:** Learning 6.58±1.70, Instructiveness 6.79±1.79, CogLoad 3.79±1.65
- **Durum:** ✅ Metrikler HTML bulgularıyla uyumlu

## 📁 Dosya Yapısı

```
synthetic_data_N150/
├── README.md                          # Bu dosya
├── synthetic_data_full.json           # Tüm veri (JSON format)
│
├── participants.csv                   # 150 katılımcı demografik verileri
├── task_sessions.csv                  # 900 task session kaydı
├── pre_post_tests.csv                 # 1800 test (900 pre + 900 post)
├── generated_codes.csv                # 900 üretilen kod
├── nasa_tlx_responses.csv             # 900 NASA-TLX bilişsel yük ölçümü
├── ai_code_evaluations.csv            # 900 AI değerlendirmesi
├── technical_metrics.csv              # 900 teknik metrik (yazılımcı bakışı)
├── pedagogical_metrics.csv            # 900 pedagojik metrik (eğitimci bakışı)
├── task_comparisons.csv               # 900 görev karşılaştırması
└── final_evaluations.csv              # 150 final değerlendirme anketi
```

## 📈 Demografik Dağılım

### Yaş
- **Ortalama:** 28.3 yaş
- **Std Dev:** 4.0
- **Aralık:** 22-38

### Cinsiyet
- **Erkek:** 104 (%69.3)
- **Kadın:** 46 (%30.7)

### Eğitim Seviyesi
- **Lisans:** 69 (%46.0)
- **Yüksek Lisans:** 51 (%34.0)
- **Doktora:** 30 (%20.0)

### Dreyfus Yetkinlik Seviyesi
- **Novice:** 27 (%18.0)
- **Advanced Beginner:** 54 (%36.0)
- **Competent:** 31 (%20.7)
- **Proficient:** 25 (%16.7)
- **Expert:** 13 (%8.7)

### Çalışma Alanı
- **Yazılım Geliştirme:** ~45%
- **Eğitim:** ~28%
- **Akademik Araştırma:** ~27%

## 🎭 Persona Performance Rankings

1. **Can - Gas Optimizer** (Technical, Competent): 9.20/10
2. **Ahmet - Smart Contract Beginner** (Technical, Novice): 9.00/10
3. **Deniz - DApp Architect** (Technical, Proficient): 8.52/10
4. **Prof. Mehmet - Academic** (Pedagogical, Advanced Beginner): 8.51/10
5. **Dr. Ayşe - Beginner Friendly** (Pedagogical, Novice): 8.46/10
6. **Elif - Security Aware** (Technical, Advanced Beginner): 8.44/10
7. **Mentor Fatma - Supportive** (Pedagogical, Expert): 8.40/10
8. **Burak - Blockchain Specialist** (Technical, Expert): 8.14/10
9. **Öğretmen Zeynep - Practical** (Pedagogical, Competent): 7.82/10
10. **Ali - Facilitator** (Pedagogical, Proficient): 7.74/10

## 🔬 Araştırma Tasarımı

### Counterbalanced Design
- Her katılımcı 6 task tamamladı
- 3 task Similar mode ile
- 3 task Complementary mode ile
- Sıralama randomize edildi

### Değerlendirme Formları
1. **Pre-test** (5 soru, her task öncesi)
2. **Post-test** (5 soru, her task sonrası)
3. **NASA-TLX** (6 dimension bilişsel yük)
4. **AI Code Evaluation** (5 metrik + yorumlar)
5. **Technical Metrics** (5 manuel + 3 otomatik metrik)
6. **Pedagogical Metrics** (7 pedagojik metrik + Bloom taxonomy)
7. **Task Comparison** (zorluk + karşılaştırma)
8. **Final Evaluation** (15 soru genel değerlendirme)

## ⚠️ ETİK UYARI

**Bu veri setinin kullanım kısıtlamaları:**

### ✅ İZİN VERİLEN KULLANIM
- Platform özelliklerini test etme
- Veri analiz pipeline'ını geliştirme
- Yönetim paneli görselleştirmelerini deneme
- İstatistiksel analiz metodlarını doğrulama
- Database performansını test etme
- Algoritma ve formül testleri
- Proof-of-concept gösterimi

### ❌ YASAK KULLANIM
- Bilimsel makalede gerçek veri olarak sunma
- Doktora/yüksek lisans tezinde gerçek araştırma verisi olarak kullanma
- Konferans bildirilerinde gerçek bulgular olarak paylaşma
- Akademik yükselme dosyalarında kullanma
- Herhangi bir resmi bilimsel yayında kullanma

**NEDEN YASAK?**
- Data fabrication (veri uydurma) akademik suiistimaldir
- Ciddi etik ihlaldir
- Akademik kariyeri sonlandırabilir
- Üniversite ve kurumlar tarafından cezalandırılır

## 📊 Veri Kalite Kontrolleri

### İstatistiksel Tutarlılık
- ✅ Demografik dağılımlar HTML ile uyumlu
- ✅ Tüm 6 hipotez doğrulandı
- ✅ Effect size'lar beklenen aralıkta
- ✅ p-değerleri tutarlı
- ✅ Dual-perspective metrics validate edildi

### Veri Bütünlüğü
- ✅ Her session için tüm formlar dolu
- ✅ 150 katılımcı × 6 task = 900 session
- ✅ Hiç eksik veri yok (complete dataset)
- ✅ Pre-test < Post-test learning gain pozitif
- ✅ Dreyfus seviye dağılımı tutarlı

## 🔧 Kullanım Örnekleri

### Python ile Veri Okuma

```python
import pandas as pd
import json

# CSV okuma
participants = pd.read_csv('synthetic_data_N150/participants.csv')
sessions = pd.read_csv('synthetic_data_N150/task_sessions.csv')
technical = pd.read_csv('synthetic_data_N150/technical_metrics.csv')

# JSON okuma (tüm veri)
with open('synthetic_data_N150/synthetic_data_full.json', 'r') as f:
    all_data = json.load(f)

# Analiz
print(f"Toplam katılımcı: {len(participants)}")
print(f"Ortalama yaş: {participants['age'].mean():.1f}")
print(f"Dreyfus dağılımı:\n{participants['competency_level'].value_counts()}")
```

### Database'e Import

```python
from database.database import DatabaseSession
from database.models import Participant, TaskSession
import pandas as pd

# Participants import
participants_df = pd.read_csv('synthetic_data_N150/participants.csv')

with DatabaseSession() as session:
    for _, row in participants_df.iterrows():
        participant = Participant(
            uuid=row['uuid'],
            age=row['age'],
            gender=row['gender'],
            # ... diğer alanlar
        )
        session.add(participant)
    session.commit()
```

### Hipotez Testi

```python
from scipy import stats
import numpy as np

# H1: Similar vs Complementary satisfaction
similar_sessions = sessions[sessions['assigned_ai_type'] == 'Similar']
comp_sessions = sessions[sessions['assigned_ai_type'] == 'Complementary']

similar_scores = similar_sessions.merge(ai_eval, on='session_id')['code_understandability']
comp_scores = comp_sessions.merge(ai_eval, on='session_id')['code_understandability']

t_stat, p_value = stats.ttest_ind(similar_scores, comp_scores)
cohen_d = (similar_scores.mean() - comp_scores.mean()) / np.sqrt((similar_scores.std()**2 + comp_scores.std()**2) / 2)

print(f"H1: Similar > Complementary")
print(f"  Similar: {similar_scores.mean():.2f}")
print(f"  Complementary: {comp_scores.mean():.2f}")
print(f"  p-value: {p_value:.4f}")
print(f"  Cohen's d: {cohen_d:.2f}")
```

## 🛠️ Bakım ve Güncelleme

### Yeniden Üretme

```bash
# Veriyi yeniden üret (farklı random seed ile)
python generate_synthetic_data.py

# Doğrula
python validate_synthetic_data.py
```

### Özelleştirme

`generate_synthetic_data.py` dosyasında:
- `TOTAL_PARTICIPANTS`: Katılımcı sayısını değiştir
- `DREYFUS_DIST`: Dreyfus dağılımını ayarla
- `PERSONA_PERFORMANCE`: Persona skorlarını güncelle

## 📞 Destek

Sorular için:
- **Script:** `generate_synthetic_data.py` ve `validate_synthetic_data.py` dosyalarına bakın
- **Doküman:** `documentation/` klasöründe ek bilgi bulunabilir

## 📜 Lisans

Bu sentetik veri seti **eğitim ve test amaçlı** üretilmiştir.
Gerçek bilimsel araştırmalarda kullanılması kesinlikle yasaktır.

---

**Son Güncelleme:** 2025-11-10
**Versiyon:** 1.0
**Durum:** Validated ✅
