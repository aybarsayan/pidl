"""
Synthetic Data Importer - Sentetik veriyi database'e import et
"""

import sys
sys.path.insert(0, '.')

import pandas as pd
from database.database import DatabaseSession
from database.models import (
    Participant, TaskSession, PrePostTest, GeneratedCode,
    NASATLXResponse, AICodeEvaluation, FinalEvaluation, TaskComparison,
    TechnicalMetrics, PedagogicalMetrics,
    CompetencyLevel, AIType, TaskStatus, TestType
)
from datetime import datetime

def import_participants(csv_path: str):
    """Katılımcıları import et"""
    print("\n📥 Katılımcılar import ediliyor...")

    df = pd.read_csv(csv_path)

    # Competency level mapping
    level_map = {
        "Novice": CompetencyLevel.NOVICE,
        "Advanced Beginner": CompetencyLevel.ADVANCED_BEGINNER,
        "Competent": CompetencyLevel.COMPETENT,
        "Proficient": CompetencyLevel.PROFICIENT,
        "Expert": CompetencyLevel.EXPERT
    }

    with DatabaseSession() as session:
        for _, row in df.iterrows():
            participant = Participant(
                uuid=row['uuid'],
                age=int(row['age']),
                gender=row['gender'],
                education=row['education'],
                work_field=row['work_field'],
                technical_score=int(row['technical_score']),
                pedagogical_score=int(row['pedagogical_score']),
                competency_level=level_map.get(row['competency_level'], CompetencyLevel.NOVICE),
                consent_given=bool(row['consent_given']),
                completed=bool(row['completed']),
                total_duration_minutes=int(row['total_duration_minutes']) if pd.notna(row['total_duration_minutes']) else None,
                created_at=datetime.fromisoformat(row['created_at'])
            )
            session.add(participant)

        session.commit()

    print(f"   ✅ {len(df)} katılımcı eklendi")


def import_task_sessions(csv_path: str):
    """Task session'ları import et"""
    print("\n📥 Task session'lar import ediliyor...")

    df = pd.read_csv(csv_path)

    ai_type_map = {
        "Similar": AIType.SIMILAR,
        "Complementary": AIType.COMPLEMENTARY
    }

    status_map = {
        "Started": TaskStatus.STARTED,
        "Completed": TaskStatus.COMPLETED
    }

    with DatabaseSession() as session:
        for _, row in df.iterrows():
            task_session = TaskSession(
                participant_uuid=row['participant_uuid'],
                task_number=int(row['task_number']),
                assigned_ai_type=ai_type_map.get(row['assigned_ai_type'], AIType.SIMILAR),
                assigned_persona=row['assigned_persona'],
                status=status_map.get(row['status'], TaskStatus.COMPLETED),
                duration_minutes=int(row['duration_minutes']) if pd.notna(row['duration_minutes']) else None,
                started_at=datetime.fromisoformat(row['started_at']),
                completed_at=datetime.fromisoformat(row['completed_at']) if pd.notna(row['completed_at']) else None
            )
            session.add(task_session)

        session.commit()

    print(f"   ✅ {len(df)} task session eklendi")


def import_pre_post_tests(csv_path: str):
    """Pre/Post testleri import et"""
    print("\n📥 Pre/Post testler import ediliyor...")

    df = pd.read_csv(csv_path)

    test_type_map = {
        "pre": TestType.PRE,
        "post": TestType.POST
    }

    with DatabaseSession() as session:
        # Session ID mapping'i al
        sessions_query = session.query(TaskSession).all()
        session_id_map = {i+1: s.id for i, s in enumerate(sessions_query)}

        for _, row in df.iterrows():
            task_session_id = session_id_map.get(int(row['session_id']))
            if not task_session_id:
                continue

            pre_post_test = PrePostTest(
                task_session_id=task_session_id,
                test_type=test_type_map.get(row['test_type'], TestType.PRE),
                q1_answer=row['q1'],
                q2_answer=row['q2'],
                q3_answer=row['q3'],
                q4_answer=row['q4'],
                q5_answer=row['q5'],
                score=int(row['score'])
            )
            session.add(pre_post_test)

        session.commit()

    print(f"   ✅ {len(df)} pre/post test eklendi")


