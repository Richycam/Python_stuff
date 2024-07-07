import random 






length = input("how long should the passsword be? \n ")
diff = input("how difficult should it be from 1-3? ")
print("okay then here is your password ")
converted_integer = int(length)
cov_int = int(diff)

counter = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"

count2 = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"

count3 = "!","?","!","@","#","$" "%","^","&","*","~","|","/","<",">","[","]"

if cov_int == 2:
    counter = counter + count2 
elif cov_int == 3:
    counter = counter + count2 + count3 
else: 
    counter = counter    


one = random.choice(counter)
two = random.choice(counter)
three = random.choice(counter)
four = random.choice(counter)
five = random.choice(counter)
six = random.choice(counter)
seven = random.choice(counter)
eight = random.choice(counter)
nine = random.choice(counter)
ten = random.choice(counter)


def main():
    if converted_integer== 1:
        print(one)
    elif converted_integer == 2:
        print(one + two)
    elif converted_integer == 3:
        print(one + two + three)
    elif  converted_integer== 4:
        print(one + two + three + four)
    elif converted_integer == 5:
        print(one + two + three + four + five)
    elif  converted_integer== 6:
        print(one + two + three + four + five + six)
    elif converted_integer == 7:
        print(one + two + three + four + five + six + seven)
    elif converted_integer == 8:
        print(one + two + three + four + five + six + eight)
    elif converted_integer == 9:
        print(one + two + three + four + five + six + eight+ nine)
    elif converted_integer == 10:
        print(one + two + three + four + five + six + eight + nine + ten)


main()
