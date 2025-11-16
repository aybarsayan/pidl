"""
Synthetic Data Generator - Test Amaçlı Veri Üretimi
UYARI: Bu veri SADECE platform testi içindir, gerçek araştırmada kullanılamaz!

HTML'deki bulguları tersine mühendislik yaparak N=150 sentetik veri seti oluşturur.
"""

import random
import json
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os
import numpy as np

# Random seed for reproducibility
random.seed(42)
np.random.seed(42)

# =============================================================================
# BULGULARDAN ÇIKARIMLAR (doktora_tezi_full.html)
# =============================================================================

TOTAL_PARTICIPANTS = 150

# Demografik Dağılım
AGE_RANGE = (22, 45)
AGE_MEAN = 28.5
AGE_STD = 4.2

GENDER_DIST = {"Erkek": 0.68, "Kadın": 0.32}

EDUCATION_DIST = {
    "Lisans": 0.42,
    "Yüksek Lisans": 0.38,
    "Doktora": 0.20
}

WORK_FIELD_DIST = {
    "Yazılım Geliştirme": 0.45,
    "Eğitim": 0.28,
    "Akademik Araştırma": 0.27
}

# Dreyfus Seviye Dağılımı
DREYFUS_DIST = {
    "Novice": 0.22,  # 33 kişi
    "Advanced Beginner": 0.26,  # 39 kişi
    "Competent": 0.28,  # 42 kişi
    "Proficient": 0.16,  # 24 kişi
    "Expert": 0.08  # 12 kişi
}

DREYFUS_SCORE_RANGES = {
    "Novice": (0, 30),
    "Advanced Beginner": (25, 50),
    "Competent": (45, 70),
    "Proficient": (65, 85),
    "Expert": (80, 100)
}

# 10 Persona tanımları
PERSONAS = {
    "pedagogical": [
        {"id": "edu_novice", "name": "Dr. Ayşe - Beginner Friendly", "level": "Novice"},
        {"id": "edu_advanced_beginner", "name": "Prof. Mehmet - Academic", "level": "Advanced Beginner"},
        {"id": "edu_competent", "name": "Öğretmen Zeynep - Practical", "level": "Competent"},
        {"id": "edu_proficient", "name": "Ali - Facilitator", "level": "Proficient"},
        {"id": "edu_expert", "name": "Mentor Fatma - Supportive", "level": "Expert"}
    ],
    "technical": [
        {"id": "tech_novice", "name": "Ahmet - Smart Contract Beginner", "level": "Novice"},
        {"id": "tech_advanced_beginner", "name": "Elif - Security Aware", "level": "Advanced Beginner"},
        {"id": "tech_competent", "name": "Can - Gas Optimizer", "level": "Competent"},
        {"id": "tech_proficient", "name": "Deniz - DApp Architect", "level": "Proficient"},
        {"id": "tech_expert", "name": "Burak - Blockchain Specialist", "level": "Expert"}
    ]
}

# Persona Performance Rankings (HTML'den)
PERSONA_PERFORMANCE = {
    "Can - Gas Optimizer": 8.4,
    "Prof. Mehmet - Academic": 8.2,
    "Deniz - DApp Architect": 8.1,
    "Öğretmen Zeynep - Practical": 7.9,
    "Ali - Facilitator": 7.8,
    "Elif - Security Aware": 7.6,
    "Ahmet - Smart Contract Beginner": 7.4,
    "Dr. Ayşe - Beginner Friendly": 7.3,
    "Mentor Fatma - Supportive": 7.5,
    "Burak - Blockchain Specialist": 7.7
}

# Task listesi (HTML'den)
TASKS = [
    "Token Transfer Contract - ERC20 benzeri basit token",
    "Voting System - Basit oylama mekanizması",
    "Escrow Contract - Güvenli ödeme sistemi",
    "NFT Minting - ERC721 benzeri NFT",
    "Staking Contract - Token stake etme",
    "Auction System - Açık artırma sistemi"
]

# =============================================================================
# VERİ OLUŞTURMA FONKSİYONLARI
# =============================================================================

