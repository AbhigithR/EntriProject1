class BankingSystem:

    def __init__(self, Pin, Balance, Account_No, Phone_No):
        self.__pin = Pin
        self._Balance = Balance
        self.__Account_No = Account_No
        self.__Number = Phone_No

    def change_pin(self):  # User Can Set a New Pin
        Account_No = int(input("Please enter your Account Number :"))
        if Account_No == self.__Account_No:
            Number = int(input("Please enter your Mobile Number :"))
            if Number == self.__Number:
                Pin = int(input("Enter a new PIN :"))
                print("Your PIN Changed Successfully")
            else:
                print("Contact Number You Entered is Incorrect")
        else:
            print("The Account Number You Entered is Invalid")

    def customer_service(self):

        Name_Of_Bank = "Name of Bank :IBIM BANK"
        Address_Of_Bank = "Address Of Bank = Branch : PATHANAMTHITTA Building_No. VII / 350"
        customer_care = "Customer Care Number :1801 1500"
        email = "Email :ibimbank@gmail.com"
        service = (Name_Of_Bank, Address_Of_Bank, customer_care, email)
        print(service)

    def account_login(self):
        try:
            print("WELCOME ! PLEASE INSERT YOUR CARD")
            Account_Pin = int(input("please Enter your PIN :"))

            if Account_Pin == self.__pin:
                print("LOG IN SUCCESSFULLY\nWELCOME TO IBIM BANK")
                return True
            else:
                print("THE PIN OR ACCOUNT NUMBER YOU ENTERED IS INVALID")
                return False

        except ValueError:
            print("PLEASE ENTER PIN")


class Banking_Operation(BankingSystem):

    def check_balance(self):  # Operation To Check Bank Balance

        print(f"Your Bank Balance {self._Balance}\nTHANK YOU FOR USING IBIM BANK")

    def deposition_operation(self):  # Operation To Select For Deposition

        print("DEPOSIT PER TRANSACTION LIMIT : 200000")  # Message to User About the Transaction Limit
        continue_cancel = int(input("Press 1 To Continue\nPress 2 To Cancel"))  # User Can Continue or cancel operation
        if continue_cancel == 1:  # User Click continue
            account_type = int(
                input("press 1 for CURRENT \npress 2 for SAVING"))  # User Can select his/her Account Type
            if account_type == 1:  # Deposition in Current Account
                print("Acceptable Denomination: ₹100,₹200,₹500")

                # User Can put his cash on the machine and type the amount on the screen
                amount_deposit = int(input("please insert your cash and type the amount:"))
                if amount_deposit > 200000:
                    print("SORRY THE TRANSACTION LIMIT IS 200000")
                else:

                    enter_cancel = int(
                        input("press 1 to ENTER\npress 2 to CANCEL"))  # User Can Click Enter or cancel here
                    if enter_cancel == 1:
                        print("PLEASE WAIT ........ VALIDATING CASH.....")
                        print("The money you deposited :", amount_deposit)
                        # This Message Shows About User's Available Balance
                        print(f"Your Available Balance :{self._Balance + amount_deposit} ")
                    elif enter_cancel == 2:  # User Click Cancel and the deposition process cancelled
                        print("DEPOSITION PROCESS CANCELLED")
                    else:
                        print("THE NUMBER YOU ENTERED IS INCORRECT")
            elif account_type == 2:  # Deposition In Savings Account
                print("Acceptable Denomination: ₹100,₹200,₹500")
                amount_dep_saving = int(input("please insert your cash and type the amount:"))
                if amount_dep_saving > 200000:  # Deposition Above 2Lakh is Not Acceptable Through the Machine
                    print("Sorry The Transaction Limit is 200000")
                else:
                    # Here User Can Cancel or Continue Depositing money to his/her  Savings Account
                    cancel_enter = int(input("press 1 to ENTER\npress 2 to CANCEL"))
                    if cancel_enter == 1:
                        print("PLEASE WAIT ........ VALIDATING CASH.....")
                        print(f"The money you deposited : {amount_dep_saving}")
                        # This Message Shows About Users Available Balance
                        print(f"Your Available Balance :{self._Balance + amount_dep_saving} ")
                    elif cancel_enter == 2:
                        print("Deposition Process Cancelled")
                    else:
                        print("Please select a Valid Input 1 OR 2")
            else:
                print("PLEASE ENTER A VALID INPUT")  # User Entered an Invalid Input in Account Selection

        elif continue_cancel == 2:  # User clicked Cancel

            print("OPERATION CANCELLED")  # User Clicked Cancel Option and Operation Cancelled
        else:
            print("PLEASE ENTER 1 OR 2")  # User entered an invalid input

    def withdraw_money(self):
        # Asking user to confirm that he/she want to withdraw the money
        confirmation = int(input("are you sure want to withdraw the money?\npress 1 to CONFIRM or press 2 to "
                                 "CANCEL"))
        if confirmation == 1:  # User Confirmed to Withdraw Money
            # Asking the user to input the amount he/she wants to withdraw
            money = int(input('enter the amount you want to withdraw :'))
            confirm_withdraw = int(input('press 1 to Confirm\npress 2 to Cancel'))  # Confirm / Cancel
            if confirm_withdraw == 1:  # User Clicked Confirm
                if self._Balance < money:  # Users Balance is Lesser Than The Withdrawal Amount
                    print("INSUFFICIENT BALANCE\nYOUR BALANCE IS", self._Balance)
                else:
                    print("processing......")
                    print(f"Your Account has debited Rs {money} available balance is {self._Balance - money}")

            elif confirm_withdraw == 2:  # User Cancelled Operation
                print("Transaction Cancelled")
            else:
                print("ENTER A VALID INPUT")  # User Typed an Invalid Input
        elif confirmation == 2:
            print("Process Cancelled")
        else:
            print("SELECT A VALID INPUT 1 OR 2")

    def perform_operations(self):
        Choose = int(input("----------------------------\n"
                           " enter 1 for BALANCE CHECK  │\n"
                           " enter 2 to DEPOSIT         │\n"
                           " enter 3 to WITHDRAW        │ \n"
                           " enter 4 to CHANGE PIN      │ \n"
                           " enter 5 to CUSTOMER SERVICE│\n"
                           " enter 6 for EXIT           │ \n"
                           "--------------------------- :"))

        if Choose == 1:
            C1.check_balance()

        elif Choose == 2:
            C1.deposition_operation()
        elif Choose == 3:
            C1.withdraw_money()
        elif Choose == 4:
            C1.change_pin()
        elif Choose == 5:
            C1.customer_service()
        elif Choose == 6:
            print("T H A N K Y O U \nFOR USING IBIM BANK \nPLEASE COLLECT YOUR CARD BEFORE LEAVING")
            exit()

        else:
            print("Please enter a Valid Input")


C1 = Banking_Operation(9050, 55000, 123456, 987654321)
if C1.account_login():
    while True:
        C1.perform_operations()
