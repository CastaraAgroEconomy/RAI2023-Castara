# This script creates the base Truth Table to track valid and invalid combinations of options based upon predefined rules

import streamlit as st
import numpy as np

from features.Validation.valid_selection import validate_choice

# Initialize session state variables if not already present
for key, default in {
    'n': 1, 'x': 1, 'm': 1, 'y': 1,
    'selected_role': None, 'selected_sub_role': None,
    'selected_action': None, 'selected_activity': None,
    'self': None, 'R_go': 0
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

class TruthTable:
    def __init__(self, n=14, x=30, m=30, y=35):
        self.n = n
        self.x = x
        self.m = m
        self.y = y
        self.table = np.zeros((n, x, m, y), dtype=int)
        self.generate_table()  # Automatically builds the Truth Table on initialization

    def generate_table(self):
        st.write("⚠️ - Generating Truth Table with predefined validation rules.")
        
        for n in range(self.n):
            for x in range(self.x):
                for m in range(self.m):
                    for y in range(self.y):
                        # Validate each possible combination and update table
                        is_valid = validate_choice(n, x, m, y)
                        self.table[n, x, m, y] = int(bool(is_valid))  # Set to 1 if valid, 0 if not


    def is_valid_combination(self, n, x, m, y):
        return self.table[n, x, m, y] == 1

    def get_next_valid_selection(self, n, x, m, y):
        # Determines the next level with invalid choices and returns it
        if self.table[n, :, :, :].max() == 0:
            return "role"
        elif self.table[n, x, :, :].max() == 0:
            return "sub_role"
        elif self.table[n, x, m, :].max() == 0:
            return "action"
        else:
            return "activity"


# Function to validate selection
def validate_selection(n, x, m, y):
    # Uses the validate_choice function to determine if selection is valid
    is_valid = validate_choice(
        st.session_state.selected_role,
        st.session_state.selected_sub_role,
        st.session_state.selected_action,
        st.session_state.selected_activity
    )
    
    if is_valid:
        st.session_state.R_go = 1
    else:
        st.session_state.R_go = 0
    return is_valid
    

# Initialize the TruthTable
R = TruthTable()

# Example usage
def finalize_selection():
    n, x, m, y = (
        st.session_state.n,
        st.session_state.x,
        st.session_state.m,
        st.session_state.y
    )
    
    if R.is_valid_combination(n, x, m, y):
        st.success("Valid combination!")
    else:
        next_step = R.get_next_valid_selection(n, x, m, y)
        st.error(f"Invalid combination. Please re-select your {next_step}.")