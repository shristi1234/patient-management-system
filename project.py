#This is for login process.

print("LOG IN")
Email = input("Enter your E-mail address")
print(Email)
Password = input("Enter your password 8 digit ")
print(Password)
#This is appointment taking process.
print("Take an Appointment")
print("List of Specialists")
print("1. Doctor A")
print("2. Doctor B")
print("3. Doctor C")
print("4. Doctor D")

# This is for Doctor A

select_doctor = input("Choose your doctor")

if select_doctor == "1":

        print("Doctor A \n a. 10AM-11AM \n b.12AM-1PM \n c. 2PM-3PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 10AM-11AM")
        elif your_time == "b":
            print("b. 12AM-1PM")
        elif your_time == "c":
            print("c. 2PM-3PM")
        else:
            print("Not available")
#This is for Doctor B

elif select_doctor == "2":

        print("Doctor B \n a. 10:30AM-11:30AM\n b. 12:30PM-1:30PM \n c. 2:30PM-3:30PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 10:30AM-11:30AM")
        elif your_time == "b":
            print("b. 12:30PM-1:30PM")
        elif your_time == "c":
            print("c. 2:30PM-3:30PM")
        else:
            print("Not available")

#This is for Doctor C

elif select_doctor == "3":

        print("Doctor C \n a. 11AM-12AM \n b. 1PM-2PM \nc. 3PM-4PM")

        your_time = input("Favouralbe time")

        if your_time == "a":
            print("a. 11AM-12AM")
        elif your_time == "b":
            print("b. 1PM-2PM")
        elif your_time == "c":
            print("c. 3PM-4PM")
        else:
            print("Not available")

#This is for Doctor D

elif select_doctor == "4":

        print("Doctor D \n a. 1:30PM-2:30AM \n b. 3:30PM-4:30PM \n c. 4:30PM-5:30PM")

        your_time = input("Favouralbe time")

        if your_time == "a":
            print("a. 1:30PM-2:30AM")
        elif your_time == "b":
            print("b. 3:30PM-4:30PM")
        elif your_time == "c":
            print("c. 2:30PM-3:30PM")
        else:
            print("Not available")


else:
    print("Doctor not available")

print("For cash Enter Y")
print("For credit Enter C")
payment = input("finish the payment")
if payment=="Y":
    print("payment done by cash")
    receivebill = input("Please enter the receipt for the bill")
    print(receivebill)
    print= input("Thank you")
elif payment=="C":
     print("payment done by credit")
     creditbill = input("Please enter the credit card number")
     print(creditbill)
     print("Thank you")
else:
    print("not paid and go for payment")




