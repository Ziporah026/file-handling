file = open('example.txt', 'w')#write file
file.write("This is a test file that contain python") #write test file
file.close#close file

file = open('example.txt', 'r') #read file contents written to file
content = file.read()
print(content)	