def give_me_number():
    while True:
        number = input("enter the number")
        print(f"ur enterd number is {number}")
        hmm = input("do you want to continue(y/n): ")
        if hmm == 'n':
            break
        else:
            continue
        
give_me_number()