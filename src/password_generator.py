"""
Module 3: Secure Password Generator
-----------------------------------
Generates cryptographically secure passwords using Python's `secrets` module 
(CSPRNG) with guaranteed character type inclusion.
"""

import secrets
import string
from typing import Dict, Any


def generate_secure_password(
    length: int = 16,
    include_upper: bool = True,
    include_lower: bool = True,
    include_digits: bool = True,
    include_special: bool = True
) -> str:
    """Generates a cryptographically secure random password satisfying user criteria."""
    categories = []
    if include_upper:
        categories.append(string.ascii_uppercase)
    if include_lower:
        categories.append(string.ascii_lowercase)
    if include_digits:
        categories.append(string.digits)
    if include_special:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        categories.append(special_chars)

    if not categories:
        raise ValueError("At least one character type must be selected.")

    if length < len(categories):
        raise ValueError(
            f"Password length ({length}) must be at least {len(categories)} "
            f"to include at least one character from each of the selected categories."
        )

    # 1. Guarantee at least ONE character from each selected category
    password_chars = [secrets.choice(cat) for cat in categories]

    # 2. Fill remaining slots from combined pool
    combined_pool = "".join(categories)
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(combined_pool))

    # 3. Cryptographically shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def generate_and_evaluate_password(
    length: int = 16,
    include_upper: bool = True,
    include_lower: bool = True,
    include_digits: bool = True,
    include_special: bool = True
) -> Dict[str, Any]:
    """Generates a secure password and evaluates its strength using Module 1."""
    from .password_checker import check_password_strength

    pwd = generate_secure_password(length, include_upper, include_lower, include_digits, include_special)
    evaluation = check_password_strength(pwd)

    return {
        "generated_password": pwd,
        "length": length,
        "criteria": {
            "uppercase": include_upper,
            "lowercase": include_lower,
            "digits": include_digits,
            "special": include_special,
        },
        "strength_evaluation": evaluation,
    }
