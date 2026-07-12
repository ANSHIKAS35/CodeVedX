import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n====== UTILITY USAGE PREDICTION TOOL ======")
    print("1. Add Usage Data")
    print("2. View Usage Data")
    print("3. Update Usage Data")
    print("4. Predict Usage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- ADD DATA ----------------
    if choice == "1":
        month = input("Enter Month: ")

        try:
            units = int(input("Enter Units Used: "))
        except ValueError:
            print("Units must be a number!")
            continue

        with open("usage.csv", "a") as file:
            file.write(f"{month},{units}\n")

        print("Data Saved Successfully!")

    # ---------------- VIEW DATA ----------------
    elif choice == "2":
        try:
            with open("usage.csv", "r") as file:
                print("\n------ Usage Data ------")

                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 2:
                        print(data[0], ":", data[1])

        except FileNotFoundError:
            print("usage.csv file not found!")

    # ---------------- UPDATE DATA ----------------
    elif choice == "3":
        month = input("Enter Month to Update: ")

        try:
            new_units = int(input("Enter New Units: "))
        except ValueError:
            print("Units must be a number!")
            continue

        try:
            with open("usage.csv", "r") as file:
                lines = file.readlines()

            with open("usage.csv", "w") as file:
                for line in lines:
                    data = line.strip().split(",")

                    if data[0] == "Month":
                        file.write(line)

                    elif data[0].lower() == month.lower():
                        file.write(f"{month},{new_units}\n")

                    else:
                        file.write(line)

            print("Data Updated Successfully!")

        except FileNotFoundError:
            print("usage.csv file not found!")

    # ---------------- PREDICT USAGE (ML) ----------------
    elif choice == "4":

        try:
            df = pd.read_csv("usage.csv")

            if len(df) < 2:
                print("Please add at least 2 records for prediction.")

            else:
                X = [[i + 1] for i in range(len(df))]
                y = df["Units"]

                model = LinearRegression()
                model.fit(X, y)

                next_month = [[len(df) + 1]]

                prediction = model.predict(next_month)

                print(f"\nPredicted Next Month Usage: {prediction[0]:.2f} Units")

        except FileNotFoundError:
            print("usage.csv file not found!")

        except Exception as e:
            print("Error:", e)

    # ---------------- EXIT ----------------
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please enter 1 to 5.")