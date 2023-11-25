# Function for data transformation
def transform_data():
    # Simulating data transformation
    with open('source_data.csv', 'r') as file:
        data = file.readlines()
        transformed_data = ["P_" + row.strip() if idx != 0 else row.strip() for idx, row in enumerate(data)]
    
    with open('transformed_data.csv', 'w') as file:
        file.write('\n'.join(transformed_data))
    print("Data transformation completed.")