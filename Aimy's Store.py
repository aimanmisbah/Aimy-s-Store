import streamlit as st
import datetime

# Function to display receipt
def print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, account_info):
    st.write("\n" + "=" * 40)
    st.header("Aimy's Store")
    st.subheader("Cash Receipt")
    st.write("=" * 40)
    st.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}  Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.write("-" * 40)

    # Receipt table
    st.write("{:<15} {:<10} {:<10}".format('Item', 'Qty', 'Price (PKR)'))
    st.write("-" * 40)
    for item in items:
        st.write("{:<15} {:<10} {:<10}".format(item['name'], item['quantity'], item['total_price']))

    st.write("-" * 40)
    st.write(f"Total Quantity: {total_quantity}")
    st.write("")  # Line gap
    st.write(f"Net Amount: PKR {total_amount:.2f}")
    st.write(f"Received Amount: PKR {received_amount:.2f}")
    st.write(f"Change: PKR {change:.2f}")
    st.write("")  # Line gap
    st.write(f"Payment Method: {payment_method}")

    if payment_method == 'Card':
        st.write(f"Account Number: {'*' * 9}{account_info[-4:]}")

    st.write("=" * 40)
    st.write("Thank you for shopping at Aimy's Store!")
    st.write("Hoping to serve you again soon!")
    st.write("=" * 40)

# Main Billing function
def supermarket_billing():
    st.title("Aimy's Store Billing System")

    items = []
    total_quantity = 0
    total_amount = 0.0

    st.write("Enter items below:")

    while True:
        item_name = st.text_input("Enter the item name (or leave blank to finish):", "")
        
        if item_name == "":
            break
        
        try:
            quantity = st.number_input(f"Enter the quantity of {item_name}:", min_value=1, step=1)
            price = st.number_input(f"Enter the price of {item_name} (in PKR):", min_value=0.0, step=0.01)
        except ValueError:
            st.error("Invalid input. Please enter valid numbers for quantity and price.")
            continue
        
        total_price = quantity * price
        items.append({'name': item_name, 'quantity': quantity, 'total_price': total_price})
        
        total_quantity += quantity
        total_amount += total_price

    st.write(f"\nTotal Amount: PKR {total_amount:.2f}")

    payment_method = st.selectbox("Select Payment Method:", ["Cash", "Card"])

    if payment_method == "Cash":
        received_amount = st.number_input("Enter the amount received from customer (in PKR):", min_value=0.0, step=0.01)

        if received_amount >= total_amount:
            change = received_amount - total_amount
        else:
            st.error(f"Amount received is less than the total amount. You need PKR {total_amount - received_amount:.2f} more.")
            return

    elif payment_method == "Card":
        account_info = st.text_input("Enter your 13-digit Account Number (only last 4 will be shown):", max_chars=13)
        pin_code = st.text_input("Enter your PIN Code (last 4 digits will be hidden):", type="password")

        if len(account_info) != 13:
            st.error("Account Number must be 13 digits long.")
            return
        if len(pin_code) < 4:
            st.error("PIN Code must be at least 4 digits.")
            return

        # Assuming the card transaction is successful
        received_amount = total_amount  # Full amount paid via card
        change = 0.0

    print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, account_info)

# Call the billing function
if __name__ == "__main__":
    supermarket_billing()
