import streamlit as st
from PIL import Image
import time

# Set up the app title and layout
st.set_page_config(page_title="Interactive Python Course", layout="wide")

# Sidebar for navigation
st.sidebar.title("Course Navigation")
section = st.sidebar.radio("Go to", ["Introduction", "Variables", "Data Types", "Control Flow", "Functions", "OOP", "File Handling", "DSA", "Quiz", "Feedback"])

# Display Course Image and Introduction
def display_image():
    st.title("Welcome to the Python Interactive Course!")
    st.markdown("""
    ### Learn Python interactively through this course.
    This course covers the essentials of Python programming and engages you with quizzes and examples.
    """)
    image = Image.open('python.png')  # Replace with your image path
    st.image(image, caption='Learn Python', width=400)

def introduction():
    st.header("Introduction to Python")
    st.markdown("""
    Python is a versatile programming language. It's used in web development, data science, artificial intelligence, and more.
    
    In this section, you'll learn:
    - What is Python?
    - History of Python
    - How Python is used in various industries.
    
    Let's dive in!
    """)
    st.header("What is Python?")
    st.markdown("""

    - Python is a general-purpose programming language that's used to build software, websites, and more. 
    - It's also used for data analysis, machine learning, and scientific computing. 
    - Python is known for its simplicity, readability, and ease of use.

        """)

def variables_lesson():
    st.header("Lesson 1: Variables in Python")
    st.markdown("""
    Variables are containers for storing data values. You can create a variable by assigning a value to it using the equals sign (`=`).

    Example:
    ```python
    x = 5
    y = "Hello, World"
    print(x)
    print(y)
    ```

    Variables can store different types of data, including numbers, strings, and more.
    """)

def data_types_lesson():
    st.header("Lesson 2: Data Types")
    st.markdown("""
    Python supports various data types, such as:
    - `int` for integers
    - `float` for decimal numbers
    - `str` for strings
    - `bool` for boolean values (True or False)
    
    Example:
    ```python
    x = 10
    y = 3.14
    name = "Python"
    is_active = True
    ```

    Data types are essential because they determine how data is stored and manipulated in your program.
    """)

def control_flow_lesson():
    st.header("Lesson 3: Control Flow")
    st.markdown("""
    Control flow allows you to control the execution of your code. This includes:
    - `if` statements
    - `for` loops
    - `while` loops

    Example:
    ```python
    x = 10
    if x > 5:
        print("x is greater than 5")
    ```

    Loops allow you to iterate over a sequence of items or repeat code multiple times.
    """)

def functions_lesson():
    st.header("Lesson 4: Functions in Python")
    st.markdown("""
    Functions allow you to encapsulate code that can be reused. You define a function using the `def` keyword.

    Example:
    ```python
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("John"))
    ```

    Functions help organize your code and make it more modular and maintainable.
    """)

def oop_lesson():
    st.header("Lesson 5: Object-Oriented Programming (OOP)")
    st.markdown("""
    OOP is a programming paradigm based on the concept of "objects", which can contain data and code. It allows for concepts like inheritance, encapsulation, and polymorphism.

    Example:
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name
        
        def bark(self):
            return f"{self.name} says Woof!"
    
    my_dog = Dog("Buddy")
    print(my_dog.bark())
    ```

    OOP helps in structuring code efficiently and making it more reusable.
    """)

def file_handling_lesson():
    st.header("Lesson 6: File Handling")
    st.markdown("""
    File handling allows you to read from and write to files in Python.

    Example of writing to a file:
    ```python
    with open('example.txt', 'w') as file:
        file.write("Hello, World!")
    ```

    Example of reading from a file:
    ```python
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
    ```

    File handling is essential for data persistence in applications.
    """)

def dsa_lesson():
    st.header("Lesson 7: Data Structures and Algorithms (DSA)")
    st.markdown("""
    DSA is a way of organizing data to perform operations efficiently. Common data structures include lists, stacks, queues, trees, and graphs.

    Example of using a list:
    ```python
    my_list = [1, 2, 3, 4]
    my_list.append(5)
    print(my_list)  # Output: [1, 2, 3, 4, 5]
    ```

    Understanding DSA is crucial for problem-solving in programming.
    """)

def quiz():
    st.header("Python Quiz")
    st.markdown("Test your knowledge with this interactive quiz!")

    # Question 1
    question_1 = st.radio("1. What is the output of the following code?\n```python\nx = 5\ny = 'Hello'\nprint(x, y)\n```", 
                         ("5 Hello", "Hello 5", "Error"))

    if question_1 == "5 Hello":
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect, try again!")

    # Question 2
    question_2 = st.radio("2. What is the data type of the variable 'name' in the code below?\n```python\nname = 'Python'\n```", 
                         ("int", "float", "str"))

    if question_2 == "str":
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect, try again!")

    # Additional Quiz Question on OOP
    question_3 = st.radio("3. What keyword is used to define a class in Python?", 
                         ("def", "class", "function"))

    if question_3 == "class":
        st.success("Correct! 🎉")
    else:
        st.error("Incorrect, try again!")

def feedback():
    st.header("Feedback Section")
    feedback_text = st.text_area("Please provide your feedback on this course:")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback! 💬")
        time.sleep(1)
        st.balloons()  # Celebration animation for feedback submission

# Routing to sections with loading animation
if section == "Introduction":
    with st.spinner("Loading Introduction..."):
        time.sleep(1)
        display_image()
        introduction()
elif section == "Variables":
    with st.spinner("Loading Variables Lesson..."):
        time.sleep(1)
        variables_lesson()
elif section == "Data Types":
    with st.spinner("Loading Data Types Lesson..."):
        time.sleep(1)
        data_types_lesson()
elif section == "Control Flow":
    with st.spinner("Loading Control Flow Lesson..."):
        time.sleep(1)
        control_flow_lesson()
elif section == "Functions":
    with st.spinner("Loading Functions Lesson..."):
        time.sleep(1)
        functions_lesson()
elif section == "OOP":
    with st.spinner("Loading OOP Lesson..."):
        time.sleep(1)
        oop_lesson()
elif section == "File Handling":
    with st.spinner("Loading File Handling Lesson..."):
        time.sleep(1)
        file_handling_lesson()
elif section == "DSA":
    with st.spinner("Loading DSA Lesson..."):
        time.sleep(1)
        dsa_lesson()
elif section == "Quiz":
    with st.spinner("Loading Quiz..."):
        time.sleep(1)
        quiz()
elif section == "Feedback":
    with st.spinner("Loading Feedback Section..."):
        time.sleep(1)
        feedback()
