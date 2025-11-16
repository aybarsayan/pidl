"""
Persona Selector - 10 Persona arasından kullanıcı yetkinliğine göre seçim
"""

import random
from typing import Dict, List


# HTML'deki gibi 10 persona tanımı
ACTIVE_PERSONAS = {
    "pedagogical": [
        {
            "id": "edu_novice",
            "name": "Dr. Ayşe - Beginner Friendly",
            "description": "Çok açıklayıcı, basit, adım adım öğreten",
            "dreyfus_level": "novice",
            "technical_score_range": (0, 30),
            "pedagogical_score_range": (0, 30)
        },
        {
            "id": "edu_advanced_beginner",
            "name": "Prof. Mehmet - Academic",
            "description": "Akademik yaklaşım, theory-based",
            "dreyfus_level": "advanced_beginner",
            "technical_score_range": (20, 50),
            "pedagogical_score_range": (20, 50)
        },
        {
            "id": "edu_competent",
            "name": "Öğretmen Zeynep - Practical",
            "description": "Pratik örnekler, uygulamalı öğrenme",
            "dreyfus_level": "competent",
            "technical_score_range": (40, 70),
            "pedagogical_score_range": (40, 70)
        },
        {
            "id": "edu_proficient",
            "name": "Ali - Facilitator",
            "description": "Yönlendirici, collaborative learning",
            "dreyfus_level": "proficient",
            "technical_score_range": (60, 85),
            "pedagogical_score_range": (60, 85)
        },
        {
            "id": "edu_expert",
            "name": "Mentor Fatma - Supportive",
            "description": "Destekleyici, mentörlük odaklı",
            "dreyfus_level": "expert",
            "technical_score_range": (75, 100),
            "pedagogical_score_range": (75, 100)
        }
    ],
    "technical": [
        {
            "id": "tech_novice",
            "name": "Ahmet - Smart Contract Beginner",
            "description": "Temel Solidity, basit kontratlar",
            "dreyfus_level": "novice",
            "technical_score_range": (0, 30),
            "pedagogical_score_range": (0, 30)
        },
        {
            "id": "tech_advanced_beginner",
            "name": "Elif - Security Aware",
            "description": "Güvenlik odaklı, basic security patterns",
            "dreyfus_level": "advanced_beginner",
            "technical_score_range": (20, 50),
            "pedagogical_score_range": (20, 50)
        },
        {
            "id": "tech_competent",
            "name": "Can - Gas Optimizer",
            "description": "Gas optimization, efficiency",
            "dreyfus_level": "competent",
            "technical_score_range": (40, 70),
            "pedagogical_score_range": (40, 70)
        },
        {
            "id": "tech_proficient",
            "name": "Deniz - DApp Architect",
            "description": "Architecture patterns, scalable design",
            "dreyfus_level": "proficient",
            "technical_score_range": (60, 85),
            "pedagogical_score_range": (60, 85)
        },
        {
            "id": "tech_expert",
            "name": "Burak - Blockchain Specialist",
            "description": "Advanced patterns, protocol-level",
            "dreyfus_level": "expert",
            "technical_score_range": (75, 100),
            "pedagogical_score_range": (75, 100)
        }
    ]
}


def select_persona_by_scores(
    technical_score: int,
    pedagogical_score: int,
    mode: str = "auto"
) -> Dict:
    """
    Kullanıcı skorlarına göre persona seç

    Args:
        technical_score: Teknik yetkinlik skoru (0-100)
        pedagogical_score: Pedagojik yetkinlik skoru (0-100)
        mode: "auto", "pedagogical", "technical"

    Returns:
        Dict: Seçilen persona bilgileri
    """
    # Mode'a göre persona pool'u seç
    if mode == "pedagogical":
        pool = ACTIVE_PERSONAS["pedagogical"]
    elif mode == "technical":
        pool = ACTIVE_PERSONAS["technical"]
    else:  # auto
        # Hangi skor daha yüksekse o domain'den seç
        if pedagogical_score > technical_score:
            pool = ACTIVE_PERSONAS["pedagogical"]
        else:
            pool = ACTIVE_PERSONAS["technical"]

    # Skor aralığına göre uygun persona'ları filtrele
    suitable_personas = []
    dominant_score = max(technical_score, pedagogical_score)

    for persona in pool:
        tech_min, tech_max = persona["technical_score_range"]
        ped_min, ped_max = persona["pedagogical_score_range"]

        # Dominant score, persona'nın range'ine uyuyor mu?
        if tech_min <= dominant_score <= tech_max or ped_min <= dominant_score <= ped_max:
            suitable_personas.append(persona)

    # Eğer hiç uygun bulunamazsa, en yakın seviyeyi seç
    if not suitable_personas:
        # Ortadaki persona'yı seç (competent)
        suitable_personas = [pool[2]]

    # Random seçim yap (aynı seviyede birden fazla uygun varsa)
    selected = random.choice(suitable_personas)

    return selected


def select_similar_persona(
    technical_score: int,
    pedagogical_score: int
) -> Dict:
    """
    Similar mode: Kullanıcıyla benzer seviyede persona seç (±10 puan)

    Args:
        technical_score: Teknik yetkinlik skoru (0-100)
        pedagogical_score: Pedagojik yetkinlik skoru (0-100)

    Returns:
        Dict: Benzer seviye persona
    """
    return select_persona_by_scores(technical_score, pedagogical_score, mode="auto")


def select_complementary_persona(
    technical_score: int,
    pedagogical_score: int
) -> Dict:
    """
    Complementary mode: Kullanıcıdan 1-2 seviye üstte persona seç

    Args:
        technical_score: Teknik yetkinlik skoru (0-100)
        pedagogical_score: Pedagojik yetkinlik skoru (0-100)

    Returns:
        Dict: Tamamlayıcı (daha üst seviye) persona
    """
    # Dominant score'u bul
    dominant_score = max(technical_score, pedagogical_score)
    domain = "pedagogical" if pedagogical_score > technical_score else "technical"

    # +20-30 puan ekleyerek üst seviye seç
    boosted_score = min(100, dominant_score + 25)

    pool = ACTIVE_PERSONAS[domain]

    # Boosted score'a uygun persona'ları bul
    suitable_personas = []
    for persona in pool:
        tech_min, tech_max = persona["technical_score_range"]
        ped_min, ped_max = persona["pedagogical_score_range"]

        if tech_min <= boosted_score <= tech_max or ped_min <= boosted_score <= ped_max:
            suitable_personas.append(persona)

    # Eğer bulunamazsa, en üst seviye persona'yı seç
    if not suitable_personas:
        suitable_personas = [pool[-1]]  # Expert

    return random.choice(suitable_personas)


def get_all_personas() -> Dict[str, List[Dict]]:
    """
    Tüm persona'ları döndür

    Returns:
        Dict: Tüm persona listesi
    """
    return ACTIVE_PERSONAS


def get_persona_by_id(persona_id: str) -> Dict:
    """
    ID'ye göre persona getir

    Args:
        persona_id: Persona ID (örn: "edu_novice", "tech_expert")

    Returns:
        Dict: Persona bilgileri veya None
    """
    for domain_personas in ACTIVE_PERSONAS.values():
        for persona in domain_personas:
            if persona["id"] == persona_id:
                return persona
    return None
