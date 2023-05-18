print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()


combined_string = name1 + name2


t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")


l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")


true = t + r + u + e

love = l + o + v + e

love_score = int(str(true) + str(love))

score = f"Your score is {love_score}"

if (love_score < 10) or (love_score > 90):
    message = f"{score}, you go together like coke and mentos."
    print(message)
elif 40 <= love_score <= 50:
    message = f"{score}, you are alright together."
    print(message)
else:
    print(f"{score}.")