def generate_participant_demographics() -> Dict:
    """Bir katılımcının demografik bilgilerini oluştur"""

    # Yaş (normal dağılım)
    age = int(np.random.normal(AGE_MEAN, AGE_STD))
    age = max(AGE_RANGE[0], min(AGE_RANGE[1], age))

    # Cinsiyet (weighted random)
    gender = random.choices(
        list(GENDER_DIST.keys()),
        weights=list(GENDER_DIST.values())
    )[0]

    # Eğitim
    education = random.choices(
        list(EDUCATION_DIST.keys()),
        weights=list(EDUCATION_DIST.values())
    )[0]

    # Çalışma alanı
    work_field = random.choices(
        list(WORK_FIELD_DIST.keys()),
        weights=list(WORK_FIELD_DIST.values())
    )[0]

    # Dreyfus seviyesi
    dreyfus_level = random.choices(
        list(DREYFUS_DIST.keys()),
        weights=list(DREYFUS_DIST.values())
    )[0]

    # Skorlar (dreyfus seviyesine göre)
    score_range = DREYFUS_SCORE_RANGES[dreyfus_level]
    technical_score = random.randint(score_range[0], score_range[1])

    # H5: Teknik ve pedagojik negatif korelasyon (r=-0.18)
    # Pedagojik skoru hafif negatif korelasyonla oluştur
    correlation = -0.18
    noise = np.random.normal(0, 20)
    pedagogical_score = int(50 + correlation * (technical_score - 50) + noise)
    pedagogical_score = max(0, min(100, pedagogical_score))

    return {
        "age": age,
        "gender": gender,
        "education": education,
        "work_field": work_field,
        "technical_score": technical_score,
        "pedagogical_score": pedagogical_score,
        "competency_level": dreyfus_level
    }


def select_persona_for_mode(mode: str, technical_score: int, pedagogical_score: int, dreyfus_level: str) -> Dict:
    """Mode'a göre persona seç (Similar veya Complementary)"""

    # Dominant domain'i belirle
    if pedagogical_score > technical_score:
        domain = "pedagogical"
    else:
        domain = "technical"

    # Mode'a göre persona seç
    if mode == "Similar":
        # Aynı seviyede persona
        personas_at_level = [p for p in PERSONAS[domain] if p["level"] == dreyfus_level]
        if not personas_at_level:
            personas_at_level = [PERSONAS[domain][2]]  # Competent default
        persona = random.choice(personas_at_level)
    else:  # Complementary
        # 1-2 seviye üstte persona
        level_order = ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]
        current_idx = level_order.index(dreyfus_level)
        target_idx = min(current_idx + 2, len(level_order) - 1)
        target_level = level_order[target_idx]

        personas_at_level = [p for p in PERSONAS[domain] if p["level"] == target_level]
        if not personas_at_level:
            personas_at_level = [PERSONAS[domain][-1]]  # Expert default
        persona = random.choice(personas_at_level)

    return persona


def generate_pre_post_test_answers(dreyfus_level: str, test_type: str, ai_mode: str) -> Dict:
    """Pre-test veya Post-test cevaplarını oluştur"""

    # Base score dreyfus seviyesine göre
    base_scores = {
        "Novice": 2,
        "Advanced Beginner": 3,
        "Competent": 4,
        "Proficient": 5,
        "Expert": 5
    }

    base_score = base_scores[dreyfus_level]

    # Post-test için learning gain ekle
    if test_type == "post":
        # H2: Complementary mode daha yüksek learning outcomes (d=0.76)
        if ai_mode == "Complementary":
            # Novice için daha fazla gain (H4: d=1.24)
            if dreyfus_level == "Novice":
                gain = random.randint(2, 3)
            else:
                gain = random.randint(1, 2)
        else:  # Similar
            if dreyfus_level == "Novice":
                gain = random.randint(1, 2)
            else:
                gain = random.randint(0, 1)

        base_score = min(5, base_score + gain)

    # 5 soru için cevaplar
    answers = {}
    for i in range(1, 6):
        # Base score etrafında rastgele dağılım
        score = base_score + random.randint(-1, 1)
        score = max(0, min(5, score))
        answers[f"q{i}"] = str(score)

    total_score = sum(int(answers[f"q{i}"]) for i in range(1, 6))

    return {"answers": answers, "score": total_score}


