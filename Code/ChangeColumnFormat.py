import openpyxl

def ModifyExcel(FilePath,SheetName,ColumnName):
# Load the Excel workbook
    workbook = openpyxl.load_workbook(FilePath)

# Select the sheet you want to work with
    sheet = workbook[SheetName]   # Replace 'Sheet1' with the name of your sheet

# Choose the column you want to format (let's say it's column M)
    column_to_format = ColumnName

# Define a custom number format to treat all values as text
    text_format = openpyxl.styles.numbers.FORMAT_TEXT

# Apply the custom number format to the entire column
    for cell in sheet[column_to_format]:
        cell.number_format = text_format

# Save the changes back to the same Excel file
    workbook.save(FilePath)
