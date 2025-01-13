from PyPDF2 import PdfReader

# Load the uploaded PDF file to check if the text is selectable

file_path = "./ww/cv-ww.pdf"

reader = PdfReader(file_path)

# Extract the first page to check for text content

first_page_text = reader.pages[0].extract_text()

print(first_page_text)