def generate_nasa_tlx(dreyfus_level: str, ai_mode: str) -> Dict:
    """NASA-TLX bilişsel yük değerlerini oluştur"""

    # Base cognitive load
    base_loads = {
        "Novice": 7,
        "Advanced Beginner": 6,
        "Competent": 5,
        "Proficient": 4,
        "Expert": 3
    }

    base = base_loads[dreyfus_level]

    # Complementary biraz daha yüksek cognitive load
    if ai_mode == "Complementary":
        base += random.randint(0, 1)

    # 6 dimension (1-10 scale)
    mental_demand = min(10, max(1, base + random.randint(-1, 2)))
    physical_demand = random.randint(1, 3)  # Genelde düşük
    temporal_demand = min(10, max(1, base + random.randint(-1, 1)))
    performance = 10 - mental_demand + random.randint(0, 2)  # Inverse
    effort = min(10, max(1, base + random.randint(-1, 1)))
    frustration = min(10, max(1, base + random.randint(-2, 1)))

    total_load = mental_demand + physical_demand + temporal_demand + (10 - performance) + effort + frustration

    return {
        "mental_demand": mental_demand,
        "physical_demand": physical_demand,
        "temporal_demand": temporal_demand,
        "performance": performance,
        "effort": effort,
        "frustration": frustration,
        "total_cognitive_load": total_load
    }


def generate_ai_evaluation(dreyfus_level: str, ai_mode: str, persona_name: str) -> Dict:
    """AI kod değerlendirmesi oluştur"""

    # Base satisfaction
    base_satisfaction = {
        "Novice": 7,
        "Advanced Beginner": 7,
        "Competent": 8,
        "Proficient": 8,
        "Expert": 7
    }

    base = base_satisfaction[dreyfus_level]

    # H1: Similar mode daha yüksek satisfaction (d=0.89)
    # H3: EXCEPT Expert seviyede fark yok
    if dreyfus_level == "Expert":
        # Expert: Mode farkı yok
        base = 7 + random.randint(0, 1)
    else:
        # Diğer seviyeler: Similar daha yüksek
        if ai_mode == "Similar":
            base += random.randint(1, 2)
        else:
            base += random.randint(0, 1)

    # Persona performance etkisi
    persona_boost = PERSONA_PERFORMANCE.get(persona_name, 7.5) - 7.5
    base += int(persona_boost)

    base = max(1, min(10, base))

    # 5 metrik
    code_understandability = base + random.randint(-1, 1)
    explanation_quality = base + random.randint(-1, 1)

    # H4: Novice seviyede Complementary daha etkili (educational value)
    if dreyfus_level == "Novice":
        if ai_mode == "Complementary":
            educational_value = base + random.randint(1, 2)  # Boost for Complementary
        else:
            educational_value = base + random.randint(-1, 0)  # Lower for Similar
    else:
        educational_value = base + random.randint(-1, 1)

    perceived_code_quality = base + random.randint(-1, 1)
    perceived_security = base + random.randint(-1, 1)

    # Clamp to 1-10
    code_understandability = max(1, min(10, code_understandability))
    explanation_quality = max(1, min(10, explanation_quality))
    educational_value = max(1, min(10, educational_value))
    perceived_code_quality = max(1, min(10, perceived_code_quality))
    perceived_security = max(1, min(10, perceived_security))

    return {
        "code_understandability": code_understandability,
        "explanation_quality": explanation_quality,
        "educational_value": educational_value,
        "perceived_code_quality": perceived_code_quality,
        "perceived_security": perceived_security,
        "best_aspect": random.choice([
            "Açıklamalar çok netti",
            "Kod kalitesi iyiydi",
            "Adım adım öğretiyordu",
            "Güvenlik konusunda bilinçliydi",
            "Örnekler gerçekçiydi"
        ]),
        "improvement_needed": random.choice([
            "Daha fazla örnek olabilir",
            "Gas optimizasyonu eklenebilir",
            "Daha detaylı güvenlik analizi",
            "Görsel diyagramlar olabilir",
            ""
        ])
    }


