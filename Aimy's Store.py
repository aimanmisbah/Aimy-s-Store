import streamlit as st
import datetime

# Function to display receipt
def print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, account_info=None):
    receipt = f"""
    <div style="text-align: center;">
        <h2>Aimy's Store</h2>
        <h3>Cash Receipt</h3>
        <hr style="border: 1px solid black;">
        <p>Date: {datetime.datetime.now().strftime('%Y-%m-%d')} | Time: {datetime.datetime.now().strftime('%H:%M:%S')}</p>
        <hr>
        <table style="margin: auto;">
            <tr>
                <th style="padding: 5px;">Item</th>
                <th style="padding: 5px;">Qty</th>
                <th style="padding: 5px;">Price (PKR)</th>
            </tr>"""
    
    for item in items:
        receipt += f"""
            <tr>
                <td style="padding: 5px;">{item['name']}</td>
                <td style="padding: 5px;">{item['quantity']}</td>
                <td style="padding: 5px;">{item['total_price']}</td>
            </tr>"""
    
    receipt += f"""
        </table>
        <hr>
        <p>Total Quantity: {total_quantity}</p>
        <p>Net Amount: PKR {total_amount:.2f}</p>
        <p>Received Amount: PKR {received_amount:.2f}</p>
        <p>Change: PKR {change:.2f}</p>
        <hr>
        <p>Payment Method: {payment_method}</p>
        <p>Account Info: {account_info}</p>
        <hr>
        <p>Thank you for shopping at Aimy's Store!</p>
        <p>Hoping to serve you again soon!</p>
    </div>"""
    
    return receipt

# Main function for Streamlit app
def supermarket_billing():
    st.title("Aimy's Store Billing System")
    
    items = []
    total_quantity = 0
    total_amount = 0.0

    st.header("Add Items")
    while True:
        item_name = st.text_input("Enter the item name (or leave blank to finish):")
        
        if item_name == "":
            break
        
        quantity = st.number_input(f"Enter the quantity of {item_name}:", min_value=1, step=1)
        price = st.number_input(f"Enter the price of {item_name} (in PKR):", min_value=0.0, step=0.01)
        
        total_price = quantity * price
        items.append({'name': item_name, 'quantity': quantity, 'total_price': total_price})
        
        total_quantity += quantity
        total_amount += total_price
    
    st.write(f"Total Amount: PKR {total_amount:.2f}")
    
    payment_method = st.selectbox("Select Payment Method:", ["Cash", "Card"])
    
    received_amount = 0.0
    account_info = None  # Initialize account_info variable

    if payment_method == "Card":
        account_info = st.text_input("Enter your 13-digit bank account number:", max_chars=13)
        if len(account_info) == 13 and account_info.isdigit():
            account_info = '*' * 9 + account_info[-4:]  # Masking account number
            pin_code = st.text_input("Enter your PIN code:", type="password")  # Hidden input for PIN
            if st.button("Submit Payment"):
                st.success("Processing card transaction...")
                received_amount = total_amount  # Assuming the card payment is successful
        else:
            st.warning("Please enter a valid 13-digit account number.")
    
    elif payment_method == "Cash":
        received_amount = st.number_input("Enter the amount received from customer (in PKR):", min_value=0.0, step=0.01)
        if received_amount >= total_amount:
            if st.button("Submit Payment"):
                change = received_amount - total_amount
                st.success("Payment Successful!")
        else:
            st.warning("Received amount is less than the total amount.")
    
    # Display receipt if payment is processed
    if received_amount >= total_amount:
        change = received_amount - total_amount
        receipt = print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, account_info)
        st.markdown(receipt, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    supermarket_billing()
