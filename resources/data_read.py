from openpyxl import load_workbook

def get_data(file,sheet):
    wb = load_workbook(file)
    sheet = wb[sheet]
    rows = sheet.max_row
    cols = sheet.max_column
    data = []
    row_dict = {}
    headers = [sheet.cell(1,col).value for col in range(1,cols+1)]
    print("headrs: ", headers)
   
    for j in range(2,rows+1):
       row_values = [sheet.cell(j,col).value for col in range(1,cols+1)]

    print("rows: ", row_values)
    row_dict = dict(zip(headers,row_values))
    data.append(row_dict)
    return data



