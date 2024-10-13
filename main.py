import streamlit as st
existingTasksKey = "existingTasks"
inputFieldKey = "newTaskInputField"
# Initialize session state for tasks if not already initialized
if existingTasksKey not in st.session_state:
    st.session_state[existingTasksKey] = []

# Function to add a task
def add_task():
    new_task = st.session_state[inputFieldKey]
    if new_task:  # Check if the input is not empty
        st.session_state[existingTasksKey].append(new_task)  # Add the task to the list
        del st.session_state[inputFieldKey]
    else:
        st.error("Input can't be empty")  # Show error if the input is empty

# Title
numberOfExistingTasks = len(st.session_state[existingTasksKey])
st.title(f"You have {numberOfExistingTasks} tasks.")

# Display the tasks
if numberOfExistingTasks>0:
    st.subheader('Your Tasks:')
if st.session_state[existingTasksKey]:
    for i, task in enumerate(st.session_state[existingTasksKey]):
        st.write(f"{i + 1}. {task}")


# Input box to enter a new task
st.text_input('Enter a new task', key=inputFieldKey, on_change=add_task)
# Button to add a task with a callback to trigger the function
st.button('Add Task', on_click=add_task)
