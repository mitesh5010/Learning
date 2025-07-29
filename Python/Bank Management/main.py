import json
import random
import string
from pathlib import Path

class Bank:
  database = 'data.json'
  data = []

  try:
    if Path(database).exists():
      with open(database) as fs:
        data = json.loads(fs.read())
    else:
      print("no such file.")
  except Exception as err:
    print(f"Loading error :{err}")

  @staticmethod
  def __update(cls):
    with open(cls.database, 'w') as fs:
      fs.write(json.dumps(Bank.data))
    
  @classmethod
  def __accNoGenerate(cls):
    alpha = random.choices(string.ascii_letters, k=3)
    num = random.choices(string.digits, k=3)
    spcahr = random.choices(string.punctuation, k=1)
    id = alpha + num + spcahr
    random.shuffle(id)
    return ''.join(id)

  def CreateAccount(self):
    info = {
      "name": input("Name:-"),
      "age": int(input("Age:-")),
      "email": input("Email:-"),
      "pin": input("Pin(4 number):-"),
      "accountNo": Bank.__accNoGenerate(),
      "balance": 0
    }
    if info['age'] < 18 or len(str(info["pin"])) != 4:
      print("You are not eligible to open an account")
    else:
      print("Account created successfully")
      for i in info:
        print(f"{i} : {info[i]}")
      print("Your account number is:", info["accountNo"]," Please remember it.")
      Bank.data.append(info)
      Bank.__update(self)

  def DepositeMoney(self):
    accountNo = input("Enter your account number:-")
    pin = input("Enter your pin:-")

    userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

    if not userdata:
      print("Invalid account number or pin.")
    else:
      amount = int(input("Enter amount to deposit:-"))
      if amount > 10000 or amount <= 0:
        print("You can deposit below 10000 and above 0 at a time.")
      else:
        userdata[0]['balance'] += amount
        Bank.__update(self)
        print(f"Your new balance is: {userdata[0]['balance']}")

  def WithdrawMoney(self):
    accountNo = input("Enter your account number:-")
    pin = input("Enter your pin:-")

    userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

    if not userdata:
      print("Invalid account number or pin.")
    else:
      amount = int(input("Enter amount to withdraw:-"))
      if amount > userdata[0]['balance'] or amount <= 0:
        print("You can withdraw below your balance and above 0 at a time.")
      else:
        userdata[0]['balance'] -= amount
        Bank.__update(self)
        print(f"Your new balance is: {userdata[0]['balance']}")

  def GetAccountDetails(self):
    accountNo = input("Enter your account number:-")
    pin = input("Enter your pin:-")

    userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]
    print("Your Account Details:")
    for i in userdata[0]:
      print(f"{i}: {userdata[0][i]}")

  def updateDetails(self):
    accountNo = input("Enter your account number:-")
    pin = input("Enter your pin:-")

    userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

    if not userdata:
      print("No Account Found")
    else:
      print("You can not change Account Number, Age , Balance.")
      print("fill the changes else leave it empty")

      newData = {
        "name": input("New Name:-"),
        "email": input("New Email:-"),
        "pin" : input("New Pin:-"),
      }
      for key, value in newData.items():
        if value:
          userdata[0][key] = value
          Bank.__update(self)
      print("Details updated successfully.")
      print("Your new details are:")
      for i in userdata[0]:
        print(f"{i}: {userdata[0][i]}")

  def DeleteAccount(self):
    accountNo = input("Enter your account number:-")
    pin = input("Enter your pin:-")

    userdata = [i for i in Bank.data if i['accountNo'] == accountNo and i['pin'] == pin]

    if not userdata:
      print("No Account Found")
    else:
      Bank.data.remove(userdata[0])
      Bank.__update(self)
      print("Account deleted successfully.")
      print("Thank you for using our service.")



user = Bank()
print("1: create account")
print("2: Deposite money")
print("3: Withdraw money")
print("4: for details")
print("5: for updating details")
print("6: deleting account")

check = int(input("Enter your response:-"))

if check == 1:
  user.CreateAccount()
elif check == 2:
  user.DepositeMoney()
elif check == 3:
  user.WithdrawMoney()
elif check == 4:
  user.GetAccountDetails()
elif check == 5:
  user.updateDetails()
elif check == 6:
  user.DeleteAccount()


