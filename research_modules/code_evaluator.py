"""
Automatic Code Evaluator - Otomatik kod değerlendirme sistemi
Security, Gas Optimization, Code Complexity analizi
"""

import re
from typing import Dict, Optional
import hashlib


class CodeEvaluator:
    """Otomatik kod değerlendirme sınıfı"""

    @staticmethod
    def evaluate_smart_contract(code: str, language: str = "solidity") -> Dict[str, float]:
        """
        Smart contract kodunu otomatik değerlendir

        Args:
            code: Değerlendirilecek kod
            language: Programlama dili (default: solidity)

        Returns:
            Dict: Değerlendirme skorları (0-100)
        """
        if not code or not code.strip():
            return {
                "security_score": 0.0,
                "gas_score": 0.0,
                "complexity_score": 0.0,
                "overall_score": 0.0
            }

        # Her metrik için değerlendirme yap
        security_score = CodeEvaluator._evaluate_security(code)
        gas_score = CodeEvaluator._evaluate_gas_optimization(code)
        complexity_score = CodeEvaluator._evaluate_complexity(code)

        # Genel skor hesapla
        overall_score = (security_score * 0.4 + gas_score * 0.3 + complexity_score * 0.3)

        return {
            "security_score": round(security_score, 2),
            "gas_score": round(gas_score, 2),
            "complexity_score": round(complexity_score, 2),
            "overall_score": round(overall_score, 2)
        }

    @staticmethod
    def _evaluate_security(code: str) -> float:
        """
        Güvenlik skorunu hesapla (0-100)
        Basit pattern matching ile güvenlik kontrolü
        """
        score = 50.0  # Base score

        # Pozitif güvenlik paternleri (her biri +10 puan)
        positive_patterns = [
            (r'\brequire\s*\(', "require kontrolü kullanılmış", 10),
            (r'\bassert\s*\(', "assert kontrolü kullanılmış", 8),
            (r'\brevert\s*\(', "revert kullanılmış", 8),
            (r'\bmodifier\s+\w+', "modifier kullanılmış", 12),
            (r'\bnonReentrant\b', "reentrancy koruması var", 15),
            (r'\bprivate\b|\binternal\b', "visibility belirtilmiş", 7),
        ]

        for pattern, description, points in positive_patterns:
            if re.search(pattern, code):
                score += points

        # Negatif güvenlik paternleri (her biri -15 puan)
        negative_patterns = [
            (r'\btx\.origin\b', "tx.origin kullanılmış (tehlikeli)", -15),
            (r'\.call\s*\{', "low-level call kullanılmış", -10),
            (r'\.delegatecall\s*\(', "delegatecall kullanılmış (riskli)", -15),
            (r'\.send\s*\(', "send kullanılmış (deprecated)", -12),
            (r'\bselfdestruct\s*\(', "selfdestruct kullanılmış", -10),
        ]

        for pattern, description, points in negative_patterns:
            if re.search(pattern, code):
                score += points

        # 0-100 aralığında sınırla
        return max(0.0, min(100.0, score))

    @staticmethod
    def _evaluate_gas_optimization(code: str) -> float:
        """
        Gas optimizasyon skorunu hesapla (0-100)
        """
        score = 50.0  # Base score

        # Pozitif gas optimizasyon paternleri
        positive_patterns = [
            (r'\bconstant\b', "constant kullanılmış", 10),
            (r'\bimmutable\b', "immutable kullanılmış", 10),
            (r'\bunchecked\s*\{', "unchecked block kullanılmış", 8),
            (r'\bmemory\b', "memory kullanılmış (storage yerine)", 7),
            (r'\bcalldata\b', "calldata kullanılmış", 12),
            (r'\bview\b|\bpure\b', "view/pure function var", 8),
        ]

        for pattern, description, points in positive_patterns:
            matches = len(re.findall(pattern, code))
            score += min(points * matches, points * 2)  # Max 2x puan

        # Negatif gas optimizasyon paternleri
        negative_patterns = [
            (r'\bstorage\b.*=', "fazla storage kullanımı", -5),
            (r'\bfor\s*\(.*\blength\b', "loop'ta .length kullanımı", -8),
            (r'string\s+memory', "string memory (pahalı)", -6),
        ]

        for pattern, description, points in negative_patterns:
            matches = len(re.findall(pattern, code))
            score += points * matches

        return max(0.0, min(100.0, score))

    @staticmethod
    def _evaluate_complexity(code: str) -> float:
        """
        Kod karmaşıklık skorunu hesapla (0-100)
        Düşük complexity = Yüksek skor
        """
        # McCabe Cyclomatic Complexity yaklaşımı
        decision_points = 0

        # Karar noktalarını say
        patterns = [
            r'\bif\s*\(',
            r'\belse\s+if\b',
            r'\bwhile\s*\(',
            r'\bfor\s*\(',
            r'\brequire\s*\(',
            r'\bassert\s*\(',
            r'\?.*:',  # Ternary operator
        ]

        for pattern in patterns:
            decision_points += len(re.findall(pattern, code))

        # Fonksiyon sayısı
        function_count = len(re.findall(r'\bfunction\s+\w+', code))

        # Satır sayısı (boş ve yorum hariç)
        code_lines = [line for line in code.split('\n')
                      if line.strip() and not line.strip().startswith('//')]
        line_count = len(code_lines)

        # Complexity hesapla
        cyclomatic_complexity = decision_points + 1

        # Skor hesaplama (düşük complexity = yüksek skor)
        if cyclomatic_complexity <= 5:
            complexity_score = 100
        elif cyclomatic_complexity <= 10:
            complexity_score = 80
        elif cyclomatic_complexity <= 20:
            complexity_score = 60
        elif cyclomatic_complexity <= 30:
            complexity_score = 40
        else:
            complexity_score = 20

        # Line count bazlı ayarlama
        if line_count > 300:
            complexity_score -= 10
        elif line_count < 50:
            complexity_score += 10

        return max(0.0, min(100.0, complexity_score))

    @staticmethod
    def calculate_code_hash(code: str) -> str:
        """Kod için benzersiz hash oluştur"""
        return hashlib.sha256(code.encode()).hexdigest()

    @staticmethod
    def get_code_stats(code: str) -> Dict[str, int]:
        """
        Kod istatistiklerini çıkar

        Returns:
            Dict: total_lines, code_lines, comment_lines, blank_lines, function_count
        """
        lines = code.split('\n')
        total_lines = len(lines)

        code_lines = 0
        comment_lines = 0
        blank_lines = 0

        for line in lines:
            stripped = line.strip()
            if not stripped:
                blank_lines += 1
            elif stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*'):
                comment_lines += 1
            else:
                code_lines += 1

        # Fonksiyon sayısı
        function_count = len(re.findall(r'\bfunction\s+\w+', code))

        # Modifier sayısı
        modifier_count = len(re.findall(r'\bmodifier\s+\w+', code))

        # Event sayısı
        event_count = len(re.findall(r'\bevent\s+\w+', code))

        return {
            "total_lines": total_lines,
            "code_lines": code_lines,
            "comment_lines": comment_lines,
            "blank_lines": blank_lines,
            "function_count": function_count,
            "modifier_count": modifier_count,
            "event_count": event_count,
            "comment_ratio": round(comment_lines / total_lines * 100, 2) if total_lines > 0 else 0
        }


