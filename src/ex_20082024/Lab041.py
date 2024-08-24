score = int(input("Enter your score\n"))
# score >=90 and scroe <=100 -> "A"
# score >=80 and scroe <=89 -> "B"

if score >= 90 and score <= 100:  # Simplified Chaining Format -> 90 <= score <= 100
    print("You grade is ", "A")
elif score >= 80 and score <= 89:
    print("You grade is ", "B")
elif score >= 70 and score <= 79:
    print("You grade is ", "C")
elif score >= 60 and score <= 69:
    print("You grade is ", "D")
elif score >= 100:
    print("You are  Superman!!")
else:
    print("You grade is ", "F")