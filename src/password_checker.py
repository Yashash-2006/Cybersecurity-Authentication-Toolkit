"""
Module 1: Password Strength Checker
-----------------------------------
Evaluates the security strength of a given password based on length, 
character diversity (uppercase, lowercase, numbers, special symbols), 
Shannon entropy estimation, and common weak pattern detection.
"""

import math
import re
from typing import Dict, Any, List

COMMON_WEAK_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty",
    "password123", "admin", "welcome", "login", "iloveyou",
    "123123", "admin123", "letmein", "monkey", "dragon"
}


def calculate_entropy(password: str) -> float:
    """Calculates Shannon Entropy (bits) based on active character pool size."""
    if not password:
        return 0.0

    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def check_password_strength(password: str) -> Dict[str, Any]:
    """
    Evaluates password strength and returns detailed score, metrics, and recommendations.
    """
    if not isinstance(password, str):
        password = str(password)

    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))

    is_common = password.lower() in COMMON_WEAK_PASSWORDS
    score = 0
    recommendations: List[str] = []

    if is_common:
        score = 5
        strength_label = "Very Weak (Common Weak Password)"
        recommendations.append("AVOID using commonly leaked passwords like 'password', '123456', or 'qwerty'.")
        return {
            "password_length": length,
            "has_uppercase": has_upper,
            "has_lowercase": has_lower,
            "has_digits": has_digit,
            "has_special": has_special,
            "is_common_password": True,
            "entropy_bits": round(calculate_entropy(password), 2),
            "score": score,
            "strength": strength_label,
            "recommendations": recommendations,
        }

    # Length score (up to 40 pts)
    if length < 8:
        score += length * 3
        recommendations.append("Password is too short. Increase length to at least 12 characters.")
    elif 8 <= length < 12:
        score += 25
        recommendations.append("Consider lengthening your password to 12 or more characters for better security.")
    elif 12 <= length < 16:
        score += 35
    else:
        score += 40

    # Character Diversity (up to 40 pts)
    if has_lower:
        score += 10
    else:
        recommendations.append("Include lowercase letters (a-z).")

    if has_upper:
        score += 10
    else:
        recommendations.append("Include uppercase letters (A-Z).")

    if has_digit:
        score += 10
    else:
        recommendations.append("Include numeric digits (0-9).")

    if has_special:
        score += 10
    else:
        recommendations.append("Include special characters (e.g., !@#$%^&*).")

    # Entropy bonus (up to 20 pts)
    entropy = calculate_entropy(password)
    if entropy >= 60:
        score += 20
    elif entropy >= 40:
        score += 10
    elif entropy >= 25:
        score += 5

    # Penalties
    if re.search(r'(.)\1{2,}', password):
        score = max(0, score - 15)
        recommendations.append("Avoid repeating characters sequentially (e.g., 'aaa', '111').")

    if re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|qwe)', password.lower()):
        score = max(0, score - 10)
        recommendations.append("Avoid simple keyboard sequences like '123' or 'abc'.")

    score = min(100, max(0, score))

    # Strict cap for short passwords (<8 chars)
    if length < 8:
        score = min(score, 45)

    if score < 30:
        strength_label = "Very Weak"
    elif score < 50:
        strength_label = "Weak"
    elif score < 70:
        strength_label = "Moderate"
    elif score < 85:
        strength_label = "Strong"
    else:
        strength_label = "Very Strong"

    if not recommendations:
        recommendations.append("Great job! Your password meets high security standards.")

    return {
        "password_length": length,
        "has_uppercase": has_upper,
        "has_lowercase": has_lower,
        "has_digits": has_digit,
        "has_special": has_special,
        "is_common_password": False,
        "entropy_bits": round(entropy, 2),
        "score": score,
        "strength": strength_label,
        "recommendations": recommendations,
    }
