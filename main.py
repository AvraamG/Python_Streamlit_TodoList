import streamlit as st
existingTasksKey = "existingTasks"
inputFieldKey = "newTaskInputField"
disableOnChangeKey = "disable_on_change"
# Initialize session state for tasks if not already initialized
if existingTasksKey not in st.session_state:
    st.session_state[existingTasksKey] = []
if disableOnChangeKey not in st.session_state:
    st.session_state[disableOnChangeKey] = False

def ClearInputFieldWithoutTriger():
    st.session_state[disableOnChangeKey] = True
    st.session_state[inputFieldKey] = ""
    st.session_state[disableOnChangeKey] = False

# Function to add a task
def AddNewTask():
    if st.session_state[disableOnChangeKey]:
        return
    new_task = st.session_state[inputFieldKey]
    if new_task:  # Check if the input is not empty
        st.session_state[existingTasksKey].append(new_task)  # Add the task to the list
        ClearInputFieldWithoutTriger()


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
inputField = st.text_input('Enter a new task', key=inputFieldKey, on_change=AddNewTask)
# Button to add a task with a callback to trigger the function
st.button('Add Task', on_click=AddNewTask)
