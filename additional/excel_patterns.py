''' 
openpyxl 
'''
import openpyxl
import datetime    
wb = openpyxl.load_workbook(filename = "filename.xlsx")  # open existing table
wb = openpyxl.Workbook()                            # create new table
sheet = wb.active                                   # grab the sheet
article = sheet['A1'].value                         # grab the value
sheet["A1"] = 42                                    # insert the value
wb.save('new_table.xlsx')                           # save table      
ws['A2'] = datetime.datetime.now()                  # all types will be automatically converted



''' 
xlwings (best for photos)
'''
import xlwings
filepath = "filename.xlsx"
wb = xlwings.Book(filepath)
sheet = wb.active
article = sheet.range("A1").value
sheet.range("A1").value = "text"



''' 
Google spreadsheets
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

json_file = ""  # json file of account (https://github.com/burnash/gspread/blob/master/README.md)
url = ""    # url to the spreadsheet

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)
wb = gc.open_by_url(url)
sheets = wb.worksheets()
for sheet_open in sheets:
    sheet = wb.worksheet(sheet_open.title)
    matrix = sheet.get_all_values()  # we get all values on the list
# do smth with matrix
