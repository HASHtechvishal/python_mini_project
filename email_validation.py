# email validation using python
# email validation using regex
import re
print(
    "Email validation type\n1. Normal validator--- enter N\n2. Regex validator--- enter R"
)
email_val = input("enter your validation type : ").upper()
if email_val == "R":
    # regex rull
    # a-z
    # 0-9
    # . _ time 1
    # @ time 1
    # . 2,3
    # / use for search something in regex
    # ? only give one char
    # $ search from back side
    email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_email_regex = input('Enater your email : ')
    if re.search(email_conditions, user_email_regex):
        print("Right Email")
    else:
        print("Wrong email")
        
elif email_val == "N":
    k, j, d = 0, 0, 0
    email = input(" Enter your email : ")

    if len(email) >= 6:  # check length
        if email[0].isalpha():  # first letter is capital
            if ("@" in email) and (
                email.count("@") == 1
            ):  # @ must be in email and only 1 @
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1

                    if k == 1 or j == 1 or d == 1:
                        print("please enter currect email formate")
                    else:
                        print("email is right")
            else:
                print("@ must be in email or only one @ must be there")
        else:
            print("first letter must be alpha bet")
    else:
        print("wrong email - lenght")
