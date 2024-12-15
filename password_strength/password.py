import re

def assess_password_strength(password):
    # Define the criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),._\-+=~`/?":{}|<>]', password))

    # Calculate the strength score
    strength_score = sum(
        [
            length_criteria,
            uppercase_criteria,
            lowercase_criteria,
            number_criteria,
            special_char_criteria,
        ]
    )

    # Provide feedback to the user
    feedback = []

    if not length_criteria:
        feedback.append("Your password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Your password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Your password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Your password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Your password should include at least one special character (e.g., !, @, #).")

    # Determine the password strength level
    if strength_score == 5:
        strength_level = "Strong"
    elif strength_score >= 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return {
        "strength_level": strength_level,
        "feedback": feedback,
    }

# Example usage
password = input("Enter a password to assess its strength: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['strength_level']}")
if result['feedback']:
    print("Feedback:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
