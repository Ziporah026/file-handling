from PyPDF2 import PdfReader

# Create a PDF reader object and load the PDF file
reader = PdfReader('Python assignment.pdf')

# Print the number of pages in the PDF
print(f'Number of pages: {len(reader.pages)}')

# Read the content of the PDF
page = reader.pages[0]

# Print the text content of the first page of the PDF
text = page.extract_text()
print(text)

# Print the text content of the second page of the PDF
page2 = reader.pages[1]
text = page2.extract_text()
print(text)

# Print the text content of the third page of the pdf
page3 = reader.pages[2]
text = page3.extract_text()
print(text)

# Print the text content of the fourth page of the pdf
page4 = reader.pages[3]
text = page4.extract_text()
print(text)

# Print the text content of the pdf itself
print (f'PDF')





#file = open('Python clearassignment.pdf', 'r') #open file in read mode
#content = file.read()
#print (content)