def import_generated_codes(csv_path: str):
    """Üretilen kodları import et"""
    print("\n📥 Üretilen kodlar import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        # Session ID mapping
        sessions_query = session.query(TaskSession).all()
        session_id_map = {i+1: s.id for i, s in enumerate(sessions_query)}

        for _, row in df.iterrows():
            task_session_id = session_id_map.get(int(row['session_id']))
            if not task_session_id:
                continue

            generated_code = GeneratedCode(
                task_session_id=task_session_id,
                code_text=row['code_text'],
                language=row['language'],
                prompt_used=row['prompt_used'],
                ai_persona=row['ai_persona'],
                generation_time_seconds=float(row['generation_time_seconds'])
            )
            session.add(generated_code)

        session.commit()

    print(f"   ✅ {len(df)} kod eklendi")


def import_nasa_tlx(csv_path: str):
    """NASA-TLX yanıtlarını import et"""
    print("\n📥 NASA-TLX yanıtları import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        sessions_query = session.query(TaskSession).all()
        session_id_map = {i+1: s.id for i, s in enumerate(sessions_query)}

        for _, row in df.iterrows():
            task_session_id = session_id_map.get(int(row['session_id']))
            if not task_session_id:
                continue

            nasa_tlx = NASATLXResponse(
                task_session_id=task_session_id,
                mental_demand=int(row['mental_demand']),
                physical_demand=int(row['physical_demand']),
                temporal_demand=int(row['temporal_demand']),
                performance=int(row['performance']),
                effort=int(row['effort']),
                frustration=int(row['frustration']),
                total_cognitive_load=int(row['total_cognitive_load'])
            )
            session.add(nasa_tlx)

        session.commit()

    print(f"   ✅ {len(df)} NASA-TLX yanıtı eklendi")


def import_ai_evaluations(csv_path: str):
    """AI değerlendirmelerini import et"""
    print("\n📥 AI değerlendirmeleri import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        sessions_query = session.query(TaskSession).all()
        session_id_map = {i+1: s.id for i, s in enumerate(sessions_query)}

        for _, row in df.iterrows():
            task_session_id = session_id_map.get(int(row['session_id']))
            if not task_session_id:
                continue

            ai_eval = AICodeEvaluation(
                task_session_id=task_session_id,
                code_understandability=int(row['code_understandability']),
                explanation_quality=int(row['explanation_quality']),
                educational_value=int(row['educational_value']),
                perceived_code_quality=int(row['perceived_code_quality']),
                perceived_security=int(row['perceived_security']),
                best_aspect=row['best_aspect'],
                improvement_needed=row['improvement_needed']
            )
            session.add(ai_eval)

        session.commit()

    print(f"   ✅ {len(df)} AI değerlendirmesi eklendi")


def import_technical_metrics(csv_path: str):
    """Technical metrics import et"""
    print("\n📥 Technical metrics import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        codes_query = session.query(GeneratedCode).all()
        code_id_map = {i+1: c.id for i, c in enumerate(codes_query)}

        for _, row in df.iterrows():
            generated_code_id = code_id_map.get(int(row['code_id']))
            if not generated_code_id:
                continue

            tech_metric = TechnicalMetrics(
                generated_code_id=generated_code_id,
                security_score=int(row['security_score']),
                gas_optimization_score=int(row['gas_optimization_score']),
                code_quality_score=int(row['code_quality_score']),
                maintainability_score=int(row['maintainability_score']),
                production_readiness=int(row['production_readiness']),
                auto_security_score=float(row['auto_security_score']) if pd.notna(row['auto_security_score']) else None,
                auto_gas_score=float(row['auto_gas_score']) if pd.notna(row['auto_gas_score']) else None,
                auto_complexity_score=float(row['auto_complexity_score']) if pd.notna(row['auto_complexity_score']) else None
            )
            session.add(tech_metric)

        session.commit()

    print(f"   ✅ {len(df)} technical metric eklendi")


def import_pedagogical_metrics(csv_path: str):
    """Pedagogical metrics import et"""
    print("\n📥 Pedagogical metrics import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        codes_query = session.query(GeneratedCode).all()
        code_id_map = {i+1: c.id for i, c in enumerate(codes_query)}

        for _, row in df.iterrows():
            generated_code_id = code_id_map.get(int(row['code_id']))
            if not generated_code_id:
                continue

            ped_metric = PedagogicalMetrics(
                generated_code_id=generated_code_id,
                learning_ease_score=int(row['learning_ease_score']),
                instructiveness_score=int(row['instructiveness_score']),
                cognitive_load_score=int(row['cognitive_load_score']),
                example_quality_score=int(row['example_quality_score']),
                scaffolding_score=int(row['scaffolding_score']),
                bloom_taxonomy_level=row['bloom_taxonomy_level'] if pd.notna(row['bloom_taxonomy_level']) else None,
                explanation_quality=int(row['explanation_quality']) if pd.notna(row['explanation_quality']) else None
            )
            session.add(ped_metric)

        session.commit()

    print(f"   ✅ {len(df)} pedagogical metric eklendi")


def import_task_comparisons(csv_path: str):
    """Task comparisons import et"""
    print("\n📥 Task comparisons import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        sessions_query = session.query(TaskSession).all()
        session_id_map = {i+1: s.id for i, s in enumerate(sessions_query)}

        for _, row in df.iterrows():
            task_session_id = session_id_map.get(int(row['session_id']))
            if not task_session_id:
                continue

            task_comp = TaskComparison(
                task_session_id=task_session_id,
                used_ai_type=row['used_ai_type'],
                other_ai_type=row['other_ai_type'],
                suitability_choice=row['suitability_choice'] if pd.notna(row['suitability_choice']) else None,
                reason=row['reason'],
                difficulty_rating=row['difficulty_rating'],
                has_comparison=bool(row['has_comparison'])
            )
            session.add(task_comp)

        session.commit()

    print(f"   ✅ {len(df)} task comparison eklendi")


def import_final_evaluations(csv_path: str):
    """Final evaluations import et"""
    print("\n📥 Final evaluations import ediliyor...")

    df = pd.read_csv(csv_path)

    with DatabaseSession() as session:
        for _, row in df.iterrows():
            final_eval = FinalEvaluation(
                participant_uuid=row['participant_uuid'],
                preferred_ai=row['preferred_ai'],
                preferred_ai_reason=row['preferred_ai_reason'],
                learning_better_ai=row['learning_better_ai'],
                speed_better_ai=row['speed_better_ai'],
                comfort_similar=int(row['comfort_similar']),
                development_complementary=int(row['development_complementary']),
                clarity_similar=int(row['clarity_similar']),
                quality_complementary=int(row['quality_complementary']),
                hybrid_ideal=int(row['hybrid_ideal']),
                blockchain_view_change=row['blockchain_view_change'],
                ai_learning_rating=int(row['ai_learning_rating']),
                would_recommend=row['would_recommend'],
                hardest_task=row['hardest_task'],
                ai_potential=row['ai_potential'],
                suggestions=row['suggestions'],
                blockchain_education_view=row['blockchain_education_view']
            )
            session.add(final_eval)

        session.commit()

    print(f"   ✅ {len(df)} final evaluation eklendi")


def main():
    """Ana import fonksiyonu"""

    print("\n" + "="*80)
    print("📦 SENTETİK VERİ DATABASE IMPORT")
    print("="*80)

    data_dir = "synthetic_data_N150"

    try:
        # Sıralama önemli (foreign key constraints)
        import_participants(f"{data_dir}/participants.csv")
        import_task_sessions(f"{data_dir}/task_sessions.csv")
        import_pre_post_tests(f"{data_dir}/pre_post_tests.csv")
        import_generated_codes(f"{data_dir}/generated_codes.csv")
        import_nasa_tlx(f"{data_dir}/nasa_tlx_responses.csv")
        import_ai_evaluations(f"{data_dir}/ai_code_evaluations.csv")
        import_technical_metrics(f"{data_dir}/technical_metrics.csv")
        import_pedagogical_metrics(f"{data_dir}/pedagogical_metrics.csv")
        import_task_comparisons(f"{data_dir}/task_comparisons.csv")
        import_final_evaluations(f"{data_dir}/final_evaluations.csv")

        print("\n" + "="*80)
        print("✅ TÜM VERİ BAŞARIYLA İMPORT EDİLDİ!")
        print("="*80)

        # Özet
        with DatabaseSession() as session:
            participant_count = session.query(Participant).count()
            session_count = session.query(TaskSession).count()
            code_count = session.query(GeneratedCode).count()

            print(f"\n📊 Database Özeti:")
            print(f"   Katılımcı: {participant_count}")
            print(f"   Task Session: {session_count}")
            print(f"   Üretilen Kod: {code_count}")
            print(f"\n🌐 Yönetim panelini açın: http://localhost:8501")
            print(f"   veya: http://localhost:8502\n")

    except Exception as e:
        print(f"\n❌ HATA: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
