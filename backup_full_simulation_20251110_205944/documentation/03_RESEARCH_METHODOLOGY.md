# BÖLÜM 3: ARAŞTIRMA YÖNTEMİ

## 3.1 ARAŞTIRMA MODELİ

### 3.1.1 Genel Tasarım

Bu araştırma, **karma yöntem (mixed-methods)** yaklaşımını benimser:

**Nicel Boyut:**
- Deneysel tasarım (5×2×2×3 faktöriyel)
- İstatistiksel testler (ANOVA, regression, correlation)
- Matematiksel model validasyonu

**Nitel Boyut:**
- Yarı-yapılandırılmış görüşmeler (N=30)
- Kod analizi (content analysis)
- Kullanıcı deneyimi raporları

**Entegrasyon:** Convergent parallel design (Creswell, 2014)

### 3.1.2 Faktöriyel Deneysel Tasarım

\[
\text{Design: } 5 \times 2 \times 2 \times 3
\]

**Factor 1: Yetkinlik Seviyesi** (Between-subjects)
- Novice (0-20)
- Advanced Beginner (21-40)
- Competent (41-60)
- Proficient (61-80)
- Expert (81-100)

**Factor 2: Domain Type** (Between-subjects)
- Technical (Blockchain development)
- Educational (Pedagogy & instructional design)

**Factor 3: Recommendation Mode** (Within-subjects)
- Similarity-based
- Complementary-based

**Factor 4: Task Complexity** (Within-subjects)
- Low (diploma verification)
- Medium (multi-signature fund)
- High (DAO governance)

**Toplam Koşul:** 5 × 2 × 2 × 3 = 60 deneysel koşul

---

## 3.2 ÇALIŞMA GRUBU

### 3.2.1 Örneklem Büyüklüğü

**Güç Analizi (G*Power 3.1):**
- Effect size: f = 0.25 (medium)
- α = 0.05
- Power (1-β) = 0.80
- Groups: 10
- **Required N = 150**

**Örneklem Dağılımı:**

| Seviye | Technical | Educational | Toplam |
|--------|-----------|-------------|--------|
| Novice | 15 | 15 | 30 |
| Adv. Beginner | 15 | 15 | 30 |
| Competent | 15 | 15 | 30 |
| Proficient | 15 | 15 | 30 |
| Expert | 15 | 15 | 30 |
| **TOPLAM** | **75** | **75** | **150** |

### 3.2.2 Seçim Kriterleri

**Dahil Etme:**
- 18-65 yaş arası
- İlgili alanda belirtilen deneyim süresi
- Türkçe ve İngilizce okuma yeterliliği
- Gönüllü katılım
- Temel bilgisayar okuryazarlığı

**Hariç Tutma:**
- LLM geliştirme deneyimi
- Araştırma konusuyla çıkar çatışması
- Önceki PIDL platform kullanımı
- Cognitive impairment

**Örnekleme Yöntemi:** Stratified random sampling

---

## 3.3 VERİ TOPLAMA ARAÇLARI

### 3.3.1 Yetkinlik Değerlendirme Enstrümanı

**A. Technical Competency Test (TCT)**
- 5 soru (blockchain/Solidity bilgisi)
- Likert-type (5 seçenek)
- Skor: 0-300 puan (normalize → 0-100)
- Cronbach's α = 0.87 (pilot)

**B. Educational Competency Test (ECT)**
- 5 soru (pedagoji/öğretim tasarımı)
- Likert-type (5 seçenek)
- Skor: 0-300 puan (normalize → 0-100)
- Cronbach's α = 0.89 (pilot)

**C. Bonus Questions**
- AI/LLM experience (binary)
- Prompt engineering knowledge (binary)
- Learning vs Production goal (binary)

### 3.3.2 Performans Ölçüm Araçları

**Kod Kalitesi Metrikleri (Otomatik):**
- Pylint score (0-100)
- Bandit security score (0-100)
- Radon complexity (0-100)
- Type hint ratio (%)
- LOC (lines of code)

**Pedagogical Metrikleri (Hesaplanmış):**
- Learning Ease (0-100)
- Cognitive Load Score (0-100) - Sweller Theory
- Instructiveness Index (0-100)
- Example Quality (0-100)

**Gas Efficiency (Blockchain-specific):**
- Estimated gas consumption
- Storage optimization score
- Function call efficiency

### 3.3.3 Kullanıcı Deneyimi Araçları

**A. NASA-TLX (Cognitive Load)**
- Mental Demand
- Physical Demand
- Temporal Demand
- Performance
- Effort
- Frustration

**B. User Satisfaction Questionnaire**
- 10 item, 5-point Likert
- Persona appropriateness
- Code quality perception
- Learning satisfaction

**C. Semi-Structured Interview Protocol**
- N=30 katılımcı (stratified selection)
- 30-45 dakika
- Themes: experience, learning, challenges, suggestions

