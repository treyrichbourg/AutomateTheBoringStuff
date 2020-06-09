#! python3
# regex_search.py opens all .txt files in a folder and searches for any line that mathes a user-supplied regular expression
# The results are printed to the screen

from pathlib import Path
import re, pprint, os
#Prompt user to input a path to be searched
file_path = input("Please enter a path to the folder you want to search:\n")
file_path_obj = Path(file_path)
#print(file_path)
if Path.is_dir(file_path_obj) == True:
    #print('yup')
    #Prompt user to input a regular expression 
    search_criteria = re.compile(input("Enter a regular expression to search for:\n"))

    #text_files = list(file_path_obj.glob('*.txt'))
    text_files = os.listdir(file_path_obj)
    for text_file in text_files:
        if text_file.endswith('.txt'):
            contents = open(file_path_obj / text_file)
            for line in contents.readlines():
                if search_criteria.search(line) in line:
                    print(line)
        


            
    #trial = open(file_path_obj.glob('*.txt'))
    # for text_file in range(len(text_files)):
    #     print(text_files[text_file])
    #pprint.pprint(text_files)

    

else:
    print('Please enter a valid file path.')
#print(file_path)