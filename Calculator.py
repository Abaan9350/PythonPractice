def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(f"Result: {result}")

    else:
        print("Invalid Input")

        option = input("Is your character a boy?\n")
        if option.lower() == "yes":
            option = input("Does he wear spectacles?\n")
            if option.lower() == "yes":
                option = input("Does he get scolded in class frequently?\n")
                if option.lower() == "yes":
                    option = input("Does he usually wear shirts?\n")
                    if option.lower() == "yes":
                        option = input("Does he invest in stock market?\n")
                        if option.lower() == "yes":
                            option = input("Does he have a cat?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Raihan!")
                            else:
                                print("You are thinking of Ganesh!")
                        else:
                            option = input("Does he live in Nerul?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Aditya Chaskar!")
                    else:
                        option = input("Does he invest in stock market?\n")
                        if option.lower() == "yes":
                            option = input("Does he have a cat?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Raihan!")
                            else:
                                option = input("Is he good at driving? (lol)\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Vedant Shetty")
                        else:
                            option = input("Good at driving cars?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Vedant Shetty!")
                            else:
                                option = input("Is he good at video games?\n")
                                if option.lower() == "yes":
                                    option = input("Does he sleep in class?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Anish Masurkar!")
                                    else:
                                        print("You are thinking of Nidhish!")
                                option = input("Does he live in Nerul?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Aditya Chaskar!")
                else:
                    option = input("Does he usually wear shirts in class?\n")
                    if option.lower() == "yes":
                        option = input("Good Ball knowledge?\n")
                        if option.lower() == "yes":
                            print("You are thinking of Soham Desai!")
                        else:
                            option = input("Extremely Good at Maths?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Ashish!")
                            else:
                                option = input("Is his Hometown in Nashik?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Akshar!")
                                else:
                                    option = input("Good at Chess?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Shreyash!")
                                    else:
                                        option = input("Does he play football?\n")
                                        if option.lower() == "yes":
                                            print("You are thinking of Aditya Chaskar!")
                                        else:
                                            print("You are thinking of Vedant Patil!")
                    else:
                        option = input("Is he good at basketball?\n")
                        if option.lower() == "yes":
                            print("You are thinking of Tejas!")
                        else:
                            option = input("Is he really good at mathematics?\n")
                            if option.lower() == "yes":
                                print("You are thinking of Ashish!")
                            else:
                                option = input("Hometown in Nagpur?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Akshar!")
                                else:
                                    option = input("Alibaug?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Manthan!")
                                    else:
                                        option = input("Does he look like Manthan?\n")
                                        if option.lower() == "yes":
                                            print("You are thinking of Aditya Chaskar!")
                    option = input("Does he get scolded in class usually?\n")
                    if option.lower() == "yes":
                        option = input("Does he wear shirts frequently?\n")
                        if option.lower() == "yes":
                            option = input("Does he have a beard?\n")
                            if option.lower() == "yes":
                                option = input("Kashmir?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Aditya Dogra")
                            else:
                                option = input("Fufu?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Danny!")
                                else:
                                    option = input("Does he go to gym?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Atharva!")
                        else:
                            option = input("Is he good at football?\n")
                            if option.lower() == "yes":
                                option = input("Is he known for his hair?\n")
                                if option.lower() == "yes":
                                    print("You are thinking of Aryan!")
                                else:
                                    option = input("Is his walk iconic?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Dipesh!")
                                    else:
                                        print("You are thinking of Abaan!")
                            else:
                                option = input("Is he into PC games?\n")
                                if option.lower() == "yes":
                                    option = input("Does he sleep in class?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of: Anish Masurkar!")
                                    else:
                                        option = input("Is he into Video editing?\n")
                                        if option.lower() == "yes":
                                            print("You are thinking of Amruthesh")
                                        else:
                                            option = input("Does he have a beard?\n")
                                            if option.lower() == "yes":
                                                print("You are thinking of Saad!")
                                            else:
                                                print("You are thinking of Suraj!")
                                else:
                                    option = input("Does he have good ball knowledge?\n")
                                    if option.lower() == "yes":
                                        print("You are thinking of Atharva!")

        else:
            print("Does he usually wear shirts?")
            option = input()
            if option.lower() == "yes":
                print("Is he good in academics?")
                option = input()
                if option.lower() == "yes":
                    print("Is he in the college Drama team?")
                    option = input()
                    if option.lower() == "yes":
                        print("You are thinking of Sujit Asari!")
                    else:
                        print("Interest in camera?")
                        option = input()
                        if option.lower() == "yes":
                            print("Kerala?")
                            option = input()
                            if option.lower() == "yes":
                                print("You are thinking of Amruthesh!")
                            else:
                                print("You are thinking of Sahil Pawar!")
                        else:
                            print("Autistic?")
                            option = input()
                            if option.lower() == "yes":
                                print("You are thinking of Uday!")
                            else:
                                print("Constant hairstyle since Sem 1?")
                                option = input()
                                if option.lower() == "yes":
                                    print("You are thinking of Vedant Borade!")
                                else:
                                    print("You are thinking of Hrishikesh!")
                else:
                    print("Is he involved in any college clubs?")
                    option = input()
                    if option.lower() == "yes":
                        print("Is he south Indian?")
                        option = input()
                        if option.lower() == "yes":
                            print("You are thinking of Aditya Venkat!")
            else:
                print("Is he good at basketball?")
                option = input()
                if option.lower() == "yes":
                    print("You are thinking of Abhishek!")
                else:
                    print("Fish??")
                    option = input()
                    if option.lower() == "yes":
                        print("You are thinking of Pravanshu!")
                    else:
                        print("Good in academics??")
                        option = input()
                        if option.lower() == "yes":
                            print("Has helped everyone with assignments?")
                            option = input()
                            if option.lower() == "yes":
                                print("Good ball knowledge?")
                                option = input()
                                if option.lower() == "yes":
                                    print("You are thinking of Sameer!")
