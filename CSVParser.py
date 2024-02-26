import csv

# Path to your source CSV file containing French words
source_csv_path = 'francais.txt'
# Path to the new CSV file to store 5-letter French words
output_csv_path = '5_letter_french_words.csv'

# Function to filter and create the new CSV file
def filter_five_letter_words(source_path, output_path):
    with open(source_path, 'r', newline='', encoding='utf-8') as source_file:
        reader = csv.reader(source_file)
        five_letter_words = [word[0].lower() for word in reader if len(word[0]) == 5 and '-' not in word[0]]

    with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        for word in five_letter_words:
            writer.writerow([word])

# Call the function with your file paths
filter_five_letter_words(source_csv_path, output_csv_path)