def generate_technical_metrics(dreyfus_level: str, ai_mode: str) -> Dict:
    """Technical metrics oluştur (HTML bulgularına göre)"""

    # HTML'deki ortalamalar: Security 7.2±1.8, Gas 6.8±1.9, Quality 7.5±1.6

    base_technical = {
        "Novice": 6,
        "Advanced Beginner": 7,
        "Competent": 7,
        "Proficient": 8,
        "Expert": 8
    }

    base = base_technical[dreyfus_level]

    # Complementary mode biraz daha iyi teknik kalite
    if ai_mode == "Complementary":
        base += random.randint(0, 1)

    security_score = int(np.random.normal(7.2, 1.8))
    gas_optimization_score = int(np.random.normal(6.8, 1.9))
    code_quality_score = int(np.random.normal(7.5, 1.6))
    maintainability_score = base + random.randint(-1, 1)
    production_readiness = base + random.randint(-1, 1)

    # Clamp to 1-10
    security_score = max(1, min(10, security_score))
    gas_optimization_score = max(1, min(10, gas_optimization_score))
    code_quality_score = max(1, min(10, code_quality_score))
    maintainability_score = max(1, min(10, maintainability_score))
    production_readiness = max(1, min(10, production_readiness))

    # Otomatik skorlar (0-100)
    auto_security_score = security_score * 10 + random.randint(-5, 5)
    auto_gas_score = gas_optimization_score * 10 + random.randint(-5, 5)
    auto_complexity_score = 100 - (dreyfus_level == "Novice") * 20 + random.randint(-10, 10)

    return {
        "security_score": security_score,
        "gas_optimization_score": gas_optimization_score,
        "code_quality_score": code_quality_score,
        "maintainability_score": maintainability_score,
        "production_readiness": production_readiness,
        "auto_security_score": float(max(0, min(100, auto_security_score))),
        "auto_gas_score": float(max(0, min(100, auto_gas_score))),
        "auto_complexity_score": float(max(0, min(100, auto_complexity_score)))
    }


def generate_pedagogical_metrics(dreyfus_level: str, ai_mode: str) -> Dict:
    """Pedagogical metrics oluştur (HTML bulgularına göre)"""

    # HTML'deki ortalamalar: Learning 7.1±1.7, Instructiveness 7.3±1.8, Cognitive Load 4.2±1.6

    base_pedagogical = {
        "Novice": 7,
        "Advanced Beginner": 7,
        "Competent": 7,
        "Proficient": 7,
        "Expert": 6  # Expertler için çok basit olabilir
    }

    base = base_pedagogical[dreyfus_level]

    # Similar mode daha rahat öğrenme
    if ai_mode == "Similar":
        base += random.randint(0, 1)

    learning_ease_score = int(np.random.normal(7.1, 1.7))
    instructiveness_score = int(np.random.normal(7.3, 1.8))
    cognitive_load_score = int(np.random.normal(4.2, 1.6))  # Düşük=iyi
    example_quality_score = base + random.randint(-1, 1)
    scaffolding_score = base + random.randint(-1, 1)
    explanation_quality = base + random.randint(-1, 1)

    # Clamp
    learning_ease_score = max(1, min(10, learning_ease_score))
    instructiveness_score = max(1, min(10, instructiveness_score))
    cognitive_load_score = max(1, min(10, cognitive_load_score))
    example_quality_score = max(1, min(10, example_quality_score))
    scaffolding_score = max(1, min(10, scaffolding_score))
    explanation_quality = max(1, min(10, explanation_quality))

    # Bloom taxonomy
    bloom_levels = [
        "Remember (Hatırlama) - Seviye 1",
        "Understand (Anlama) - Seviye 2",
        "Apply (Uygulama) - Seviye 3",
        "Analyze (Analiz) - Seviye 4",
        "Evaluate (Değerlendirme) - Seviye 5",
        "Create (Yaratma) - Seviye 6"
    ]

    # Dreyfus seviyesine göre bloom level
    bloom_mapping = {
        "Novice": bloom_levels[1],  # Understand
        "Advanced Beginner": bloom_levels[2],  # Apply
        "Competent": bloom_levels[3],  # Analyze
        "Proficient": bloom_levels[4],  # Evaluate
        "Expert": bloom_levels[5]  # Create
    }

    bloom_level = bloom_mapping[dreyfus_level]

    return {
        "learning_ease_score": learning_ease_score,
        "instructiveness_score": instructiveness_score,
        "cognitive_load_score": cognitive_load_score,
        "example_quality_score": example_quality_score,
        "scaffolding_score": scaffolding_score,
        "bloom_taxonomy_level": bloom_level,
        "explanation_quality": explanation_quality
    }


