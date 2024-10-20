import streamlit as st

# A placeholder user database
users = {
    'admin': 'password123',
    'guest': 'password456',
}

# Placeholder for user roles and other selections
roles = {
    'admin': ['Manager', 'Supervisor', 'CEO'],
    'user1': ['Worker', 'Assistant', 'Operator']
}

actions = ['Action1', 'Action2', 'Action3']
activities = ['Activity1', 'Activity2', 'Activity3']

# Function to clear the screen
def clear_screen():
    st.session_state['clear'] = True
    st.experimental_rerun()

# Function to display the user role options
def display_role_options(user):
    st.write("Select your role:")
    selected_role = st.radio("Role", roles[user])
    if st.button("Next"):
        st.session_state['role'] = selected_role
        clear_screen()

# Function to display the action options
def display_action_options():
    st.write("Select an action:")
    selected_action = st.radio("Action", actions)
    if st.button("Next"):
        st.session_state['action'] = selected_action
        clear_screen()

# Function to display the activity options
def display_activity_options():
    st.write("Select an activity:")
    selected_activity = st.radio("Activity", activities)
    if st.button("Next"):
        st.session_state['activity'] = selected_activity
        clear_screen()

# Function to handle logout
def logout():
    st.session_state.clear()
    st.experimental_rerun()

# Main function to handle user login and navigation
def main():
    if 'role' not in st.session_state:
        # Login logic
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in users and users[username] == password:
                st.session_state['username'] = username
                clear_screen()
            else:
                st.error("Invalid username or password.")
    else:
        if 'role' not in st.session_state:
            display_role_options(st.session_state['username'])
        elif 'action' not in st.session_state:
            display_action_options()
        elif 'activity' not in st.session_state:
            display_activity_options()
        else:
            st.write(f"User Role: {st.session_state['role']}")
            st.write(f"Action: {st.session_state['action']}")
            st.write(f"Activity: {st.session_state['activity']}")
            if st.button("Logout"):
                logout()

# Starting the app
if __name__ == "__main__":
    main()
