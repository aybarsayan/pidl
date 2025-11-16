"""
Pedagogical Evaluation Form - Eğitimciler için kod değerlendirme formu
Pedagojik metrikler: Learning Ease, Instructiveness, Cognitive Load, Example Quality
"""

import streamlit as st
from typing import Dict


class PedagogicalEvaluationForm:
    """Eğitimciler için pedagojik kod değerlendirme formu"""

    @staticmethod
    def show() -> Dict[str, int]:
        """
        Pedagojik değerlendirme formunu göster

        Returns:
            Dict[str, int]: Değerlendirme skorları
        """
        st.markdown("### 📚 Pedagogical Evaluation (Eğitimciler için)")
        st.info("👩‍🏫 Lütfen üretilen kodu **pedagojik açıdan** değerlendirin (1=Çok Kötü, 10=Mükemmel)")

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🎓 Learning Ease (Öğrenme Kolaylığı)")
                learning_ease_score = st.slider(
                    "Bu koddan öğrenmek ne kadar kolay?",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="ped_learning",
                    help="Kod öğrenci için anlaşılır mı? Adım adım açıklama var mı?"
                )

                st.markdown("#### 📖 Instructiveness (Öğreticilik)")
                instructiveness_score = st.slider(
                    "Kod ne kadar öğretici?",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="ped_instruct",
                    help="Yorum ve açıklamalar yeterli mi? Kavramlar net mi?"
                )

                st.markdown("#### 🧠 Cognitive Load (Bilişsel Yük)")
                cognitive_load_score = st.slider(
                    "Bilişsel yük seviyesi (DÜŞÜK=İYİ)",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="ped_cognitive",
                    help="1=Çok kolay anlaşılır, 10=Çok karmaşık ve yorucu"
                )

            with col2:
                st.markdown("#### 📝 Example Quality (Örnek Kalitesi)")
                example_quality_score = st.slider(
                    "Verilen örnekler ne kadar kaliteli?",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="ped_example",
                    help="Örnekler açıklayıcı mı? Gerçek hayattan mı?"
                )

                st.markdown("#### 🪜 Scaffolding (Kademeli Öğrenme)")
                scaffolding_score = st.slider(
                    "Kademeli öğrenme desteği",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="ped_scaffold",
                    help="Basit başlayıp karmaşığa mı gidiyor? ZPD'ye uygun mu?"
                )

        # Ek pedagojik metrikler
        st.markdown("---")
        st.markdown("#### 🎯 Bloom Taxonomy Level")
        bloom_level = st.selectbox(
            "Bu kod hangi Bloom seviyesine hitap ediyor?",
            [
                "Remember (Hatırlama) - Seviye 1",
                "Understand (Anlama) - Seviye 2",
                "Apply (Uygulama) - Seviye 3",
                "Analyze (Analiz) - Seviye 4",
                "Evaluate (Değerlendirme) - Seviye 5",
                "Create (Yaratma) - Seviye 6"
            ],
            key="ped_bloom"
        )

        st.markdown("#### 💡 Explanation Quality (Açıklama Kalitesi)")
        explanation_quality = st.slider(
            "AI'nın verdiği açıklamaların kalitesi",
            min_value=1,
            max_value=10,
            value=5,
            key="ped_explanation",
            help="Açıklamalar net, anlaşılır ve yeterli mi?"
        )

        # Cognitive load'u tersine çevir (düşük=iyi olmalı, yüksek skor=iyi için)
        inverted_cognitive_load = 11 - cognitive_load_score

        # Ortalama skor hesapla (cognitive load tersine çevrilmiş haliyle)
        avg_score = (learning_ease_score + instructiveness_score + inverted_cognitive_load +
                     example_quality_score + scaffolding_score + explanation_quality) / 6

        st.markdown("---")
        st.metric("📊 Ortalama Pedagojik Skor", f"{avg_score:.1f}/10")

        return {
            "learning_ease_score": learning_ease_score,
            "instructiveness_score": instructiveness_score,
            "cognitive_load_score": cognitive_load_score,  # Orijinal değer (1=kolay, 10=zor)
            "example_quality_score": example_quality_score,
            "scaffolding_score": scaffolding_score,
            "bloom_taxonomy_level": bloom_level,
            "explanation_quality": explanation_quality
        }

    @staticmethod
    def show_with_comments() -> Dict[str, any]:
        """
        Açıklama alanları ile birlikte pedagojik değerlendirme formu

        Returns:
            Dict: Skorlar ve yorumlar
        """
        scores = PedagogicalEvaluationForm.show()

        st.markdown("---")
        st.markdown("### 💬 Pedagogical Comments (İsteğe bağlı)")

        col1, col2 = st.columns(2)

        with col1:
            best_pedagogical_aspect = st.text_area(
                "En iyi pedagojik yönü neydi?",
                placeholder="Örn: Adım adım açıklama çok iyi, örnekler net...",
                key="ped_best"
            )

        with col2:
            improvement_needed = st.text_area(
                "Pedagojik olarak neyi geliştirmeli?",
                placeholder="Örn: Daha fazla örnek eklenebilir, görsel diyagram olabilir...",
                key="ped_improve"
            )

        scores["best_pedagogical_aspect"] = best_pedagogical_aspect
        scores["improvement_needed"] = improvement_needed

        return scores
