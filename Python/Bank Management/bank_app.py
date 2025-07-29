import streamlit as st
import json
import random
import string
from pathlib import Path

class Bank:
    def __init__(self):
        self.database = 'data.json'
        self.data = self.load_data()

    def load_data(self):
        if Path(self.database).exists():
            try:
                with open(self.database, 'r') as file:
                    return json.load(file)
            except Exception as e:
                st.error(f"Error loading data: {e}")
                return []
        return []

    def save_data(self):
        with open(self.database, 'w') as file:
            json.dump(self.data, file, indent=2)

    def generate_account_no(self):
        acc_no = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=7))
        return acc_no

    def create_account(self, name, age, email, pin):
        if age < 18 or len(pin) != 4 or not pin.isdigit():
            return False, "You must be 18+ and PIN should be 4 digits."
        acc_no = self.generate_account_no()
        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": acc_no,
            "balance": 0
        }
        self.data.append(account)
        self.save_data()
        return True, acc_no

    def find_account(self, acc_no, pin):
        for acc in self.data:
            if acc["accountNo"] == acc_no and acc["pin"] == pin:
                return acc
        return None

    def deposit(self, acc, amount):
        if amount <= 0 or amount > 10000:
            return False, "Deposit must be between ₹1 and ₹10,000."
        acc["balance"] += amount
        self.save_data()
        return True, acc["balance"]

    def withdraw(self, acc, amount):
        if amount <= 0 or amount > acc["balance"]:
            return False, "Invalid amount. Check your balance."
        acc["balance"] -= amount
        self.save_data()
        return True, acc["balance"]

    def update_details(self, acc, new_name=None, new_email=None, new_pin=None):
        if new_name:
            acc["name"] = new_name
        if new_email:
            acc["email"] = new_email
        if new_pin and len(new_pin) == 4 and new_pin.isdigit():
            acc["pin"] = new_pin
        self.save_data()
        return acc

    def delete_account(self, acc):
        self.data.remove(acc)
        self.save_data()
        return True

# --- Streamlit UI ---
st.set_page_config("💳 Bank App", layout="centered")
st.title("💳 Simple Bank System")

bank = Bank()

menu = st.sidebar.selectbox("Select Option", [
    "Create Account", "Deposit", "Withdraw", "Account Details", "Update Details", "Delete Account"
])

def account_login():
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    acc = bank.find_account(acc_no, pin)
    if acc:
        return acc
    else:
        st.warning("Invalid account number or PIN.")
        return None

if menu == "Create Account":
    st.subheader("🧾 Open New Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        success, msg = bank.create_account(name, age, email, pin)
        if success:
            st.success(f"Account created! Your account number: {msg}")
        else:
            st.error(msg)

elif menu == "Deposit":
    st.subheader("💰 Deposit Money")
    acc = account_login()
    if acc:
        amount = st.number_input("Enter amount to deposit", min_value=1)
        if st.button("Deposit"):
            success, msg = bank.deposit(acc, amount)
            if success:
                st.success(f"Deposit successful. New balance: ₹{msg}")
            else:
                st.error(msg)

elif menu == "Withdraw":
    st.subheader("🏧 Withdraw Money")
    acc = account_login()
    if acc:
        amount = st.number_input("Enter amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            success, msg = bank.withdraw(acc, amount)
            if success:
                st.success(f"Withdrawal successful. New balance: ₹{msg}")
            else:
                st.error(msg)

elif menu == "Account Details":
    st.subheader("🔍 View Account Details")
    acc = account_login()
    if acc:
        st.json(acc)

elif menu == "Update Details":
    st.subheader("✏️ Update Your Info")
    acc = account_login()
    if acc:
        name = st.text_input("New Name", value=acc["name"])
        email = st.text_input("New Email", value=acc["email"])
        pin = st.text_input("New PIN (4-digit)", type="password")
        if st.button("Update"):
            updated = bank.update_details(acc, name, email, pin)
            st.success("Details updated successfully!")
            st.json(updated)

elif menu == "Delete Account":
    st.subheader("❌ Delete Your Account")
    acc = account_login()
    if acc:
        if st.button("Confirm Delete"):
            bank.delete_account(acc)
            st.success("Your account has been deleted.")