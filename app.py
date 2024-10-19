import pandas as pd 
import streamlit as st

def super_market():
    if 'items' not in st.session_state:
        st.session_state.items = []
    
    st.title("Amiy's Store")
    st.subheader("Billing System")

    item_name = st.text_input("Enter the item name:")
    quantity = st.number_input("Enter the quantity:", min_value=1, value=1)
    price_per_item = st.number_input("Enter the price per item:", min_value=0.0, value=0.0)

    if st.button("Add Item"):
        if item_name:
            total_price = quantity * price_per_item
            st.session_state.items.append({
                "name": item_name,
                "quantity": quantity,
                "total_price": total_price
            })
            st.success(f"Added {quantity} x {item_name} to the bill.")

    if st.session_state.items:
        st.subheader("Items in Cart:")
        items_df = pd.DataFrame(st.session_state.items)
        st.write(items_df)

        total_quantity = sum(item["quantity"] for item in st.session_state.items)
        total_amount = sum(item["total_price"] for item in st.session_state.items)
        
        st.write(f"Total Quantity: {total_quantity}")
        st.write(f"Total Amount: ${total_amount:.2f}")
        
        if st.button("Print Receipt"):
            print_receipt(st.session_state.items, total_quantity, total_amount)

def print_receipt(items, total_quantity, total_amount):
    st.subheader("Receipt")
    st.write("Aimy's Store")
    st.write("Cash Receipt")
    st.write("_" * 30)
    
    for item in items:
        st.write(f"Item Name: {item['name']}")
        st.write(f"Quantity: {item['quantity']}")
        st.write(f"Total Price: ${item['total_price']:.2f}")
        st.write("_" * 30)
    
    st.write(f"Total Quantity: {total_quantity}")
    st.write(f"Total Amount: ${total_amount:.2f}")
    st.write("_" * 30)

# Call the function
super_market()
