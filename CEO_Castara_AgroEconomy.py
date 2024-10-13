import streamlit as st

from Get_yield_data import yield_tracking
from Get_performance_data  import franchise_performance
from Get_financial_data import financial_data
from Clear_screen import clear_display


# Function to clear the display
def clear_display():
    st.session_state.clear_display = True

# Placeholder for user authentication
def authenticate_user(username, password):
    return True  # Simplified for testing

# Login screen with validation
def login_screen():
    st.title("Castara AgroEconomy C-Suite Pilot")
    st.image("Castara_AgroEconomy_Mobile_App.JPG", caption="Vertical Farming franchise master control center for key management roles", use_column_width=True)
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login", key="login_process_button"):
        if not username or not password:
            st.error("Please enter both Username and Password.")
        else:
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                clear_display()
                role_selection_screen()
                st.write("press button to advance")
            else:
               st.error("Authentication failed. Please check your credentials.")

# Role selection screen
def role_selection_screen():
    st.header("Select Your Role")
    user_role = st.selectbox("Select your role", ["Franchisee", "Management", "Investor", "Technical Staff"], key="user_role_selection")
    if st.button("Next", key="user_role_select_button"):
        st.session_state.user_role = user_role
        display_dashboard_internal(user_role)
        st.write("press button to advance")
   

# Display role-specific dashboard
def display_dashboard_internal(user_role):
    clear_display()
    if user_role == "Franchisee":
        st.header("Franchisee Dashboard")
        yield_tracking()
    elif user_role == "Management":
        st.header("Management Dashboard")
        franchise_performance()
    else:
        st.header(f"{user_role} Dashboard")
        st.write(f"Welcome to the {user_role} Dashboard.")
        st.write(" ")
        st.write(f"⚠️ The {user_role} Dashboard will be installed at a future date")
        st.write(" ")
        st.write(" ")
    
    if st.button("Select option", key="option_select_button"):
        st.write("⚠️ Select option")
        st.write(" ")
        main_menu(user_role)


# Main menu with role options
def main_menu(user_role):
    clear_display()
    st.sidebar.title("Navigation")
    
    if user_role == "Franchisee":
        option = st.sidebar.selectbox("Choose Action", ["Yield Management", "Financial Performance"], key="Franchisee_option_select")
    elif user_role == "Management":
        option = st.sidebar.selectbox("Choose Action", ["Franchise Performance", "Strategic Planning"], key="Management_option_select")
    elif user_role == "Investor":
        option = st.sidebar.selectbox("Choose Action", ["Financial Overview", "Sustainability Impact"], key="Investor_option_select")
    elif user_role == "Technical Staff":
        option = st.sidebar.selectbox("Choose Action", ["Equipment Monitoring", "Maintenance Logs"], key="Technical_Staff_option_select")
    
    if st.button("Select Option", key="option_select_button"):
        st.write("⚠️ - Select Option")
        st.session_state.option = option
        display_content(user_role, option)
    else:
        st.write("press button to advance")

# Display content based on selected option
def display_content(user_role, option):
    clear_display()
    #st.header(f"{st.session_state.user_role} - {st.session_state.option}")
    st.write(f"Displaying content for {st.session_state.user_role} & {st.session_state.option}.")
    
    if user_role == "Franchisee":
        if option == "Yield Management":
            st.write("⚠️ - Yield Management feature to be implemented here")
        elif option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here")
    if user_role == "Management":
        if option == "Financial Performance":
            st.write("⚠️ - Financial Performance feature to be implemented here")
        elif option == "Strategic Planning":
            st.write("⚠️ - Strategic Planning feature to be implemented here")
    elif user_role == "Investor":
        if option == "Financial Overview":
            st.write("⚠️ - Financial Overview feature to be implemented here")
        elif option == "Sustainability Impact":
            st.write("⚠️ - Sustainability Impact feature to be implemented here")
    elif user_role == "Technical Staff":
        if option == "Equipment Monitoring":
            st.write("⚠️ - Equipment Monitoring feature to be implemented here")
        elif option == "Monitoring Logs":
            st.write("⚠️ - Monitoring Logs feature to be implemented here")
    
    if st.button("Return to Dashboard", key="RTD_select_button"):
        st.session_state.option == None # resets to null
        display_dashboard_internal(user_role)
    else:
        st.write("press button to advance")

# Main app function
# checks & resets

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False # sets off
    if 'clear_screen' not in st.session_state:
        st.session_state.clear_screen = False # set off
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None # sets null
# resets
    clear_display() # reset on
    if not st.session_state.logged_in: 
        login_screen() # presents the login screen
    elif not st.session_state.user_role:
        role_selection_screen() # request a user_role  
    if option == None:
        st.session_state.option = option
        main_menu(user_role) # selects from a choice of options for a given user_role   
    else:
        user_role = st.session_state.user_role
        option = st.session_state.option
        display_dashboard_internal(user_role) # defaults to current user role dashboard

# Run app
if __name__ == "__main__":
    main()