---

## 3.4 DENEYSEL PLATFORM: PIDL

### 3.4.1 Sistem Mimarisi

```
PIDL Platform Architecture:

┌─────────────────────────────────────────┐
│         Frontend (Streamlit)            │
│  - 8 Ana Sekme                          │
│  - Dual-domain Assessment               │
│  - Dual-mode Recommendations            │
│  - Multi-LLM Support                    │
└──────────────┬──────────────────────────┘
               |
┌──────────────┴──────────────────────────┐
│         Backend (Python)                │
│  - competency_assessment.py             │
│  - recommendation_engine.py             │
│  - code_generator.py                    │
│  - evaluator.py                         │
│  - advanced_math_models.py              │
│  - multi_llm_engine.py                  │
└──────────────┬──────────────────────────┘
               |
┌──────────────┴──────────────────────────┐
│         Data Layer                      │
│  - user_profiles.json                   │
│  - code_outputs/                        │
│  - performance_logs/                    │
└─────────────────────────────────────────┘
```

### 3.4.2 Teknik Özellikler

**Programlama Dili:** Python 3.13  
**Framework:** Streamlit 1.31.0  
**LLM APIs:** OpenAI (GPT-4o), Anthropic (Claude), Google (Gemini), X.AI (Grok)  
**Analiz Kütüphaneleri:** NumPy, Pandas, Plotly  
**Kod Analizi:** Pylint, Bandit, Radon  

**Toplam Kod:** ~2500+ satır  
**Modüller:** 10 ana dosya  
**Test Coverage:** >80%

### 3.4.3 Veri Güvenliği

- Anonim UUID kullanımı
- KVKK/GDPR uyumlu
- Encrypted storage
- Opt-out seçeneği

---

## 3.5 VERİ TOPLAMA SÜRECİ

### Faz 1: Baseline (Hafta 1-2)
1. Katılımcı recruitment
2. Informed consent
3. Demographic survey
4. Dual-domain competency assessment

### Faz 2: Main Experiment (Hafta 3-5)
Her katılımcı:
- 6 görev (2 low + 2 medium + 2 high complexity)
- Her görev için 2 mod test (similarity + complementary)
- Toplam: 12 kod üretimi per katılımcı
- Süre: ~3-4 saat (2 oturumda)

### Faz 3: Post-Test (Hafta 6)
- User satisfaction survey
- NASA-TLX cognitive load
- Performance self-assessment
- Semi-structured interviews (subset)

**Toplam Veri:**
- 150 katılımcı × 12 task = 1,800 kod
- 10 persona × 1,800 = 18,000 kod (comparison)
- ~150 GB veri

---

## 3.6 VERİ ANALİZİ PLANI

### 3.6.1 Tanımlayıcı İstatistikler

- Mean, SD, Min, Max, Median
- Normallik testleri (Shapiro-Wilk)
- Outlier detection (IQR method)

### 3.6.2 Hipotez Testleri

**ANOVA (Multi-way):**

\[
Y_{ijkl} = \mu + \alpha_i + \beta_j + \gamma_k + (\alpha\beta)_{ij} + (\alpha\gamma)_{ik} + (\beta\gamma)_{jk} + \epsilon_{ijkl}
\]

- \( \alpha_i \): Yetkinlik etkisi
- \( \beta_j \): Domain etkisi
- \( \gamma_k \): Mode etkisi
- Interactions

**Post-hoc:** Tukey HSD (α=0.05)

**Effect Size:** 
- Partial η²
- Cohen's d
- Omega-squared

**Regression:**

\[
Performance = \beta_0 + \beta_1(Expertise) + \beta_2(Mode) + \beta_3(Expertise \times Mode) + \epsilon
\]

**Model Fit:**
- R²
- Adjusted R²
- RMSE
- AIC/BIC

---

## 3.7 GEÇERLİK VE GÜVENİRLİK

### 3.7.1 İç Geçerlik Tehditleri

**Tehdit:** Maturation (katılımcılar öğrenebilir)  
**Kontrol:** Counterbalancing, short duration

**Tehdit:** Testing effect (tekrar test)  
**Kontrol:** Farklı görevler her testte

**Tehdit:** Selection bias  
**Kontrol:** Random assignment, stratification

### 3.7.2 Dış Geçerlik

**Ecological Validity:** Gerçek blockchain education tasks  
**Population Validity:** Representative sample (N=150)  
**Temporal Validity:** 6 aylık follow-up (subset)

### 3.7.3 Güvenirlik

**Test-Retest:** r > 0.80 (2 hafta interval, N=20)  
**Inter-Rater:** κ > 0.75 (code quality assessment)  
**Internal Consistency:** Cronbach's α > 0.85

---

**Sayfa Sayısı:** 30-35 sayfa  
**Şekil/Tablo:** 8-10 adet  
**Kaynak:** 40-50 referans

