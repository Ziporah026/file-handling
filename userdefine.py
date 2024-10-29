def read_example_txt():
    with open('example.txt', 'r') as file:
        print(file.read())

def append_note_txt():
    with open('note.txt', 'a') as file: #append text to the end of the file
     text = input('Enter your notes here:')
    file.write(text + "\n")
def read_example_txt():
    with open('example.txt', 'r') as file: 
        print(file.read())