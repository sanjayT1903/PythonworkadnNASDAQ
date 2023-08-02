import gspread
import pandas as pd

SHEET_ID = '//not here'
SHEET_NAME = 'Sheet1'
gc = gspread.service_account('creds.json')
spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet(SHEET_NAME)

print(worksheet.cell(3,12).value) #second value is x/letter value 


#rows = worksheet.get_all_records()
#print(rows[:5])

#print('==============================')
#df = pd.DataFrame(rows)
#print(df.head())
