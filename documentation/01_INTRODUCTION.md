# BÖLÜM 1: GİRİŞ

## 1.1 ARAŞTIRMANIN KONUSU

Yapay zeka teknolojilerinin eğitim alanında hızla yaygınlaşmasıyla birlikte, insan-AI işbirliği modelleri kritik bir araştırma alanı haline gelmiştir. Özellikle büyük dil modelleri (Large Language Models - LLM), kod üretimi, içerik oluşturma ve problem çözme gibi alanlarda insan yeteneklerini desteklemekte veya artırmaktadır. Ancak, farklı yetkinlik seviyelerindeki kullanıcıların AI sistemleriyle etkileşiminde ne tür farklılıklar olduğu ve optimal işbirliği modelinin nasıl tasarlanması gerektiği soruları henüz yeterince araştırılmamıştır.

Bu araştırma, **blockchain tabanlı eğitim teknolojileri** bağlamında, farklı yetkinlik seviyelerindeki kullanıcıların (pedagogical vs technical expertise) AI persona'larıyla etkileşimini inceler ve **dual-mode adaptive recommendation framework** önermektedir.

### Araştırmanın Özgün Değeri:

1. **İlk defa** similarity-based ve complementary-based tavsiye stratejilerini birleştiren hibrit model
2. **Blockchain eğitim** sistemleri için özel tasarlanmış persona-based yaklaşım
3. **6 katmanlı matematiksel framework** ile kapsamlı modelleme
4. **Pedagogical vs Technical expertise** dikotomisinin empirik analizi

---

## 1.2 PROBLEM DURUMU

### 1.2.1 Mevcut Durum

Blockchain teknolojileri eğitim sektöründe giderek daha fazla kullanılmakta, diploma doğrulama, sertifika yönetimi, öğrenci kayıtları ve akademik credential'ların saklanması gibi alanlarda uygulanmaktadır (Grech & Camilleri, 2017; Chen et al., 2018). Ancak, bu sistemlerin geliştirilmesi hem **teknik yetkinlik** (blockchain, smart contract, Solidity) hem de **pedagogical expertise** (eğitim teorileri, öğrenme tasarımı, kullanıcı ihtiyaçları) gerektirmektedir.

### 1.2.2 Literatürdeki Boşluklar

Mevcut literatür taraması (N=247 makale, 2018-2025) şu boşlukları ortaya koymuştur:

**Boşluk 1: Yetkinlik-Bazlı AI Etkileşimi**
- LLM performans çalışmaları çoğunlukla model-centric (Wei et al., 2022)
- Kullanıcı yetkinliğinin etkisi ihmal edilmiş
- Dreyfus Model'in AI bağlamında uygulaması yok

**Boşluk 2: Pedagogical vs Technical Dichotomy**
- Blockchain eğitim literatüründe teknik odak dominant
- Pedagogical design perspective eksik (sadece %12 çalışma)
- İki uzmanlık alanının işbirliği modellenmemiş

**Boşluk 3: Recommendation Strategy**
- Mevcut sistemler similarity-based (collaborative filtering)
- Complementary-based yaklaşım eksik
- Dual-mode adaptive sistemler yok

### 1.2.3 Pratik İhtiyaç

Eğitim kurumları ve EdTech şirketleri şu sorunlarla karşılaşmaktadır:

- **Yetkinlik uyuşmazlığı:** Eğitimciler blockchain bilmiyor, developer'lar pedagoji bilmiyor
- **Suboptimal sistemler:** Ya teknik mükemmel/pedagojik zayıf ya da tersi
- **Yüksek maliyet:** Trial-error ile doğru uzman bulma
- **Sürdürülebilirlik:** Doğru işbirliği modeli olmadan projeler başarısız

---

## 1.3 ARAŞTIRMANIN AMACI VE ÖNEMİ

### 1.3.1 Genel Amaç

Bu araştırmanın genel amacı, blockchain tabanlı eğitim teknolojilerinin geliştirilmesinde, **farklı yetkinlik profillerine sahip kullanıcılar için optimal AI persona tavsiye sistemini** tasarlamak, matematiksel olarak modellemek ve empirik olarak validate etmektir.

### 1.3.2 Özel Amaçlar

