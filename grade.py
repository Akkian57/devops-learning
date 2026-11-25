score = int(input("Enter Score : "))

if score > 90 and score <= 100:
  print("A")
elif score >= 80 and score <= 89:
  print("B")
elif score >= 70 and score <= 79:
  print("C")
elif score >= 60 and score <= 69:
  print("D")
elif score < 60 and score >= 0:
  print("F")
else:
  print("Grade should be between 0 to 100 ")