def generate_task_comparison(task_number: int, used_ai: str, other_ai: str, dreyfus_level: str) -> Dict:
    """Task comparison verisi oluştur"""

    has_comparison = task_number > 1  # İlk task'te karşılaştırma yok

    if not has_comparison:
        return {
            "used_ai_type": used_ai,
            "other_ai_type": other_ai,
            "suitability_choice": None,
            "reason": "",
            "difficulty_rating": random.choice(["Orta", "Kolay", "Zor"]),
            "has_comparison": False
        }

    # H1: Similar daha tatmin edici
    # H2: Complementary daha öğretici

    difficulty_options = ["Çok Kolay", "Kolay", "Orta", "Zor", "Çok Zor"]

    # Difficulty dreyfus seviyesine göre
    difficulty_probs = {
        "Novice": [0.05, 0.15, 0.40, 0.30, 0.10],
        "Advanced Beginner": [0.10, 0.25, 0.40, 0.20, 0.05],
        "Competent": [0.15, 0.35, 0.35, 0.12, 0.03],
        "Proficient": [0.20, 0.40, 0.30, 0.08, 0.02],
        "Expert": [0.30, 0.40, 0.25, 0.04, 0.01]
    }

    difficulty = random.choices(difficulty_options, weights=difficulty_probs[dreyfus_level])[0]

    # Suitability choice
    suitability_options = [used_ai, other_ai, "İkisi de uygun"]

    # Similar için comfort, Complementary için learning
    if used_ai == "Similar":
        suitability_weights = [0.50, 0.20, 0.30]  # Similar daha çok tercih edilir
    else:
        suitability_weights = [0.45, 0.25, 0.30]  # Complementary de iyi ama biraz daha az

    suitability = random.choices(suitability_options, weights=suitability_weights)[0]

    reason_templates = {
        "Similar": "Rahat hissettim, seviyeme uygundu",
        "Complementary": "Daha çok öğrendim, zorlayıcıydı ama faydalı",
        "İkisi de uygun": "Her ikisinin de avantajları vardı"
    }

    reason = reason_templates.get(suitability, "")

    return {
        "used_ai_type": used_ai,
        "other_ai_type": other_ai,
        "suitability_choice": suitability,
        "reason": reason,
        "difficulty_rating": difficulty,
        "has_comparison": True
    }


def generate_final_evaluation(participant_data: Dict, all_sessions: List[Dict]) -> Dict:
    """Final evaluation formu oluştur"""

    dreyfus = participant_data["competency_level"]

    # Task modlarını say
    similar_count = sum(1 for s in all_sessions if s["assigned_ai_type"] == "Similar")
    complementary_count = sum(1 for s in all_sessions if s["assigned_ai_type"] == "Complementary")

    # H1 & H2'ye göre tercihler
    if dreyfus in ["Novice", "Advanced Beginner"]:
        # Novice/AB: Complementary daha faydalı (H4)
        preferred_ai = random.choices(
            ["Similar", "Complementary", "Hibrit"],
            weights=[0.20, 0.50, 0.30]
        )[0]
    elif dreyfus == "Expert":
        # Expert: Fark yok (H3)
        preferred_ai = random.choices(
            ["Similar", "Complementary", "Hibrit"],
            weights=[0.35, 0.35, 0.30]
        )[0]
    else:
        # Competent/Proficient: Dengeli
        preferred_ai = random.choices(
            ["Similar", "Complementary", "Hibrit"],
            weights=[0.30, 0.40, 0.30]
        )[0]

    return {
        "preferred_ai": preferred_ai,
        "preferred_ai_reason": f"Bu mod benim seviyeme daha uygundu",
        "learning_better_ai": "Complementary",  # H2
        "speed_better_ai": "Similar",  # Hız için Similar
        "comfort_similar": random.randint(7, 9),  # H1
        "development_complementary": random.randint(7, 9),  # H2
        "clarity_similar": random.randint(7, 9),
        "quality_complementary": random.randint(7, 8),
        "hybrid_ideal": random.randint(7, 9),
        "blockchain_view_change": random.choice([
            "Evet, artık blockchain daha anlaşılır",
            "Kısmen, bazı konular netleşti",
            "Hayır, zaten bilgim vardı"
        ]),
        "ai_learning_rating": random.randint(7, 10),
        "would_recommend": random.choice(["Evet", "Evet", "Kısmen"]),
        "hardest_task": random.choice(TASKS),
        "ai_potential": "Blockchain eğitiminde AI çok faydalı",
        "suggestions": random.choice([
            "Daha fazla örnek olabilir",
            "Görsel diyagramlar eklenebilir",
            "Daha interaktif olabilir",
            ""
        ]),
        "blockchain_education_view": "AI destekli eğitim gelecek vaat ediyor"
    }


