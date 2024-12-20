import pandas
nato_alphabet_file_data = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabet = {row.letter: row.code for (index, row) in nato_alphabet_file_data.iterrows()}

user_input = input('Your word:\n')

print([alphabet[letter] for letter in user_input.upper()])

