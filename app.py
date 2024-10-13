import streamlit as st
import datetime

def print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, bank_account):
    st.subheader("Aimy's Store")  # Add store heading to the receipt
    st.subheader("Cash Receipt")
    st.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}    Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.write("-" * 50)

    # Heading for the items table
    st.write("{:<20} {:<10} {:<10}".format('Item', 'Qty', 'Price (PKR)'))
    st.write("-" * 50)

    # Display each item
    for item in items:
        st.write("{:<20} {:<10} {:<10}".format(item['name'], item['quantity'], item['total_price']))

    st.write("-" * 50)
    st.write(f"Total Quantity: {total_quantity}")
    st.write("")  # Line gap
    st.write(f"Net Amount: PKR {total_amount:.2f}")
    st.write(f"Received Amount: PKR {received_amount:.2f}")
    st.write(f"Change: PKR {change:.2f}")
    st.write(f"Payment Method: {payment_method}")
    if payment_method == "Card":
        st.write(f"Bank Account (last 4 digits): **** **** **** {bank_account[-4:]}")
    st.write("=" * 50)
    st.write("Thank you for shopping at Aimy's Store!")

def supermarket_billing():
    # Initialize session state for items if it doesn't exist
    if 'items' not in st.session_state:
        st.session_state.items = []

    # Ensure items is a list
    if not isinstance(st.session_state.items, list):
        st.session_state.items = []

    total_quantity = sum(item['quantity'] for item in st.session_state.items)
    total_amount = sum(item['total_price'] for item in st.session_state.items)

    st.title("Aimy's Store")  # Title of the app
    st.subheader("Billing System")

    # Input fields for item name, quantity, and price
    item_name = st.text_input("Enter the item name:")
    quantity = st.number_input("Enter the quantity:", min_value=1)
    price = st.number_input("Enter the price (in PKR):", min_value=0.0)

    # Button to add item
    if st.button("Add Item"):
        if item_name and quantity > 0 and price >= 0:
            total_price = quantity * price
            st.session_state.items.append({'name': item_name, 'quantity': quantity, 'total_price': total_price})
            st.success(f"Added {quantity} of {item_name} at PKR {price} each.")
        else:
            st.error("Please fill in all fields correctly.")

    # Display the current list of items
    if st.session_state.items:
        st.write("-" * 50)
        st.write("{:<20} {:<10} {:<10}".format('Item', 'Qty', 'Price (PKR)'))
        st.write("-" * 50)
        for item in st.session_state.items:
            st.write("{:<20} {:<10} {:<10}".format(item['name'], item['quantity'], item['total_price']))

        st.write("-" * 50)
        st.write(f"Total Amount: PKR {total_amount:.2f}")

    # Payment method selection
    payment_method = st.selectbox("Select Payment Method:", ["Cash", "Card"])
    received_amount = 0.0

    if payment_method == "Cash":
        received_amount = st.number_input("Enter the amount received from customer (in PKR):", min_value=0.0)
    else:
        bank_account = st.text_input("Enter your 13-digit Bank Account Number:", max_chars=13)
        pin_code = st.text_input("Enter your PIN Code:", type="password")

    change = received_amount - total_amount if payment_method == "Cash" else 0

    if st.button("Print Receipt"):
        if payment_method == "Cash" and received_amount < total_amount:
            st.error("Amount received is less than the total amount.")
        else:
            print_receipt(st.session_state.items, total_quantity, total_amount, received_amount, change, payment_method, bank_account)

# Call the billing function
supermarket_billing()
