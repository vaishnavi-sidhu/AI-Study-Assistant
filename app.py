subject = input("Enter Subject: ")
exam_date = input("Enter Exam Date: ")

print("\n===== AI STUDY ASSISTANT =====")
print(f"Subject: {subject}")
print(f"Exam Date: {exam_date}")

print("\nPersonalized Study Plan")
print("Week 1: Learn fundamentals")
print("Week 2: Practice important topics")
print("Week 3: Solve previous year questions")
print("Week 4: Mock tests and revision")

print("\nQuick Quiz")
print("Q1. What is your confidence level? (Low/Medium/High)")

confidence = input("Answer: ")

if confidence.lower() == "low":
    print("Recommendation: Spend extra time on basics.")
elif confidence.lower() == "medium":
    print("Recommendation: Focus on practice questions.")
else:
    print("Recommendation: Focus on mock tests and revision.")

print("\nGood Luck for your Exam!")
