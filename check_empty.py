from tkinter import *
import openwindow
import gender_selection
from tkinter import messagebox


def check_empty_fields(registration_no, current_day_date, student, class_selection_combo, date_of_birth, religion, radio, skills, father_name, father_occupation, mother_name, mother_occupation, image_placeholder):
    try:
        try:
            reg_number = registration_no.get() 
        except TclError:
            messagebox.showerror(title='Error', message='Few data is missing\n    Data not saved!')
            
        current_date = current_day_date.get()   
        student_name = student.get()        
        student_class = class_selection_combo.get()
        dob = date_of_birth.get()
        student_religion = religion.get()
        gender = gender_selection.gender_selected(radio)
        student_skills = skills.get()
        fathers_name = father_name.get()
        fathers_occupation = father_occupation.get()
        mothers_name = mother_name.get()
        mothers_occupation = mother_occupation.get()
        
        if (current_date == '' or student_name == '' or dob == '' or student_religion == '' or student_skills == '' or fathers_name == '' or mothers_name == '' or mothers_occupation =='' or student_class == '' or gender == None):
            messagebox.showerror(title='Error', message='Few data is missing\n    Data not saved!')
        
        else:
            messagebox.showerror(title='Error', message='upload Image')
    
    except:
        pass                 
        