1. Kullanıcı yetkinliğinin **çok boyutlu vektör reprezentasyonunu** (10-dimensional) oluşturmak
2. **Dual-mode recommendation algoritmasını** (similarity + complementary) geliştirmek
3. Pedagogical ve technical expertise'in **optimal ağırlıklarını** belirlemek
4. **6 katmanlı matematiksel framework** ile model validasyonu yapmak
5. **N=150 katılımcı** ile empirik veri toplamak ve hipotezleri test etmek

### 1.3.3 Araştırmanın Önemi

#### Teorik Önem:

- **Yeni teorik framework:** Dual-mode recommendation (similarity + complementary)
- **Genişletilmiş model:** Dreyfus Model + bilgi türleri + bilişsel faktörler
- **Dikotomi teorisi:** Pedagogical-Technical expertise trade-off'u

#### Metodolojik Önem:

- **6-layer mathematical framework:** Kapsamlı modelleme yaklaşımı
- **Persona-as-proxy:** Simulated expertise metodolojisi
- **Dual-perspective metrics:** Technical + Pedagogical değerlendirme

#### Pratik Önem:

- **EdTech kurumları:** Doğru uzman eşleştirmesi
- **Eğitimciler:** AI asistanları ile etkili çalışma
- **Developer'lar:** Pedagogical awareness kazanma
- **Politika yapıcılar:** AI-human collaboration standartları

---

## 1.4 ARAŞTIRMA SORULARI VE HİPOTEZLER

### 1.4.1 Ana Araştırma Sorusu

**AS-MAIN:** "Blockchain tabanlı eğitim sistemleri geliştirmede, dual-mode adaptive recommendation framework'ün (similarity + complementary), kullanıcı performansı ve öğrenme kazanımları üzerindeki etkisi nedir ve optimal mod seçimi hangi faktörlere bağlıdır?"

### 1.4.2 Alt Araştırma Soruları

**AS1:** Farklı yetkinlik seviyelerindeki kullanıcılar (Dreyfus: Novice→Expert), AI persona'larıyla etkileşimde nasıl farklılaşır ve bu farklılık matematiksel olarak nasıl modellenir?

**AS2:** Pedagogical expertise ve technical expertise arasındaki trade-off nedir ve blockchain eğitim sistemlerinde optimal denge nasıl kurulur?

**AS3:** Similarity-based ve complementary-based recommendation stratejilerinin, farklı kullanıcı hedeflerinde (learning vs production) etkinliği nasıl değişir?

**AS4:** 6 katmanlı matematiksel framework, kullanıcı-persona matching doğruluğunu ve performans tahminini ne ölçüde iyileştirir?

**AS5:** Multi-LLM ortamında (OpenAI, Claude, Gemini, Grok), aynı persona karakteristiği farklı modeller tarafından nasıl yansıtılır ve performans farkları nelerdir?

### 1.4.3 Hipotezler

#### **H1: Yetkinlik-Performans İlişkisi**

H1a: Kullanıcı yetkinlik seviyesi ile AI-assisted performans arasında logaritmik ilişki vardır (R²>0.65)

