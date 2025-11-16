"""
PIDL Katılımcı Detay Sayfası
Her katılımcının 6 görevi, kodları, değerlendirmeleri
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import sys
import os

# Working directory'yi düzelt
if os.path.basename(os.getcwd()) == "pages":
    os.chdir("..")
sys.path.insert(0, os.getcwd())

from database.database import DatabaseSession
from database.models import (
    Participant, TaskSession, PrePostTest, GeneratedCode,
    NASATLXResponse, AICodeEvaluation, FinalEvaluation,
    TaskStatus, AIType, TechnicalMetrics, PedagogicalMetrics
)

# Sayfa yapılandırması
st.set_page_config(
    page_title="Katılımcı Detay",
    page_icon="👤",
    layout="wide"
)

st.markdown("""
<style>
    .participant-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .session-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .code-container {
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        overflow-x: auto;
        max-height: 500px;
        overflow-y: auto;
    }
    .metric-box {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 👤 Katılımcı Detay Görünümü")
st.markdown("---")

# Katılımcı listesini yükle
@st.cache_data(ttl=10)
def load_participants():
    with DatabaseSession() as session:
        participants = session.query(Participant).all()
        return [{
            "uuid": p.uuid,
            "display_name": f"{p.uuid} - {p.gender}, {p.age} yaş, {p.competency_level.value}",
            "age": p.age,
            "gender": p.gender,
            "education": p.education,
            "work_field": p.work_field,
            "technical_score": p.technical_score,
            "pedagogical_score": p.pedagogical_score,
            "competency_level": p.competency_level.value,
            "completed": p.completed
        } for p in participants]

participants = load_participants()

if len(participants) == 0:
    st.error("❌ Henüz katılımcı verisi yok!")
    st.stop()

# Katılımcı seçici
st.sidebar.markdown("## 🔍 Katılımcı Seç")

# Filtreler
filter_gender = st.sidebar.multiselect(
    "Cinsiyet",
    options=list(set([p["gender"] for p in participants])),
    default=None
)

filter_level = st.sidebar.multiselect(
    "Dreyfus Seviyesi",
    options=list(set([p["competency_level"] for p in participants])),
    default=None
)

# Filtreleme
filtered_participants = participants
if filter_gender:
    filtered_participants = [p for p in filtered_participants if p["gender"] in filter_gender]
if filter_level:
    filtered_participants = [p for p in filtered_participants if p["competency_level"] in filter_level]

st.sidebar.markdown(f"**{len(filtered_participants)} katılımcı bulundu**")

# Katılımcı seçimi
participant_options = {p["display_name"]: p["uuid"] for p in filtered_participants}
selected_display = st.sidebar.selectbox(
    "Katılımcı:",
    options=list(participant_options.keys()),
    index=0
)

selected_uuid = participant_options[selected_display]

# Seçilen katılımcının tam verilerini yükle
@st.cache_data(ttl=10)
def load_participant_full_data(uuid):
    with DatabaseSession() as session:
        # Participant
        participant = session.query(Participant).filter_by(uuid=uuid).first()

        # Task sessions
        task_sessions = session.query(TaskSession).filter_by(participant_uuid=uuid).all()

        # Her session için detayları al
        sessions_data = []
        for ts in task_sessions:
            # Pre/Post tests
            pre_test = session.query(PrePostTest).filter_by(
                task_session_id=ts.id,
                test_type="PRE"
            ).first()
            post_test = session.query(PrePostTest).filter_by(
                task_session_id=ts.id,
                test_type="POST"
            ).first()

            # Generated code
            code = session.query(GeneratedCode).filter_by(task_session_id=ts.id).first()

            # NASA-TLX
            nasa = session.query(NASATLXResponse).filter_by(task_session_id=ts.id).first()

            # AI Evaluation
            ai_eval = session.query(AICodeEvaluation).filter_by(task_session_id=ts.id).first()

            # Technical & Pedagogical metrics
            tech_metrics = None
            ped_metrics = None
            if code:
                tech_metrics = session.query(TechnicalMetrics).filter_by(generated_code_id=code.id).first()
                ped_metrics = session.query(PedagogicalMetrics).filter_by(generated_code_id=code.id).first()

            sessions_data.append({
                "task_session": ts,
                "pre_test": pre_test,
                "post_test": post_test,
                "code": code,
                "nasa_tlx": nasa,
                "ai_eval": ai_eval,
                "tech_metrics": tech_metrics,
                "ped_metrics": ped_metrics
            })

        # Final evaluation
        final_eval = session.query(FinalEvaluation).filter_by(participant_uuid=uuid).first()

        return {
            "participant": participant,
            "sessions": sessions_data,
            "final_eval": final_eval
        }

data = load_participant_full_data(selected_uuid)

# 1. KATILIMCI BİLGİLERİ
st.markdown(f"""
<div class="participant-card">
    <h2>👤 {data['participant'].uuid}</h2>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
        <div>
            <strong>Yaş:</strong> {data['participant'].age}<br>
            <strong>Cinsiyet:</strong> {data['participant'].gender}<br>
            <strong>Eğitim:</strong> {data['participant'].education}
        </div>
        <div>
            <strong>Çalışma Alanı:</strong> {data['participant'].work_field}<br>
            <strong>Teknik Skor:</strong> {data['participant'].technical_score}/100<br>
            <strong>Pedagojik Skor:</strong> {data['participant'].pedagogical_score}/100
        </div>
        <div>
            <strong>Dreyfus Seviyesi:</strong> {data['participant'].competency_level.value}<br>
            <strong>Tamamlandı mı:</strong> {'✅ Evet' if data['participant'].completed else '❌ Hayır'}<br>
            <strong>Toplam Süre:</strong> {data['participant'].total_duration_minutes or 0} dk
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. ÖZET İSTATİSTİKLER
st.markdown("## 📊 Özet İstatistikler")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_tasks = len(data["sessions"])
    st.metric("Toplam Görev", total_tasks)

with col2:
    similar_count = sum(1 for s in data["sessions"]
                       if s["task_session"].assigned_ai_type == AIType.SIMILAR)
    st.metric("Similar Mod", similar_count)

with col3:
    comp_count = sum(1 for s in data["sessions"]
                    if s["task_session"].assigned_ai_type == AIType.COMPLEMENTARY)
    st.metric("Complementary Mod", comp_count)

with col4:
    if data["sessions"]:
        avg_duration = sum(s["task_session"].duration_minutes or 0 for s in data["sessions"]) / len(data["sessions"])
        st.metric("Ort. Süre", f"{avg_duration:.1f} dk")
    else:
        st.metric("Ort. Süre", "N/A")

with col5:
    # Learning gain
    learning_gains = []
    for s in data["sessions"]:
        if s["pre_test"] and s["post_test"]:
            gain = s["post_test"].score - s["pre_test"].score
            learning_gains.append(gain)

    if learning_gains:
        avg_gain = sum(learning_gains) / len(learning_gains)
        st.metric("Ort. Learning Gain", f"+{avg_gain:.1f}")
    else:
        st.metric("Ort. Learning Gain", "N/A")

st.markdown("---")

# 3. GÖREV DETAYLARI
st.markdown("## 📝 Görev Detayları")

for idx, session_data in enumerate(data["sessions"], 1):
    ts = session_data["task_session"]

    # AI type display
    ai_mode_display = "Similar" if ts.assigned_ai_type == AIType.SIMILAR else "Complementary"
    status_display = "Tamamlandı" if ts.status == TaskStatus.COMPLETED else "Devam Ediyor"

    with st.expander(f"🎯 Görev {ts.task_number} - {ai_mode_display} Mod - {ts.assigned_persona}", expanded=(idx == 1)):

        # Görev başlığı
        st.markdown(f"""
        <div class="session-card">
            <h3>Görev {ts.task_number}</h3>
            <strong>AI Modu:</strong> {ai_mode_display}<br>
            <strong>Persona:</strong> {ts.assigned_persona}<br>
            <strong>Durum:</strong> {status_display}<br>
            <strong>Süre:</strong> {ts.duration_minutes} dakika
        </div>
        """, unsafe_allow_html=True)

        # Tabs
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📝 Prompt & Kod",
            "📊 Pre/Post Test",
            "🧠 NASA-TLX",
            "⭐ AI Değerlendirme",
            "🔧 Technical Metrics",
            "📚 Pedagogical Metrics"
        ])

        # TAB 1: PROMPT & KOD
        with tab1:
            if session_data["code"]:
                st.markdown("### 💬 Kullanılan Prompt")
                st.info(session_data["code"].prompt_used)

                st.markdown("### 💻 Üretilen Kod")
                st.markdown(f"**Dil:** {session_data['code'].language} | **Üretim Süresi:** {session_data['code'].generation_time_seconds:.1f}s")

                st.markdown(f"""
                <div class="code-container">
{session_data['code'].code_text}
                </div>
                """, unsafe_allow_html=True)

                # Download button
                st.download_button(
                    "📥 Kodu İndir",
                    session_data["code"].code_text,
                    file_name=f"task_{ts.task_number}_code.sol",
                    mime="text/plain"
                )
            else:
                st.warning("Kod verisi bulunamadı.")

        # TAB 2: PRE/POST TEST
        with tab2:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📝 Pre-Test")
                if session_data["pre_test"]:
                    pt = session_data["pre_test"]
                    st.markdown(f"**Toplam Skor:** {pt.score}/25")
                    for i in range(1, 6):
                        answer = getattr(pt, f"q{i}_answer")
                        st.write(f"Soru {i}: {answer}/5")
                else:
                    st.warning("Pre-test verisi yok")

            with col2:
                st.markdown("### 📝 Post-Test")
                if session_data["post_test"]:
                    pt = session_data["post_test"]
                    st.markdown(f"**Toplam Skor:** {pt.score}/25")
                    for i in range(1, 6):
                        answer = getattr(pt, f"q{i}_answer")
                        st.write(f"Soru {i}: {answer}/5")

                    # Learning gain
                    if session_data["pre_test"]:
                        gain = pt.score - session_data["pre_test"].score
                        st.success(f"**Learning Gain:** +{gain} puan")
                else:
                    st.warning("Post-test verisi yok")

        # TAB 3: NASA-TLX
        with tab3:
            if session_data["nasa_tlx"]:
                nasa = session_data["nasa_tlx"]

                st.markdown("### 🧠 Bilişsel Yük (NASA-TLX)")

                # Radar chart
                categories = ['Mental Demand', 'Physical Demand', 'Temporal Demand',
                            'Performance', 'Effort', 'Frustration']
                values = [
                    nasa.mental_demand,
                    nasa.physical_demand,
                    nasa.temporal_demand,
                    10 - nasa.performance,  # Inverse
                    nasa.effort,
                    nasa.frustration
                ]

                fig = go.Figure(data=go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself'
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                    showlegend=False,
                    title="NASA-TLX Dimensions"
                )
                st.plotly_chart(fig, use_container_width=True)

                st.metric("Toplam Bilişsel Yük", f"{nasa.total_cognitive_load}/60")
            else:
                st.warning("NASA-TLX verisi yok")

        # TAB 4: AI DEĞERLENDIRME
        with tab4:
            if session_data["ai_eval"]:
                ai = session_data["ai_eval"]

                st.markdown("### ⭐ AI Kod Değerlendirmesi")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Code Understandability", f"{ai.code_understandability}/10")
                    st.metric("Explanation Quality", f"{ai.explanation_quality}/10")

                with col2:
                    st.metric("Educational Value", f"{ai.educational_value}/10")
                    st.metric("Perceived Quality", f"{ai.perceived_code_quality}/10")

                with col3:
                    st.metric("Perceived Security", f"{ai.perceived_security}/10")
                    avg = (ai.code_understandability + ai.explanation_quality +
                          ai.educational_value + ai.perceived_code_quality +
                          ai.perceived_security) / 5
                    st.metric("Ortalama", f"{avg:.1f}/10")

                if ai.best_aspect:
                    st.success(f"**En iyi yönü:** {ai.best_aspect}")
                if ai.improvement_needed:
                    st.warning(f"**Geliştirilebilir:** {ai.improvement_needed}")
            else:
                st.warning("AI değerlendirme verisi yok")

        # TAB 5: TECHNICAL METRICS
        with tab5:
            if session_data["tech_metrics"]:
                tech = session_data["tech_metrics"]

                st.markdown("### 🔧 Technical Metrics (Yazılımcı Bakışı)")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Manuel Değerlendirme (1-10)**")
                    st.metric("Security", f"{tech.security_score}/10")
                    st.metric("Gas Optimization", f"{tech.gas_optimization_score}/10")
                    st.metric("Code Quality", f"{tech.code_quality_score}/10")
                    st.metric("Maintainability", f"{tech.maintainability_score}/10")
                    st.metric("Production Readiness", f"{tech.production_readiness}/10")

                with col2:
                    st.markdown("**Otomatik Analiz (0-100)**")
                    if tech.auto_security_score:
                        st.metric("Auto Security", f"{tech.auto_security_score:.1f}/100")
                    if tech.auto_gas_score:
                        st.metric("Auto Gas", f"{tech.auto_gas_score:.1f}/100")
                    if tech.auto_complexity_score:
                        st.metric("Auto Complexity", f"{tech.auto_complexity_score:.1f}/100")
            else:
                st.warning("Technical metrics verisi yok")

        # TAB 6: PEDAGOGICAL METRICS
        with tab6:
            if session_data["ped_metrics"]:
                ped = session_data["ped_metrics"]

                st.markdown("### 📚 Pedagogical Metrics (Eğitimci Bakışı)")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Learning Ease", f"{ped.learning_ease_score}/10")
                    st.metric("Instructiveness", f"{ped.instructiveness_score}/10")
                    st.metric("Cognitive Load", f"{ped.cognitive_load_score}/10",
                            help="Düşük=iyi")
                    st.metric("Example Quality", f"{ped.example_quality_score}/10")

                with col2:
                    st.metric("Scaffolding", f"{ped.scaffolding_score}/10")
                    if ped.explanation_quality:
                        st.metric("Explanation Quality", f"{ped.explanation_quality}/10")
                    if ped.bloom_taxonomy_level:
                        st.info(f"**Bloom Taxonomy:** {ped.bloom_taxonomy_level}")
            else:
                st.warning("Pedagogical metrics verisi yok")

st.markdown("---")

# 4. FINAL EVALUATION
if data["final_eval"]:
    st.markdown("## 🎓 Final Değerlendirme")

    final = data["final_eval"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🤖 AI Tercihleri")
        st.write(f"**Tercih Edilen AI:** {final.preferred_ai}")
        st.write(f"**Sebep:** {final.preferred_ai_reason}")
        st.write(f"**Öğrenme için Daha İyi:** {final.learning_better_ai}")
        st.write(f"**Hız için Daha İyi:** {final.speed_better_ai}")

    with col2:
        st.markdown("### ⭐ Genel Değerlendirme")
        st.metric("AI Learning Rating", f"{final.ai_learning_rating}/10")
        st.write(f"**Tavsiye Eder mi:** {final.would_recommend}")
        st.write(f"**En Zor Görev:** {final.hardest_task}")

    if final.suggestions:
        st.info(f"**Öneriler:** {final.suggestions}")

st.markdown("---")
st.caption("💡 **İpucu:** Farklı katılımcıları karşılaştırmak için sol menüden başka bir katılımcı seçin.")
