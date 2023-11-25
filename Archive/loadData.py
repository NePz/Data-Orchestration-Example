# Function for data loading
def load_data():
    # Simulating data loading
    with open('transformed_data.csv', 'r') as file:
        data = file.read()
        print("Loaded data:")
        print(data)

    print("Data loading completed.")
