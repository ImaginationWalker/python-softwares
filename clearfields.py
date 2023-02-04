from tkinter import *
from PIL import Image, ImageTk
import registration_no_calculator
import current_date


def clean(registration_no, student_name, class_selection_combo, date_of_birth, religion, radio, skills, father_name,
          father_occupation, mother_name, mother_occupation, image_placeholder, current_day_date,
          from_four_certificate_entry, b_certificate_entry):
    try:
        student_name.set('')
        class_selection_combo.set('Level 4/1')
        date_of_birth.set('')
        religion.set('')
        radio.set(None)
        skills.set('')
        father_name.set('')
        father_occupation.set('')
        mother_name.set('')
        mother_occupation.set('')
        today = current_date.todays_date()
        current_day_date.set(today)
        b_certificate_entry.config(state='normal')
        from_four_certificate_entry.config(state='normal')
        from_four_certificate_entry.delete(0, END)
        b_certificate_entry.delete(0, END)
        
        placeholder_image = Image.open('images/person.png')
        resized_image = placeholder_image.resize((248, 248))
        student_image = ImageTk.PhotoImage(resized_image)
        image_placeholder.config(image=student_image)
        image_placeholder.image = student_image
        
        registration_no.set(registration_no_calculator.reg_no_calc())
        
    except:
        pass                 
        