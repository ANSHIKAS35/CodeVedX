import pandas as pd
df = pd.read_csv("student.csv")
print(df)
print(df.head(5))
print(df.info())
print(df.describe())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Data Visualization
import matplotlib.pyplot as plt

plt.scatter(df["StudyHours"], df["FinalMarks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()  

# Input Features
x = df[["Attendance", "StudyHours", "Assignment", "PreviousMarks"]]

# Predicted Target
y = df["FinalMarks"]

print(x.head())
print(y.head())

#Train
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)

model.fit(X_train, y_train)
# Prediction
predictions = model.predict(X_test)

print("Actual Marks:", list(y_test))
print("Predicted Marks:", predictions)

print("✅ Model Training Complete")
from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

#Model Saving
import joblib

joblib.dump(model, "model/model.pkl")

print("✅ Model Saved Successfully")