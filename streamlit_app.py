import streamlit as st

st.title("Student Marks & Grade Calculator")

subjects = st.number_input("Enter number of subjects", min_value=1, max_value=10, value=5)
marks = []

for i in range(int(subjects)):
    marks.append(st.number_input(f"Enter marks for subject {i+1} (out of 100)", min_value=0, max_value=100))

if st.button("Calculate Result"):
    total = sum(marks)
    percentage = total / (subjects * 100) * 100
    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")
    
    if percentage >= 90:
        st.success("Grade: A+")
    elif percentage >= 75:
        st.info("Grade: A")
    elif percentage >= 60:
        st.info("Grade: B")
    elif percentage >= 50:
        st.warning("Grade: C")
    else:
        st.error("Grade: Fail")
