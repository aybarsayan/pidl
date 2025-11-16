# UYGULAMA REHBERİ
## PIDL Platformunun Araştırmada Kullanımı

---

## 1. SİSTEM KURULUMU

### 1.1 Gereksinimler

**Donanım:**
- CPU: 4+ core
- RAM: 8+ GB
- Disk: 10+ GB

**Yazılım:**
- Python 3.10+
- pip package manager
- Git (version control)

### 1.2 Kurulum Adımları

```bash
# 1. Repository clone
git clone https://github.com/[your-repo]/pidl.git
cd pidl

# 2. Virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# 3. Dependencies
pip install -r requirements.txt

# 4. Environment variables
cp .env.example .env
# .env dosyasını düzenle: OPENAI_API_KEY ekle

# 5. Test
python test_system.py

# 6. Çalıştır
streamlit run app.py
```

---

## 2. ARAŞTIRMADA KULLANIM

### 2.1 Katılımcı Akışı

**Adım 1: Giriş ve Onay**
- Bilgilendirilmiş onam formu
- Demografik bilgiler
- Unique ID atama

**Adım 2: Yetkinlik Değerlendirmesi**
- 10 soru (5 technical + 5 educational)
- Otomatik skorlama
- Profil oluşturma

**Adım 3: Dual-Mode Tavsiyeleri**
- Similarity mode sonuçları
- Complementary mode sonuçları
- Kullanıcı tercih kaydı

**Adım 4: Kod Üretim Görevleri**
- 6 görev (randomize sıra)
- Her görev için seçilen persona ile çalışma
- Kod üretimi ve kayıt

**Adım 5: Post-Test**
- Satisfaction survey
- NASA-TLX
- Opsiyonel interview davet

### 2.2 Veri Kayıt Noktaları

**Otomatik Loglama:**
```json
{
  "session_id": "uuid",
  "timestamp": "ISO-8601",
  "user_profile": {
    "technical_score": 45,
    "educational_score": 65,
    "level_tech": "competent",
    "level_edu": "proficient"
  },
  "recommendations": {
    "similarity_mode": ["tech_1", "tech_2", "tech_5"],
    "complementary_mode": ["edu_1", "edu_2", "edu_5"]
  },
  "selected_persona": "tech_1",
  "task": "diploma_verification",
  "code_output": "...",
  "metrics": {...},
  "duration_seconds": 1834
}
```

---

## 3. METRİKLERİN HESAPLANMASI

### 3.1 Technical Metrics

**Kod Kalitesi (Pylint):**
```python
score = 100 - (errors×10 + warnings×5 + conventions×2)
```

**Güvenlik (Bandit):**
```python
score = 100 - (high_severity×20 + medium×10 + low×5)
```

**Complexity (Radon):**
```python
if avg_complexity <= 5: score = 100
elif avg_complexity <= 10: score = 80
elif avg_complexity <= 20: score = 60
else: score = max(0, 100 - (avg_complexity-20)*2)
```

### 3.2 Pedagogical Metrics

**Öğrenme Kolaylığı:**
```python
score = (comment_ratio×0.35 + docstring×0.30 + 
         function_score×0.20 + naming×0.15)
```

**Bilişsel Yük (Düşük yük = Yüksek skor):**
```python
score = (depth_score×0.40 + complexity_score×0.40 + 
         density_score×0.20)
```

---

## 4. İSTATİSTİKSEL ANALİZ PIPELINE

### 4.1 Veri Hazırlama

```python
# 1. Clean data
df = pd.read_json('data/user_profiles.json')
df = df.dropna()
df = remove_outliers(df, method='IQR')

# 2. Transform
df['log_performance'] = np.log(df['performance'] + 1)
df['normalized_score'] = (df['score'] - df['score'].mean()) / df['score'].std()

# 3. Check assumptions
shapiro_test(df['performance'])  # Normality
levene_test(groups)  # Homogeneity of variance
```

### 4.2 Ana Analizler

**ANOVA:**
```python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

model = ols('performance ~ C(level) + C(domain) + C(mode) + '
            'C(level):C(domain) + C(level):C(mode)', 
            data=df).fit()
anova_table = anova_lm(model, typ=2)
```

**Regression:**
```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

X = df[['expertise', 'mode_binary', 'task_complexity']]
y = df['performance']

model = Ridge(alpha=1.0)
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
```

**Effect Size:**
```python
def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std
```

---

## 5. RAPORLAMA STANDARTLARI

### 5.1 APA 7th Edition

- Tüm istatistikler: M(SD) formatında
- p-values: p<0.05, p<0.01, p<0.001
- Effect sizes: Her significant test için
- Confidence intervals: 95% CI

### 5.2 Tablo Formatı

**Örnek - Descriptive Statistics:**

| Variable | N | M | SD | Min | Max | Skewness | Kurtosis |
|----------|---|---|----|----|-----|----------|----------|
| Technical Score | 150 | 52.3 | 18.7 | 5 | 95 | -0.12 | -0.45 |
| Educational Score | 150 | 48.9 | 21.2 | 5 | 98 | 0.08 | -0.52 |

### 5.3 Şekil Standardları

- High resolution (300 DPI)
- Colorblind-friendly palettes
- Clear labels and legends
- APA style captions

---

## 6. ETİK PROTOKOL

### 6.1 Etik Kurul Onayı

**Başvuru Belgeleri:**
- Araştırma protokolü
- Informed consent form
- Participant information sheet
- Data management plan
- Risk assessment

**Onay Süreci:** 4-6 hafta

### 6.2 Katılımcı Hakları

- Gönüllü katılım
- İstediği zaman çıkma hakkı
- Veri silme talebi
- Anonimlik garantisi
- Sonuçlara erişim

---

**Sayfa Sayısı:** 25-30 sayfa  
**Kod Örnekleri:** 15-20 snippet  
**Akış Şemaları:** 5-6 adet

