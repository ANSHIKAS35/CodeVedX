import streamlit as st
import joblib

# Model load
model = joblib.load("model/model.pkl")

st.title("🎓 Student Performance Prediction System")
import pandas as pd

df = pd.read_csv("student.csv")   # agar data folder me hai to "data/student.csv"

st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(df))

with col2:
    st.metric("Average Marks", round(df["FinalMarks"].mean(), 2))

with col3:
    st.metric("Highest Marks", df["FinalMarks"].max())
st.subheader("Student Dataset")

st.dataframe(df)
st.subheader("Final Marks")

st.bar_chart(df["FinalMarks"])
st.subheader("Study Hours vs Marks")

chart = df[["StudyHours", "FinalMarks"]]

st.line_chart(chart)
import matplotlib.pyplot as plt

pass_students = len(df[df["FinalMarks"] >= 40])
fail_students = len(df[df["FinalMarks"] < 40])

fig, ax = plt.subplots()

ax.pie(
    [pass_students, fail_students],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%"
)

st.pyplot(fig)

attendance = st.number_input("Attendance (%)", min_value=0, max_value=100)
study_hours = st.number_input("Study Hours", min_value=0.0)
assignment = st.number_input("Assignment Marks", min_value=0, max_value=100)
previous_marks = st.number_input("Previous Marks", min_value=0, max_value=100)

if st.button("Predict"):

    prediction = model.predict([[attendance, study_hours, assignment, previous_marks]])

    marks = prediction[0]

    st.success(f"Predicted Final Marks: {marks:.2f}")

    # Grade
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "Fail"

    st.write("Grade:", grade)
    if marks >= 40:
        st.success("Result: PASS ✅")
    else:
        st.error("Result: FAIL ❌")
    if marks >= 80:
        st.success("Risk Level: Low 🟢")
    elif marks >= 60:
        st.warning("Risk Level: Medium 🟡")
    else:
        st.error("Risk Level: High 🔴")