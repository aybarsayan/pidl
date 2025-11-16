"""
Technical Evaluation Form - Yazılımcılar için kod değerlendirme formu
Teknik metrikler: Security, Gas Optimization, Code Quality, Maintainability
"""

import streamlit as st
from typing import Dict


class TechnicalEvaluationForm:
    """Yazılımcılar için teknik kod değerlendirme formu"""

    @staticmethod
    def show() -> Dict[str, int]:
        """
        Teknik değerlendirme formunu göster

        Returns:
            Dict[str, int]: Değerlendirme skorları
        """
        st.markdown("### 🔧 Technical Evaluation (Yazılımcılar için)")
        st.info("👨‍💻 Lütfen üretilen kodu **teknik açıdan** değerlendirin (1=Çok Kötü, 10=Mükemmel)")

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🔒 Security (Güvenlik)")
                security_score = st.slider(
                    "Güvenlik açıkları, reentrancy, overflow koruması",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="tech_security",
                    help="Kodda güvenlik açığı var mı? Require/assert kullanılmış mı?"
                )

                st.markdown("#### ⚡ Gas Optimization")
                gas_optimization_score = st.slider(
                    "Gas efficiency, storage kullanımı, optimize edilmiş işlemler",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="tech_gas",
                    help="Kod gas-efficient mi? Gereksiz storage kullanımı var mı?"
                )

                st.markdown("#### ✨ Code Quality")
                code_quality_score = st.slider(
                    "Clean code, best practices, naming conventions",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="tech_quality",
                    help="Kod okunabilir mi? Best practices uygulanmış mı?"
                )

            with col2:
                st.markdown("#### 🛠️ Maintainability")
                maintainability_score = st.slider(
                    "Bakım kolaylığı, modülerlik, okunabilirlik",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="tech_maintain",
                    help="Kod kolayca güncellenebilir mi? Modüler yapıda mı?"
                )

                st.markdown("#### 🚀 Production Readiness")
                production_readiness = st.slider(
                    "Production ortamına deploy edilebilirlik",
                    min_value=1,
                    max_value=10,
                    value=5,
                    key="tech_production",
                    help="Kod production'a hazır mı? Test edilebilir mi?"
                )

        # Ortalama skor hesapla
        avg_score = (security_score + gas_optimization_score + code_quality_score +
                     maintainability_score + production_readiness) / 5

        st.markdown("---")
        st.metric("📊 Ortalama Teknik Skor", f"{avg_score:.1f}/10")

        return {
            "security_score": security_score,
            "gas_optimization_score": gas_optimization_score,
            "code_quality_score": code_quality_score,
            "maintainability_score": maintainability_score,
            "production_readiness": production_readiness
        }

    @staticmethod
    def show_with_comments() -> Dict[str, any]:
        """
        Açıklama alanları ile birlikte teknik değerlendirme formu

        Returns:
            Dict: Skorlar ve yorumlar
        """
        scores = TechnicalEvaluationForm.show()

        st.markdown("---")
        st.markdown("### 💬 Technical Comments (İsteğe bağlı)")

        col1, col2 = st.columns(2)

        with col1:
            best_technical_aspect = st.text_area(
                "En iyi teknik yönü neydi?",
                placeholder="Örn: Gas optimizasyonu çok iyi, require kontrolü yapılmış...",
                key="tech_best"
            )

        with col2:
            improvement_needed = st.text_area(
                "Teknik olarak neyi geliştirmeli?",
                placeholder="Örn: Modifier eklenebilir, event kullanılmalı...",
                key="tech_improve"
            )

        scores["best_technical_aspect"] = best_technical_aspect
        scores["improvement_needed"] = improvement_needed

        return scores