H1b: Technical expertise, kod kalitesi üzerinde büyük etki gösterir (Cohen's d>0.8)

H1c: Pedagogical expertise, öğrenme kolaylığı üzerinde büyük etki gösterir (Cohen's d>0.8)

#### **H2: Dual-Mode Effectiveness**

H2a: Learning goal için complementary-mode, similarity-mode'dan anlamlı derecede daha etkilidir (p<0.05)

H2b: Production goal için similarity-mode, complementary-mode'dan anlamlı derecede daha etkilidir (p<0.05)

H2c: Adaptive hybrid mode, her iki single-mode'dan üstündür (F-test, p<0.01)

#### **H3: Expertise Dichotomy**

H3a: Pedagogical ve technical expertise arasında negatif korelasyon vardır (r<-0.5)

H3b: Optimal blockchain education system için: 60% technical + 40% pedagogical ağırlıklandırması idealdir

H3c: Pure technical veya pure pedagogical yaklaşımlar, hybrid yaklaşımdan %35+ daha düşük performans gösterir

#### **H4: Mathematical Model Validation**

H4a: 6-layer framework, baseline (simple matching) yöntemine göre %40+ doğruluk artışı sağlar

H4b: Recommendation score ile actual performance arasında güçlü korelasyon vardır (r>0.75)

H4c: Model, cross-validation'da tutarlı performans gösterir (κ>0.8)

---

## 1.5 SAYILTILAR VE SINIRLILIKLAR

### 1.5.1 Sayıltılar

1. Katılımcılar, anket sorularını dürüstçe ve dikkatli bir şekilde cevaplamışlardır
2. LLM'ler (OpenAI GPT-4o), tutarlı kalitede kod üretmektedir
3. Persona karakteristikleri, gerçek uzman davranışlarını yeterince temsil etmektedir
4. Blockchain eğitim sistemleri, genel eğitim teknolojilerine genellenebilir
5. 18 aylık araştırma süresi, yeterli veri toplama için yeterlidir

### 1.5.2 Sınırlılıklar

**Örneklem Sınırlılıkları:**
- N=150 katılımcı (ideal: 200+)
- Türkiye merkezli (kültürel genelleme sınırlı)
- Gönüllü katılım (selection bias riski)

**Metodolojik Sınırlılıklar:**
- Simulated personas (gerçek uzman değil)
- Single task per participant (learning curve sınırlı)
- Short-term effects (longitudinal sınırlı)

**Teknolojik Sınırlılıklar:**
- LLM API değişimleri (OpenAI model updates)
- Cost constraints (full multi-LLM test pahalı)
- Platform dependency (Streamlit-specific)

**Genelleme Sınırlılıkları:**
- Blockchain-education domain specific
- Code generation odaklı (diğer AI tasks?)
- Academic setting (industry farklı olabilir)

---

## 1.6 TANIMLAR

### Operasyonel Tanımlar:

**Yetkinlik (Competency):** Dreyfus Model'e göre 5 seviye (Novice, Advanced Beginner, Competent, Proficient, Expert), 0-100 skalada ölçülen beceri düzeyi

**AI Persona:** Belirli uzmanlık profili ve kod üretim stiline sahip, LLM-powered sanal uzman karakteri

**Dual-Mode Recommendation:** Similarity-based (benzerlik) ve complementary-based (tamamlayıcılık) stratejilerini birleştiren adaptif tavsiye sistemi

**Pedagogical Expertise:** Eğitim teorileri, öğretim tasarımı, öğrenci ihtiyaçları konusunda uzmanlık (0-100 skor)

**Technical Expertise:** Blockchain, smart contract, Solidity, software engineering konusunda uzmanlık (0-100 skor)

**Performance Score:** Kod kalitesi, güvenlik, gas efficiency, pedagogical value'nun ağırlıklı kombinasyonu (0-100)

**Complementarity:** Kullanıcının zayıf olduğu, persona'nın güçlü olduğu alanların matematiksel ölçüsü (0-1)

### Kısaltmalar:

- **PIDL:** Persona in the Loop
- **LLM:** Large Language Model
- **DApp:** Decentralized Application
- **ZPD:** Zone of Proximal Development
- **MCDA:** Multi-Criteria Decision Analysis
- **CLT:** Cognitive Load Theory

---

## 1.7 ARAŞTIRMANIN KAPSAMI

### Kapsam İçi:

✅ Blockchain-based eğitim sistemleri (diploma, sertifika, burs)  
✅ Kod üretimi (Python, Solidity)  
✅ 10 AI persona (5 pedagogical + 5 technical)  
✅ Dual-domain assessment (technical + educational)  
✅ Dual-mode recommendation (similarity + complementary)  
✅ N=150 katılımcı (5 seviye × 2 domain × 15 kişi)  

### Kapsam Dışı:

❌ Diğer blockchain use-case'ler (DeFi, NFT marketplaces)  
❌ Kod dışı AI görevleri (text generation, image creation)  
❌ Gerçek uzmanlarla çalışma (sadece simulated personas)  
❌ Longitudinal follow-up (>6 ay)  
❌ Çocuk katılımcılar (<18 yaş)  

---

## 1.8 BÖLÜM SONUÇ NOTLARI

Bu giriş bölümü, araştırmanın:
- **Konusunu** ve **önemini** netleştirmiştir
- **Problem durumunu** ve **boşlukları** ortaya koymuştur
- **Araştırma sorularını** ve **hipotezleri** tanımlamıştır
- **Kapsamı** ve **sınırlılıkları** belirlemiştir

**Sonraki bölüm (Bölüm 2):** Kuramsal çerçeve ve literatür taraması, bu araştırmanın teorik temellerini ve mevcut bilgi birikimini detaylı inceleyecektir.

---

**Sayfa Sayısı:** 20-25 sayfa (literatür referansları ile)  
**Tablo/Şekil:** 2-3 adet (conceptual model, research gap matrix)  
**Kaynak Sayısı:** 30-40 referans

