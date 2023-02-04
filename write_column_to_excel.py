import os
import pathlib
from openpyxl import Workbook


def write_data():
    try:
        excel_file_name = "./documents/Student_Registration_data.xlsx"
        excel_path = pathlib.Path(excel_file_name)
        if excel_path.exists():
            pass

        else:
            os.mkdir('./documents')
            excel_file = Workbook()
            sheet = excel_file.active
            sheet['A1'] = 'Registration No'
            sheet['B1'] = "Name"
            sheet['C1'] = "Class"
            sheet['D1'] = "Gender"
            sheet['E1'] = "DOB"
            sheet['F1'] = "Date Of Registration"
            sheet['G1'] = "Student Phone Number"
            sheet['H1'] = "Email"
            sheet['I1'] = "Father Name"
            sheet['J1'] = "Mother Name"
            sheet['K1'] = "Parent Phone number"
            sheet['L1'] = "Gardian"
    
            excel_file.save(excel_file_name)

    except:
        pass                 
               