# Utility functions
def evaluate_code_batch(codes: list[str]) -> list[Dict]:
    """
    Birden fazla kodu toplu değerlendir

    Args:
        codes: Kod listesi

    Returns:
        List[Dict]: Her kod için değerlendirme sonuçları
    """
    evaluator = CodeEvaluator()
    results = []

    for i, code in enumerate(codes):
        result = evaluator.evaluate_smart_contract(code)
        result["code_index"] = i
        results.append(result)

    return results


def compare_codes(code1: str, code2: str) -> Dict:
    """
    İki kodu karşılaştır

    Returns:
        Dict: Karşılaştırma sonuçları
    """
    eval1 = CodeEvaluator.evaluate_smart_contract(code1)
    eval2 = CodeEvaluator.evaluate_smart_contract(code2)

    return {
        "code1_scores": eval1,
        "code2_scores": eval2,
        "security_diff": eval1["security_score"] - eval2["security_score"],
        "gas_diff": eval1["gas_score"] - eval2["gas_score"],
        "complexity_diff": eval1["complexity_score"] - eval2["complexity_score"],
        "overall_diff": eval1["overall_score"] - eval2["overall_score"],
        "winner": "Code 1" if eval1["overall_score"] > eval2["overall_score"] else
                  "Code 2" if eval2["overall_score"] > eval1["overall_score"] else "Tie"
    }
