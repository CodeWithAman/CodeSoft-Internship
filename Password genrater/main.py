import random
import string 


if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)

    s2 = string.ascii_uppercase
    # print(s2)

    s3 = string.digits
    # print(s3)

    s4 = string.hexdigits
    # print(s4)

    s5 = string.octdigits
    # print(s5)

    s6 = string.punctuation
    # print(s6)

pass_len = int(input("Enter Your Password Length: "))

S = []

S.extend(list(s1))
S.extend(list(s2))
S.extend(list(s3))
S.extend(list(s4))
S.extend(list(s5))
S.extend(list(s6))

# print(S)

# random.shuffle(S)

print("Your password is : ")
print("".join(random.sample(S , pass_len)))