import streamlit as st

# Initialize session state for tasks if not already initialized
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Function to add a task
def add_task():
    new_task = st.session_state['new_task']
    if new_task:  # Check if the input is not empty
        st.session_state['tasks'].append(new_task)  # Add the task to the list
        st.session_state['new_task'] = ''  # Clear the input field
    else:
        st.error("Input can't be empty")  # Show error if the input is empty

# Title
st.title(f"You have {len(st.session_state['tasks'])} tasks.")

# Display the tasks
st.subheader('Your Tasks:')
if st.session_state['tasks']:
    for i, task in enumerate(st.session_state['tasks']):
        st.write(f"{i + 1}. {task}")
else:
    st.write("You have no tasks yet!")

# Input box to enter a new task
st.text_input('Enter a new task', key='new_task', on_change=add_task)


# Button to add a task with a callback to trigger the function
st.button('Add Task', on_click=add_task)
