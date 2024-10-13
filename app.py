import streamlit as st
import pandas as pd
import datetime

# Function to display and manage the billing system
def supermarket_billing():
    # Initialize the session state for items if not already done
    if 'items' not in st.session_state:
        st.session_state.items = []

    st.title("Aimy's Store")
    st.subheader("Billing System")

    # Input fields for item name, quantity, and price
    item_name = st.text_input("Enter the item name:")
    quantity = st.number_input("Enter the quantity:", min_value=1, value=1)
    price_per_item = st.number_input("Enter the price per item:", min_value=0.0, value=0.0)

    # Add item button
    if st.button("Add Item"):
        if item_name:
            total_price = quantity * price_per_item
            # Add item to session state
            st.session_state.items.append({
                'name': item_name,
                'quantity': quantity,
                'total_price': total_price
            })
            st.success(f"Added {quantity} x {item_name} to the bill.")

    # Display the added items in a table
    if st.session_state.items:
        st.subheader("Items in Cart:")
        items_df = pd.DataFrame(st.session_state.items)
        st.write(items_df)

        # Calculate total quantity and amount
        total_quantity = sum(item['quantity'] for item in st.session_state.items)
        total_amount = sum(item['total_price'] for item in st.session_state.items)

        # Display total amount
        st.write(f"Total Quantity: {total_quantity}")
        st.write(f"Total Amount: ${total_amount:.2f}")

        # Receipt button
        if st.button("Print Receipt"):
            print_receipt(st.session_state.items, total_quantity, total_amount)

# Function to print receipt
def print_receipt(items, total_quantity, total_amount):
    st.subheader("Receipt")
    st.write("Aimy's Store")  # Add store name above the cash receipt
    st.write("Cash Receipt")
    st.write("─" * 30)  # Line separator

    # Display items in a formatted way
    for item in items:
        st.write(f"{item['name']:20} | Quantity: {item['quantity']:5} | Total Price: ${item['total_price']:.2f}")
    
    st.write("─" * 30)  # Another line separator
    st.write(f"{'Total Quantity:':<20} {total_quantity:>5}")
    st.write(f"{'Total Amount:':<20} ${total_amount:.2f}")

# Call the billing function
supermarket_billing()
