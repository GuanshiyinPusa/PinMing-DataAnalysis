import streamlit as st

# Create a list to hold your selections
selected_items = []

# Define your items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Create a checkbox for each item
for item in items:
    if st.checkbox(item):
        selected_items.append(item)

# Display the selected items
st.write("Selected Items:")
st.write(selected_items)
