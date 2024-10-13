import streamlit as st
import datetime

def print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, bank_account):
    st.subheader("Cash Receipt")  # Update the subheader here
    st.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}    Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.write("-" * 40)
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
    st.write(f"Payment Method: {payment_method}")
    st.write(f"Bank Account (last 4 digits): **** **** **** {bank_account[-4:]}")
    st.write("=" * 40)
    st.write("Thank you for shopping at Aimy's Store!")

def supermarket_billing():
    items = []
    total_quantity = 0
    total_amount = 0.0

    st.title("Aimy's Store")  # Updated title
    st.subheader("Cash Receipt")  # Initial subheader (if needed)

    item_counter = 0
    while True:
        item_name = st.text_input(f"Enter the item name {item_counter + 1} (or type 'done' to finish):", key=f"item_name_{item_counter}")
        if item_name.lower() == 'done':
            break

        quantity = st.number_input(f"Enter the quantity of {item_name}:", min_value=1, key=f"quantity_{item_counter}")
        price = st.number_input(f"Enter the price of {item_name} (in PKR):", min_value=0.0, key=f"price_{item_counter}")

        total_price = quantity * price
        items.append({'name': item_name, 'quantity': quantity, 'total_price': total_price})

        total_quantity += quantity
        total_amount += total_price

        item_counter += 1

    st.write(f"\nTotal Amount: PKR {total_amount:.2f}")

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
            print_receipt(items, total_quantity, total_amount, received_amount, change, payment_method, bank_account)

# Call the billing function
supermarket_billing()
