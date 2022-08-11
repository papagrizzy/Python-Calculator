import functionpack as fc
from colorama import Fore, Back, Style
import time


name=input(f"{Fore.WHITE}{Style.BRIGHT}Please Enter your name user: ").upper()
print(F"{Fore.RED}{Back.CYAN}{Style.BRIGHT} WELCOME {name}! {Fore.RESET}{Back.RESET}")
print(" ")

choice_list=[1, 2, 3, 4, 25, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
run="Y"
while run=="Y":
    print(F"{Fore.WHITE}OPTIONS(Choose one):\n{Fore.LIGHTBLUE_EX}01. Pure Arithmatics\n02. Trigonomatric calculations\n03. Logarithmic calculations\n04. Quadratic Equations\n05. DECIMAL to BINARY\n06. DECIMAL to OCTAL\n07. DECIMAL to HEXADECIMAL\n08. BINARY to DECIMAL\n09. BINARY to OCTAL\n10. BINARY to HEXADECIMAL\n11. OCTAL to BINARY\n12. OCTAL to DECIMAL\n13. OCTAL to HEXADECIMAL\n14. HEXADECIMAL to BINARY\n15. HEXADECIMAL to DECIMAL\n16. HEXADECIMAL to OCTAL")
    print(" ")
    choice=int(input(f"{Fore.YELLOW}Enter choice: "))
    while choice not in choice_list:
        print(f"{Fore.RED}{Style.BRIGHT}Invalid Input!! Try Again{Fore.YELLOW}")
        choice=int(input("Enter choice: "))
    

    #FIRST SECTION
    if choice == 1:
        choice_list_01=[1, 2, 3, 4, 25, 6, 7]
        print(" ")
        print(f"{Fore.WHITE}Options(Choose one):\n01. Addition\n02. Subtraction\n03. Multiplication\n04. Division\n05. Exponential to the power X\n06. Power\n07. Root")
        print(" ")
        choice_01=int(input(F"{Fore.YELLOW}Enter choice: "))
        while choice_01 not in choice_list_01:
            print(f"{Fore.RED}'Invalid input!!'")
            choice_01=int(input(F"{Fore.YELLOW}Enter choice: "))
        print(" ")


        #ADDITION
        if choice_01==1:
            
            #Inputting List
            list_01=[]
            flow=run
            print("Type 'STOP' to end list")
            while flow != "stop":
                temp=input("> ")
                try:
                    temp1=int(temp)
                    list_01.append(temp1)
                except ValueError:
                    if temp.lower()=="stop":
                        flow="stop"
            print(f'{Fore.WHITE}Your Answer: {fc.addition(list_01)}')
        

        #SUBTRACTION
        elif choice_01==2:

            #Inputting list
            list_02=[]
            flow=run
            print("Type 'STOP' to end list")
            while flow != "stop":
                temp=input("> ")
                try:
                    temp1=int(temp)
                    list_02.append(temp1)
                except ValueError:
                    if temp.lower()=="stop":
                        flow="stop"
            print(f'{Fore.WHITE}Your Answer: {fc.subtraction(list_02)}')
        

        #MULTIPLICATION
        elif choice_01==3:

            #Inputting list
            list_03=[]
            flow=run
            print("Type 'STOP' to end list")
            while flow != "stop":
                temp=input("> ")
                try:
                    temp1=int(temp)
                    list_03.append(temp1)
                except ValueError:
                    if temp.lower()=="stop":
                        flow="stop"
            print(f'{Fore.WHITE}Your Answer: {fc.multiplication(list_03)}')
        

        #DIVISION
        elif choice_01==4:

            #Inputting  list
            list_04=[]
            flow=run
            print("Type 'STOP' to end list")
            while flow != "stop":
                temp=input("> ")
                try:
                    temp1=int(temp)
                    list_04.append(temp1)
                except ValueError:
                    if temp.lower()=="stop":
                        flow="stop"
            print(f'{Fore.WHITE}Your Answer: {fc.division(list_04)}')


        #E^x 
        elif choice_01==25:

            x=int(input(f"{Fore.YELLOW}Enter the value of X: "))
            print(f"{Fore.WHITE}Your Answer: {fc.expraise(x)}")

        #POWER
        elif choice_01==6:
            num=int(input(f"{Fore.YELLOW}Enter base: "))
            num1=int(input(f"{Fore.YELLOW}Enter the power: "))
            temp=(fc.power(num, num1))
            print(F'Your Answer: {str(temp)}')
        

        #ROOT
        elif choice_01==7:
            num=int(input(f"{Fore.YELLOW}Enter the Radicand: "))
            num1=int(input(f"{Fore.YELLOW}Enter Power: "))
            print(F'{Fore.WHITE}Your Answer: {fc.rootover(num, num1)}')

    
    #SECOND SECTION
    if choice==2:
        choice_list_02=[1, 2, 3]
        print(" ")
        print(f"{Fore.WHITE}Options(Choose one):\n01. Sine\n02. Cosine\n03. Tangent")
        print(" ")
        choice_02=int(input(F"{Fore.YELLOW}Enter choice: "))
        while choice_02 not in choice_list_02:
            print(f"{Fore.RED}'Invalid input!!'")
            choice_01=int(input(F"{Fore.YELLOW}Enter choice: "))
        print(" ")

        #SINE
        if choice_02==1:
            num=int(input(f"{Fore.YELLOW}Enter the Angle: "))
            print(F'{Fore.WHITE}Your Answer: {fc.sine(num)}')


        #COSINE
        if choice_02==2:
            num=int(input(f"{Fore.YELLOW}Enter the Angle: "))
            print(F'{Fore.WHITE}Your Answer: {fc.cosine(num)}')             


        #TANGENT
        if choice_02==3:
            num=int(input(f"{Fore.YELLOW}Enter the Angle: "))
            print(F'{Fore.WHITE}Your Answer: {fc.tangent(num)}')
        

    #THIRD SECTION
    if choice==3:
        choice_list_03=[1, 2]
        print(" ")
        print(f"{Fore.WHITE}Options(Choose one):\n01. LOG\n02. Natural LOG")
        print(" ")
        choice_03=int(input(F"{Fore.YELLOW}Enter choice: "))
        while choice_03 not in choice_list_03:
            print(f"{Fore.RED}'Invalid input!!'")
            choice_01=int(input(F"{Fore.YELLOW}Enter choice: "))
        print(" ")


        #Logarithm
        if choice_03==1:
            num=int(input(f"{Fore.YELLOW}Enter the Number: "))
            print(F'{Fore.WHITE}Your Answer: {fc.logarithm(num)}')

        
        #Natural LOG
        if choice_03==2:
            num=int(input(f"{Fore.YELLOW}Enter the Number: "))
            print(F'{Fore.WHITE}Your Answer: {fc.naturalog(num)}')

    
    #FOURTH SECTION
    if choice==4:
        num1=int(input(f"{Fore.YELLOW}Enter the 1st Coefficient: "))
        num2=int(input(f"{Fore.YELLOW}Enter the 2nd Coefficient: "))
        num3=int(input(f"{Fore.YELLOW}Enter the 3rd Coefficient: "))
        print(fc.quadratic_equations(num1, num2, num3))


    #FIFTH SECTION
    if choice==25:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        fc.DecimalToBinary(num)

    
    #SIXTH SECTION
    if choice==6:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.DecimalToOctal(num))


    #SEVENTH SECTION
    if choice==7:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.DecimalToHexadecimal(num))


    #EIGHTH SECTION
    if choice==8:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.BinaryToDecimal(num))


    #NINTH SECTION
    if choice==9:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.BinaryToOctal(num))


    #TENTH SECTION
    if choice==10:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.BinaryToHexadecimal(num))


    #ELEVENTH SECTION
    if choice==11:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.OctalToBinary(num)) 


    #TWELVTH
    if choice==12:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.OctalToDecimal(num)) 


    #THIRTEENTH
    if choice==13:
        num=int(input(f"{Fore.YELLOW}Enter number: "))
        print(fc.OctaltoHexadecimal(num))


    #FOURTEENTH
    if choice==14:
        num=input(f"{Fore.YELLOW}Enter number: ")
        print(fc.HexadecimalToBinary(num))

    
    #FIFTEENTH
    if choice==15:
        num=input(f"{Fore.YELLOW}Enter number: ")
        print(fc.HexadecimalToDecimal(num))



    #SIXTEENTH
    if choice==16:
        num=input(f"{Fore.YELLOW}Enter number: ")
        print(fc.HexadecimalToOctal(num))

    run=input("Do you want to continue?(Y/n)").upper()
print("Quitting", end="")
time.sleep(0.25)
print(".", end="")
time.sleep(0.25)
print(".", end="")
time.sleep(0.25)
print(".", end="")
time.sleep(0.25)
print(".", end="")
time.sleep(0.25)
print(".")
time.sleep(0.25)
print(" ")
print(f"{Fore.CYAN}GoodBye {name}!!!")
