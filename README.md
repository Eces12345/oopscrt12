class Bank:
    def __init__(self):
      # dictionary to store account details
      # account_number will be the key, details (like holder name)will be the value 
self.accounts = {}
inital_amount=0

def creat_account(self,acc_no,acc_holder):
    self.acc_no=acc_no
    self.acc_holder=acc_holder
    if acc_no in self.accounts:
        return f"Account {acc_no}already exist!"
    self.accounts[acc_no]={"holder_name":acc_holder,"balance":0}
        return f"Account{acc_no}created for{acc_holder}."
    
def deposit(self,acc_no,amount):
    if acc_no not in self.accounts:
        return f"Account {acc_no}not found!"
    if amount < 500:
        return "Miniumum deposit amount is 500."
    self.accounts [acc_no]["balance"] +=amount
        return f"Deposited{amount} to Account {acc_no}.Current Balance:{self.accounts[acc_no]['balance']}"
    
def withdraw(self,acc_no,amount):
    if acc_no not in self.accounts:
        return f"Account {acc_no}not found!"
    if self.accounts [acc_no]["balance"] < amount:
        return "insufficient balance!"
    self.accounts [acc_no]["balance"] -=amount    
      return f"Withdraw {amount}from Account {acc_no}.Current Balance:{self.accounts[acc_no]['balance']}"
     
def chk_balance(self,acc_no):
    if acc_no not in self.accounts:    
        return f"Account {acc_no}not found!"
    return f"Account{acc_no} Balance:{self.account[acc_no]['balance']}" 
    
def display_account(self):
    if not self.accounts:
        return "No account found."
    result ="Bank Accounts:\n"
    for acc_no,details in self.accounts.items():
        result += f"Account No:{acc_no},Holder:{details['holder_name']},balance:{details['balance']}"
    return result
    
#Drive code
bank = Bank()
print("******************Student Management System****************")   
print("1.Acc_creat","","2.Deposit","","3.withdraw","","chk_balance","","5.show_details","","Exit")
print("------------------------------------------------")
        
  While True:      
        
    elif chice  == '1':
         acc_no = input("Enter account number:")
         amount=int(input("enter account_holdername:"))
         result =bank creat_account(acc_no,acc_holder)
        print(result)
        
    elif choice  == '2':
         acc_no = input("Enter account number to deposit:")
         amount=int(input("enter account to deposit:"))
        print(blank.deposit(acc_no,amount))
           
     elif choice  == '3':
         acc_no = input("Enter account number to withdraw form:")
         amount=int(input("enter account to withdraw:"))
        print(bank.withdraw(acc_no,amount))
            
     elif choice  == '4':
         acc_no = input("Enter account number to check balance:")
        print(bank.chk_balance(acc_no))
            
     elif choice  == '5':
         print(bank.display_accounts())
            
     elif choice  == '6':
        print("Exiting...")
        break
            
    else:    
        print("Invalid choice! Please try again.")
        
        
        
