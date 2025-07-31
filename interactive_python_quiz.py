Total_questions=0;
correct_answers = int(input("Enter the number of correct answers (out of 20): "))

score_percentage = (correct_answers / Total_questions) * 100

if score_percentage == 100:
    feedback = "Excellent! Perfect score! 💯"
elif score_percentage >= 80:
    feedback = "Great job! You're solid on the basics. ✅"
elif score_percentage >= 60:
    feedback = "Good effort, but some review is needed. 📘"
else:
    feedback = "Needs improvement. Keep practicing! 🛠️"

print(f"Your Score: {correct_answers} / {Total_questions}")
print(f"Percentage: {score_percentage:.2f}%")
print(feedback)