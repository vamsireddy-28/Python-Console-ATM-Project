# ================== MAIN BANK CLASS ==================
class Villagebank:
    bank_name = 'grammeena bank'
    bank_manager = 'narasareddy'
    bank_IFSC = 7674916524

    def __init__(self, holdername, accountno, pin, holderage, hint):
        self.holdername = holdername
        self.accountno = accountno
        self.holderage = holderage

        # ---- ENCAPSULATION (PRIVATE VARIABLES) ----
        self.__pin = pin
        self.__hint = hint
        self.__balance = 0


# ================== MENU FUNCTION ==================
def atm_menu(account):
    while True:
        print("""
========= ATM MENU =========
1. User Details
2. Balance Enquiry
3. Deposit
4. Withdraw
5. Change PIN
6. Exit
============================
""")
        choice = int(input('Select option: '))

        if choice == 1:
            print(account.user_details())

        elif choice == 2:
            print(account.bal_amt())

        elif choice == 3:
            print(account.deposit())

        elif choice == 4:
            print(account.withdraw())

        elif choice == 5:
            print(account.cha_pin())

        elif choice == 6:
            print('Thank you for using Grammeena Bank ATM 🙏')
            break

        else:
            print('Invalid option. Please try again.')


    def __str__(self):
        return f'''
------ USER DETAILS ------
Bank Name     : {Villagebank.bank_name}
Account Holder: {self.holdername}
Account No    : {self.accountno}
Age           : {self.holderage}
--------------------------
'''

    def __check_pin(self, pin):
        return pin == self.__pin

    # ---------- USER DETAILS ----------
    def user_details(self):
        pin = int(input('Enter PIN: '))
        if self.__check_pin(pin):
            return self.__str__()
        return 'Invalid PIN'

    # ---------- BALANCE ----------
    def bal_amt(self):
        pin = int(input('Enter PIN: '))
        if self.__check_pin(pin):
            return f'Current Balance: {self.__balance}'
        return 'Invalid PIN'

    # ---------- DEPOSIT ----------
    def deposit(self):
        pin = int(input('Enter PIN: '))
        if self.__check_pin(pin):
            amount = int(input('Enter deposit amount: '))
            if amount > 0:
                self.__balance += amount
                return f'Deposit Successful. Balance: {self.__balance}'
            return 'Amount must be greater than 0'
        return 'Invalid PIN'

    # ---------- WITHDRAW ----------
    def withdraw(self):
        pin = int(input('Enter PIN: '))
        if self.__check_pin(pin):
            amount = int(input('Enter withdraw amount: '))
            if amount <= self.__balance:
                self.__balance -= amount
                return f'Withdraw Successful. Balance: {self.__balance}'
            return 'Insufficient Balance'
        return 'Invalid PIN'

    # ---------- CHANGE PIN ----------
    def cha_pin(self):
        old_pin = int(input('Enter old PIN: '))
        if self.__check_pin(old_pin):
            new_pin = int(input('Enter new PIN: '))
            self.__pin = new_pin
            return 'PIN changed successfully'
        return self.forgotpin()

    # ---------- FORGOT PIN ----------
    def forgotpin(self):
        hint = int(input('Enter hint: '))
        if hint == self.__hint:
            new_pin = int(input('Enter new PIN: '))
            self.__pin = new_pin
            return 'PIN reset successful'
        return 'Invalid hint'


# ================== OBJECT CREATION ==================
c1 = Villagebank('vamsi', 1554551515, 1234, 23, 7674916524)
atm_menu(c1)
