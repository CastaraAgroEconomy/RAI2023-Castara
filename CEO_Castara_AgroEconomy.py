import streamlit as st  # Streamlit for app interface
import pandas as pd     # Pandas for data handling
import requests         # Requests for API calls
import datetime         # Date and time functions
# Import the yield tracking function from the get_yield_data script
from get_yield_data import yield_tracking

# App title
st.title("Castara AgroEconomy C-Suite pilot")

st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
st.write(" ")

# Placeholder for user authentication (to be integrated later)
def authenticate_user(username, password):
    """ Placeholder function for user authentication. """
    # Authentication logic to be added
    return True

# User role selection and main menu
def main_menu(user_role):
    """ Displays the main menu based on user role. """
    st.sidebar.title("Navigation")
    if user_role == "Franchisee":
        st.sidebar.button("Yield Management")
        st.sidebar.button("Financial Performance")
    elif user_role == "Management":
        st.sidebar.button("Franchise Performance")
        st.sidebar.button("Strategic Planning")
    elif user_role == "Investor":
        st.sidebar.button("Financial Overview")
        st.sidebar.button("Sustainability Impact")
    elif user_role == "Technical Staff":
        st.sidebar.button("Equipment Monitoring")
        st.sidebar.button("Maintenance Logs")
    else:
        st.sidebar.write("Select a valid user role.")

# Placeholder function for user dashboard
# def display_dashboard(user_role):
    # """ Display the dashboard based on user role. """
    # st.header(f"{user_role} Dashboard")
    # st.write("Welcome to the Castara AgroEconomy dashboard.")
    # Display additional content for each user role

# Update display_dashboard() function to include yield tracking for Franchisee
def display_dashboard(user_role):
    """ Display the dashboard based on user role. """
    st.header(f"{user_role} Dashboard")
    
    if user_role == "Franchisee":
        yield_tracking()  # This will call the function from get_yield_data.py
    else:
        st.write("Welcome to the Castara AgroEconomy dashboard.")

# Main app function
def main():
    # Placeholder for authentication (to be expanded)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if authenticate_user(username, password):
        # Select user role (for demo purposes)
        user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"])
        main_menu(user_role)
        display_dashboard(user_role)
    else:
        st.error("Authentication failed.")

# Run app
if __name__ == "__main__":
    main()
