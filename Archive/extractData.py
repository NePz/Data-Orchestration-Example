# Function for data extraction
def extract_data():
    # Simulating data extraction
    with open('source_data.csv', 'w') as file:
        file.write("Player_ID,Player_Name,Goals_Scored,Assists\n")
        file.write("1,John Doe,5,2\n")
        file.write("2,Jane Smith,3,4\n")
        file.write("3,Michael Johnson,2,1\n")
        file.write("4,Emily Davis,4,3\n")
        file.write("5,Chris Wilson,1,2\n")
    print("Data extraction completed.")