# =============================================================================
# ANA VERİ OLUŞTURMA FONKSİYONU
# =============================================================================

def generate_all_synthetic_data() -> Dict:
    """150 katılımcı için tüm sentetik veriyi oluştur"""

    print("🎲 Sentetik veri üretimi başlıyor...")
    print(f"📊 Hedef: {TOTAL_PARTICIPANTS} katılımcı × 6 task = {TOTAL_PARTICIPANTS * 6} session\n")

    all_data = {
        "participants": [],
        "task_sessions": [],
        "pre_post_tests": [],
        "generated_codes": [],
        "nasa_tlx_responses": [],
        "ai_code_evaluations": [],
        "technical_metrics": [],
        "pedagogical_metrics": [],
        "task_comparisons": [],
        "final_evaluations": [],
        "metadata": {
            "total_participants": TOTAL_PARTICIPANTS,
            "total_sessions": TOTAL_PARTICIPANTS * 6,
            "generation_date": datetime.now().isoformat(),
            "warning": "SENTETIK VERİ - Sadece test amaçlı!"
        }
    }

    participant_id = 1
    session_id = 1
    code_id = 1

    for i in range(TOTAL_PARTICIPANTS):
        # Participant oluştur
        participant = generate_participant_demographics()
        participant["participant_id"] = participant_id
        participant["uuid"] = f"participant_{participant_id:03d}"
        participant["consent_given"] = True
        participant["completed"] = True
        participant["total_duration_minutes"] = random.randint(240, 300)  # 4-5 saat
        participant["created_at"] = (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat()

        all_data["participants"].append(participant)

        # 6 task session (counterbalanced: 3 Similar + 3 Complementary)
        modes = ["Similar"] * 3 + ["Complementary"] * 3
        random.shuffle(modes)

        participant_sessions = []

        for task_num in range(6):
            ai_mode = modes[task_num]
            other_mode = "Complementary" if ai_mode == "Similar" else "Similar"
            task_name = TASKS[task_num]

            # Persona seç
            persona = select_persona_for_mode(
                ai_mode,
                participant["technical_score"],
                participant["pedagogical_score"],
                participant["competency_level"]
            )

            # Task session
            session = {
                "session_id": session_id,
                "participant_uuid": participant["uuid"],
                "task_number": task_num + 1,
                "task_name": task_name,
                "assigned_ai_type": ai_mode,
                "assigned_persona": persona["name"],
                "status": "Completed",
                "duration_minutes": random.randint(35, 55),
                "started_at": participant["created_at"],
                "completed_at": participant["created_at"]
            }
            all_data["task_sessions"].append(session)
            participant_sessions.append(session)

            # Pre-test
            pre_test = generate_pre_post_test_answers(participant["competency_level"], "pre", ai_mode)
            all_data["pre_post_tests"].append({
                "session_id": session_id,
                "test_type": "pre",
                **pre_test["answers"],
                "score": pre_test["score"]
            })

            # Post-test
            post_test = generate_pre_post_test_answers(participant["competency_level"], "post", ai_mode)
            all_data["pre_post_tests"].append({
                "session_id": session_id,
                "test_type": "post",
                **post_test["answers"],
                "score": post_test["score"]
            })

            # Generated code
            code_entry = {
                "code_id": code_id,
                "session_id": session_id,
                "code_text": f"// {task_name}\\n// Generated by {persona['name']}\\npragma solidity ^0.8.0;\\n\\ncontract Example {{ }}",
                "language": "solidity",
                "prompt_used": f"Create a {task_name}",
                "ai_persona": persona["name"],
                "generation_time_seconds": random.randint(30, 120)
            }
            all_data["generated_codes"].append(code_entry)

            # NASA-TLX
            nasa_tlx = generate_nasa_tlx(participant["competency_level"], ai_mode)
            nasa_tlx["session_id"] = session_id
            all_data["nasa_tlx_responses"].append(nasa_tlx)

            # AI Evaluation
            ai_eval = generate_ai_evaluation(participant["competency_level"], ai_mode, persona["name"])
            ai_eval["session_id"] = session_id
            all_data["ai_code_evaluations"].append(ai_eval)

            # Technical Metrics
            tech_metrics = generate_technical_metrics(participant["competency_level"], ai_mode)
            tech_metrics["code_id"] = code_id
            all_data["technical_metrics"].append(tech_metrics)

            # Pedagogical Metrics
            ped_metrics = generate_pedagogical_metrics(participant["competency_level"], ai_mode)
            ped_metrics["code_id"] = code_id
            all_data["pedagogical_metrics"].append(ped_metrics)

            # Task Comparison
            task_comp = generate_task_comparison(task_num + 1, ai_mode, other_mode, participant["competency_level"])
            task_comp["session_id"] = session_id
            all_data["task_comparisons"].append(task_comp)

            session_id += 1
            code_id += 1

        # Final Evaluation
        final_eval = generate_final_evaluation(participant, participant_sessions)
        final_eval["participant_uuid"] = participant["uuid"]
        all_data["final_evaluations"].append(final_eval)

        participant_id += 1

        if (i + 1) % 30 == 0:
            print(f"✅ {i + 1}/{TOTAL_PARTICIPANTS} katılımcı oluşturuldu")

    print(f"\n✅ Tüm veri oluşturuldu!")
    return all_data


def save_data_to_files(data: Dict, output_dir: str):
    """Veriyi JSON ve CSV formatlarında kaydet"""

    os.makedirs(output_dir, exist_ok=True)

    # JSON formatında kaydet (tüm veri)
    json_path = os.path.join(output_dir, "synthetic_data_full.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 JSON kaydedildi: {json_path}")

    # Her tablo için ayrı CSV
    for table_name, records in data.items():
        if table_name == "metadata":
            continue

        if not records:
            continue

        csv_path = os.path.join(output_dir, f"{table_name}.csv")

        # CSV yazma
        keys = records[0].keys()
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(records)

        print(f"💾 CSV kaydedildi: {csv_path} ({len(records)} satır)")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("⚠️  SENTETIK VERİ OLUŞTURUCU - SADECE TEST AMAÇLI!")
    print("="*80 + "\n")

    # Veri oluştur
    synthetic_data = generate_all_synthetic_data()

    # Klasöre kaydet
    output_directory = "synthetic_data_N150"
    save_data_to_files(synthetic_data, output_directory)

    print("\n" + "="*80)
    print("✅ İşlem tamamlandı!")
    print(f"📁 Veri klasörü: {output_directory}/")
    print("="*80 + "\n")

    # İstatistikleri yazdır
    print("📊 Veri Özeti:")
    print(f"  - Katılımcı sayısı: {len(synthetic_data['participants'])}")
    print(f"  - Task session sayısı: {len(synthetic_data['task_sessions'])}")
    print(f"  - Pre/Post test sayısı: {len(synthetic_data['pre_post_tests'])}")
    print(f"  - Üretilen kod sayısı: {len(synthetic_data['generated_codes'])}")
    print(f"  - NASA-TLX yanıt sayısı: {len(synthetic_data['nasa_tlx_responses'])}")
    print(f"  - AI değerlendirme sayısı: {len(synthetic_data['ai_code_evaluations'])}")
    print(f"  - Technical metrik sayısı: {len(synthetic_data['technical_metrics'])}")
    print(f"  - Pedagogical metrik sayısı: {len(synthetic_data['pedagogical_metrics'])}")
    print(f"  - Task karşılaştırma sayısı: {len(synthetic_data['task_comparisons'])}")
    print(f"  - Final değerlendirme sayısı: {len(synthetic_data['final_evaluations'])}")
