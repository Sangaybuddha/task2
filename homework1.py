age = int(input("Enter your age:"))
student = input("Are you a student?(yes/no):")
if age <= 12:
    print("You are eligible for a discount on the movie ticket. ")
elif 13 <= age <= 18 and student == "yes":
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount.")
