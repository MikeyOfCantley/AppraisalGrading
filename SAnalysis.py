import json
#whole document
i = 0
#entering dictionary values
t = 0
#checking dictionary for entry
u = 0
#total points
total = 0
#NEWLINE
NEWLINE = '\n'
password = 'mimir'

while i < 2:
  choice = input("Type 1 for adding new word and value to dictionary, 2 for checking if a word is in the dictionary and 3 for evaluating a report: ")
  #Adding a new dictionary entry
  if choice == '1':
    passguess = input("Please enter the password: ")
    if passguess == password:
      while t < 1:
        new_key = input("Please enter new word or press 't' to exit: ")
        if new_key == 't':
          break
        new_value = input("Please enter the value for this word: ")
        new_value = float(new_value)
        a_dict = new_key + ' ' + str(new_value) + NEWLINE
        with open("dictionary.txt", "a") as myfile:
          myfile.write(a_dict) 
        print('Entry complete')
  #checking if word is in dictionary
  if choice == '2':
    while u < 1:
      with open('dictionary.txt') as file:
        contents = file.read()
        search_word = input("Please enter the word you want to check is in the dictionary or press u to exit: ")
        if search_word == 'u':
          break
        elif search_word in contents:
          print('word found')
        else:
          print('word not found')        
  if choice == '3':
    #open dictionary
    dictionary = {}
    file = open("dictionary.txt")
    for line in file:
      key, value = line.split()
      dictionary[key] = value
    #open report and split into list of words
    report = open("report.txt").read()
    words = report.split()
    #check the list of words against the dictionary and return value
    for element in words:
      if element in dictionary:
        value = dictionary.get(element)
        value = float(value)
        total += value
    print(total)

