import subprocess
from tkinter import messagebox
import pathlib
import shutil
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import current_date
import clearfields
import openwindow
import write_column_to_excel
import save_data_to_excel
import registration_no_calculator
import search_student_data
import check_empty
import save_edited_data
import deletestudent


lightgray = 'lightgray'
light_gray = '%s' % lightgray
black_color = 'black'
white_color = '#faf8f1'
label_font_size = 12
head_font_size = 12

root = Tk()
root.config(background="#edeade")
root.title('Student registration')
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry('%dx%d' % (window_width, window_height))
write_column_to_excel.write_data()
profile_image = None


def exit_program():
    root.destroy()


def clear_input():
    clearfields.clean(registration_no, student_name, class_selection_combo, date_of_birth, religion, radio, email,
                      father_name, father_occupation, mother_name, mother_occupation, image_placeholder,
                      current_day_date, from_four_certificate_entry, b_certificate_entry)


def upload_function():
    global profile_image
    profile_image = openwindow.file_opened(image_placeholder)


def save_data():
    try:                        
        save_data_to_excel.write(registration_no, current_day_date, student_name, class_selection_combo, date_of_birth,
                                 religion, radio, email, father_name, father_occupation, mother_name,
                                 mother_occupation, profile_image, b_certificate, form_four_certificate)
    
    except NameError or TclError:
        check_empty.check_empty_fields(registration_no, current_day_date, student_name, class_selection_combo,
                                       date_of_birth, religion, radio, email, father_name, father_occupation,
                                       mother_name, mother_occupation, image_placeholder)
    

def search_function():
    search_student_data.search_data(search_value, registration_no, current_day_date, student_name,
                                    class_selection_combo, date_of_birth, religion, radio, email, father_name,
                                    father_occupation, mother_name, mother_occupation, image_placeholder,
                                    from_four_certificate_entry, b_certificate_entry)
               

def update_function():
    save_edited_data.write(registration_no, current_day_date, student_name, class_selection_combo, date_of_birth,
                           religion, radio, email, father_name, father_occupation, mother_name, mother_occupation,
                           profile_image, b_certificate, form_four_certificate, registration_no_entry,
                           from_four_certificate_entry, b_certificate_entry)


def flip_window():
    certificate_frame = Frame(root, bg='#faf8f1', bd=0, width=window_width, height=window_height)
    certificate_frame.grid(row=0, column=0)

    button_frame = Frame(certificate_frame, bg='#faf8f1', width=window_width)
    button_frame.grid(row=0, column=0)

    def delete_frame():
        certificate_frame.destroy()

    button = Button(button_frame, text='Back', bd=0, fg=black_color, bg=white_color, highlightthickness=2,
                    highlightbackground='#0081b4', activebackground='#0081b4', activeforeground='white',
                    font='bold', relief=GROOVE, cursor='hand2', command=delete_frame)
    button.grid(row=0, column=0)

    birth_certificate_path = b_certificate.get()
    from_four_certificate_path = form_four_certificate.get()

    flip_main_frame = Frame(certificate_frame, bg='#faf8f1')
    flip_main_frame.grid(row=1, column=0)

    birth_heading = Label(flip_main_frame, text='Birth Certificate Image', bg='#faf8f1', fg=black_color, font=('yu gothic ui', 20))
    birth_heading.grid(row=0, column=0, padx=20)

    heading = Label(flip_main_frame, text='Form Four Certificate Image', bg='#faf8f1', fg=black_color, font=('yu gothic ui', 20))
    heading.grid(row=0, column=1, padx=20)

    pic_width = round(window_width/3)
    pic_height = round(window_height/1.3)

    l_frame = Frame(flip_main_frame, bg='#edeade', width=window_width/3, height=window_height/1.3)
    l_frame.grid(row=1, column=0, padx=pic_width/4, pady=pic_height/30)

    if birth_certificate_path:
        photo_path = pathlib.Path(birth_certificate_path)
        if photo_path.exists():
            birth_certificate_img = Image.open(birth_certificate_path)
            resized_birth = birth_certificate_img.resize((pic_width, pic_height))
            final_birth_image = ImageTk.PhotoImage(resized_birth)
            birth_image_label = Label(l_frame, bg=white_color, image=final_birth_image)
            birth_image_label.place(x=0, y=0)
            birth_image_label.image = final_birth_image

    r_frame = Frame(flip_main_frame, bg='#edeade', width=window_width/3, height=window_height/1.3)
    r_frame.grid(row=1, column=1, padx=pic_width/4)

    if from_four_certificate_path:
        photo1_path = pathlib.Path(from_four_certificate_path)
        if photo1_path.exists():
            form_four_certificate_img = Image.open(from_four_certificate_path)
            resized_certificate = form_four_certificate_img.resize((pic_width, pic_height))
            final_certificate = ImageTk.PhotoImage(resized_certificate)
            certificate_label = Label(r_frame, bg=white_color, image=final_certificate)
            certificate_label.image = final_certificate
            certificate_label.place(x=0, y=0)


def download_certificate():
    try:
        reg_number = registration_no.get()
        file_path = f'./form_four_certificate/student_{str(reg_number)}_form_four_certificate.jpg'
        download_path = str(pathlib.Path.home() / "Downloads")
        shutil.copy(file_path, download_path)
        messagebox.showinfo('Complete', 'Complete')
    except FileNotFoundError:
        messagebox.showwarning('error', 'File not available')


def download_birth_certificate():
    try:
        reg_number = registration_no.get()
        file_path = f'./birth_certificates/student_{str(reg_number)}_birth_certificate.jpg'
        download_path = str(pathlib.Path.home() / "Downloads")
        shutil.copy(file_path, download_path)
        messagebox.showinfo('Complete', 'Complete')
    except FileNotFoundError:
        messagebox.showwarning('error', 'File not available')


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('JPG Files', '*.jpg')])
    if file:
        file_path = os.path.abspath(file.name)
        from_four_certificate_entry.config(state='normal')
        from_four_certificate_entry.delete(0, END)
        from_four_certificate_entry.insert(0, file_path)


def open_file1():
    file = filedialog.askopenfile(mode='r', filetypes=[('JPG Files', '*.jpg')])
    if file:
        file_path = os.path.abspath(file.name)
        b_certificate_entry.config(state='normal')
        b_certificate_entry.delete(0, END)
        b_certificate_entry.insert(0, file_path)


def backup_data():
    value = messagebox.askyesno('Backup', 'Are you sure you want to backup everything!')
    if value:
        file_path = str(pathlib.Path.home() / 'Desktop')
        path = pathlib.Path(file_path + '/backup')
        if path.exists():
            pass
        else:
            os.mkdir(file_path + '/backup')
        full_path = file_path + '/backup'
        subprocess.call(['cp', '-r', 'birth_certificates', 'form_four_certificate', 'student_images', 'documents',
                         full_path])
        messagebox.showinfo('success', 'Backup complete !')


def delete_student():
    deletestudent.delete(registration_no, registration_no_entry)


# ==================== top frame ============================#
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.config(relief=FLAT, bd=0)
menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='Save', command=save_data)
file_menu.add_command(label='Update', command=update_function)
file_menu.add_command(label='Clear', command=clear_input)
file_menu.add_command(label='Delete', command=delete_student)
file_menu.add_command(label='Exit', command=root.quit)

upload_menu = Menu(menu)
menu.add_cascade(label='Upload', menu=upload_menu)
upload_menu.add_command(label='Upload Photo', command=upload_function)
upload_menu.add_command(label='Upload O level certificate', command=open_file)
upload_menu.add_command(label='Upload birth certificate', command=open_file1)

download_menu = Menu(menu)
menu.add_cascade(label='Download', menu=download_menu)
download_menu.add_command(label='Download O level certificate', command=download_certificate)
download_menu.add_command(label='Download birth certificate', command=download_birth_certificate)
download_menu.add_command(label='BackUp', command=backup_data)

flip_image = Image.open('./images/certificate.png')
resized_image = flip_image.resize((35, 35))
final_flip_img = ImageTk.PhotoImage(resized_image)

flip_button = Button(root, image=final_flip_img, bd=0, bg='#edeade', highlightthickness=0, relief=GROOVE,
                     cursor='hand2', command=flip_window, width=33, height=30)
flip_button.image = final_flip_img
flip_button.place(relx=0.75, rely=0.01, relwidth=0.03, relheight=0.06)

search_value = IntVar()
search_entry = Entry(root, bg=white_color, fg=black_color, width=13, textvariable=search_value, bd=0,
                     highlightcolor='blue', highlightthickness=2, highlightbackground='#0081b4',
                     font=('yu gothic ui', label_font_size))
search_entry.delete(0, END)
search_entry.place(relx=0.785, rely=0.02, relwidth=0.1, relheight=0.04)

# search_img = Image.open('./images/search.png')
# rez_img = search_img.resize((19, 19))
# final_img = ImageTk.PhotoImage(rez_img)

search_button = Button(root, text='Search', bd=0, highlightthickness=2, width=17, height=17,
                       command=search_function, bg=white_color, fg=black_color, highlightbackground='#0081b4',
                       cursor='hand2')
search_button.place(relx=0.89, rely=0.02, relwidth=0.07, relheight=0.04)

# ================== registration no ============================
registration_no_label = Label(root, text='Registration No', fg=black_color, bg='#edeade',
                              font=('yu gothic ui', label_font_size))
registration_no_label.place(relx=0, rely=0.02, relwidth=0.15, relheight=0.04)

reg_no = registration_no_calculator.reg_no_calc()
registration_no = IntVar()
registration_no_entry = Entry(root, fg=black_color, state='disabled', bd=0, highlightcolor='blue',
                              highlightthickness=1, highlightbackground='#0081b4', textvariable=registration_no,
                              font=('yu gothic ui', label_font_size))
registration_no.set(reg_no)
registration_no_entry.place(relx=0.15, rely=0.02, relwidth=0.15, relheight=0.04)

# ======================== date ==============================

date_label = Label(root, text='Date', fg=black_color, bg='#edeade', font=('yu gothic ui', label_font_size))
date_label.place(relx=0.45, rely=0.02, relwidth=0.1, relheight=0.04)

current_day_date = StringVar()
date_entry = Entry(root, bg=white_color, fg=black_color, bd=0, highlightcolor='blue', highlightthickness=1,
                   highlightbackground='#0081b4', textvariable=current_day_date,
                   font=('yu gothic ui', label_font_size))
current_day_date.set(current_date.todays_date())
date_entry.place(relx=0.55, rely=0.02, relwidth=0.15, relheight=0.04)

# ================== student frame ============================
left_frame = LabelFrame(master=root, text='Student Details', bg=white_color, fg=black_color, bd=0, highlightthickness=2,
                        font=('yu gothic ui',))
left_frame.place(relx=0.01, rely=0.1, relwidth=0.7, relheight=0.55)

student_name_label = Label(left_frame,  text='Student Name', fg=black_color, bg=white_color,
                           font=('yu gothic ui', label_font_size))
student_name_label.place(relx=0, rely=0.04, relwidth=0.2, relheight=0.04)

student_name = StringVar()
student_name_entry = Entry(left_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue',
                           highlightthickness=1, highlightbackground='#0081b4', textvariable=student_name,
                           font=('yu gothic ui', label_font_size))
student_name_entry.focus()
student_name_entry.place(relx=0.2, rely=0.02, relwidth=0.4, relheight=0.08)

class_selection_label = Label(left_frame, text='Level', bg=white_color, fg=black_color,
                              font=('yu gothic ui', label_font_size))
class_selection_label.place(relx=0.6, rely=0.035, relwidth=0.2, relheight=0.06)

class_selection_combo = Combobox(left_frame, values=['Level 4/1', 'Level 4/2', 'Level 5/3', 'Level 5/4', 'Level 6/5',
                                                      'Level 6/6'], width=20, font=('yu gothic ui', label_font_size))
class_selection_combo.set('Level 4/1')
class_selection_combo.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.08)

date_of_birth_label = Label(left_frame, text='Date of Birth', bg=white_color, fg=black_color,
                            font=('yu gothic', label_font_size))
date_of_birth_label.place(relx=0, rely=0.21, relwidth=0.2, relheight=0.06)

date_of_birth = StringVar()
date_of_birth_entry = Entry(left_frame, fg=black_color, bg=white_color, bd=0, highlightcolor='blue',
                            highlightthickness=1, highlightbackground='#0081b4', textvariable=date_of_birth,
                            font=('yu gothic ui', label_font_size))
date_of_birth_entry.place(relx=0.2, rely=0.2, relwidth=0.4, relheight=0.08)

religion_label = Label(left_frame, text='Phone', fg=black_color, bg=white_color,
                       font=('yu gothic ui', label_font_size))
religion_label.place(relx=0.6, rely=0.21, relwidth=0.2, relheight=0.06)

religion = StringVar()
religion_entry = Entry(left_frame, fg=black_color, bg=white_color, bd=0, highlightcolor='blue', highlightthickness=1,
                       highlightbackground='#0081b4', textvariable=religion, font=('yu gothic ui', label_font_size))
religion_entry.place(relx=0.78, rely=0.2, relwidth=0.2, relheight=0.08)

gender_label = Label(left_frame, text='Gender', fg=black_color, bg=white_color, font=('yu gothic ui', label_font_size))
gender_label.place(relx=0.6, rely=0.4, relwidth=0.2, relheight=0.06)

radio = IntVar()
radio_one_male = Radiobutton(left_frame, text='Male', variable=radio, value=1, bg=white_color, fg=black_color,
                             activeforeground=black_color, font=('yu gothic', label_font_size), highlightthickness=0,
                             activebackground=white_color)
radio_one_male.place(relx=0.75, rely=0.4, relwidth=0.1, relheight=0.06)

radio_one_female = Radiobutton(left_frame, text='Female', variable=radio, value=2, bg=white_color, fg=black_color,
                               activeforeground=black_color,font=('yu gothic', label_font_size), highlightthickness=0,
                               activebackground=white_color)
radio_one_female.place(relx=0.87, rely=0.4, relwidth=0.12, relheight=0.06)

email_label = Label(left_frame, text='Email', fg=black_color, bg=white_color, font=('yu gothic ui', label_font_size))
email_label.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.08)

email = StringVar()
email_entry = Entry(left_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue', highlightthickness=1,
                    highlightbackground='#0081b4', font=('yu gothic ui', label_font_size), textvariable=email)
email_entry.place(relx=0.2, rely=0.4, relwidth=0.4, relheight=0.08)

b_certificate = StringVar()
b_certificate_entry = Entry(left_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue', width=35,
                            highlightthickness=1, highlightbackground='#0081b4', font=('yu gothic ui', label_font_size),
                            textvariable=b_certificate)
b_certificate_entry.place(relx=0.01, rely=0.59, relwidth=0.59, relheight=0.08)

b_certificate_button = Button(master=left_frame, text='Birth certificate', bg=white_color, fg=black_color,
                              command=open_file1, highlightthickness=2, highlightbackground='#0081b4', bd=0)
b_certificate_button.place(relx=0.61, rely=0.59, relwidth=0.2, relheight=0.08)

form_four_certificate = StringVar()
from_four_certificate_entry = Entry(left_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue',
                                    highlightthickness=1, highlightbackground='#0081b4', width=28,
                                    font=('yu gothic ui', label_font_size), textvariable=form_four_certificate)
from_four_certificate_entry.place(relx=0.01, rely=0.78, relwidth=0.59, relheight=0.08)

from_four_certificate_button = Button(master=left_frame, text='Form four certificate', fg=black_color, bg=white_color,
                                      command=open_file, highlightthickness=2, highlightbackground='#0081b4', bd=0)
from_four_certificate_button.place(relx=0.61, rely=0.78, relwidth=0.2, relheight=0.08)

# ================== parent frame =====================================
parent_frame = LabelFrame(root, text='Parent Details', bg=white_color, fg=black_color,
                          font=('yu gothic ui',), highlightthickness=2, bd=0)
parent_frame.place(relx=0.01, rely=0.68, relwidth=0.7, relheight=0.3)

# ================== parent labels, entry ============================
father_name_label = Label(parent_frame, text='Father\'s Name', bg=white_color, fg=black_color,
                          font=('yu gothic ui', label_font_size))
father_name_label.place(relx=0, rely=0.13, relwidth=0.2, relheight=0.1)

father_name = StringVar()
father_name_entry = Entry(parent_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue', highlightthickness=1,
                          highlightbackground='#0081b4', textvariable=father_name,
                          font=('yu gothic ui', label_font_size))
father_name_entry.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.15)

father_occupation_label = Label(parent_frame, text='Phone', font=('yu gothic ui', label_font_size), bg=white_color,
                                fg=black_color)
father_occupation_label.place(relx=0.6, rely=0.13, relwidth=0.2, relheight=0.1)

father_occupation = StringVar()
father_occupation_entry = Entry(parent_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue',
                                highlightthickness=1, highlightbackground='#0081b4', textvariable=father_occupation,
                                font=('yu gothic ui', label_font_size))
father_occupation_entry.place(relx=0.76, rely=0.1, relwidth=0.22, relheight=0.15)

mother_name_label = Label(parent_frame, text='Mother\'s Name', bg=white_color, fg=black_color,
                          font=('yu gothic ui', label_font_size))
mother_name_label.place(relx=0, rely=0.39, relwidth=0.2, relheight=0.1)

mother_name = StringVar()
mother_name_entry = Entry(parent_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue', highlightthickness=1,
                          highlightbackground='#0081b4', textvariable=mother_name,
                          font=('yu gothic ui', label_font_size))
mother_name_entry.place(relx=0.2, rely=0.39, relwidth=0.4, relheight=0.15)

mother_occupation_label = Label(parent_frame, text='Gardian\'s Name', font=('yu gothic ui', label_font_size),
                                bg=white_color, fg=black_color)
mother_occupation_label.place(relx=0, rely=0.7, relwidth=0.2, relheight=0.1)

mother_occupation = StringVar()
mother_occupation_entry = Entry(parent_frame, bg=white_color, fg=black_color, bd=0, highlightcolor='blue',
                                highlightthickness=1, highlightbackground='#0081b4', textvariable=mother_occupation,
                                font=('yu gothic ui', label_font_size))
mother_occupation_entry.place(relx=0.2, rely=0.7, relwidth=0.4, relheight=0.15)


# ==================== image placeholder ==============================
img = Image.open('images/person.png')
resized_img = img.resize((248, 248))
photo_img = ImageTk.PhotoImage(resized_img)
image_placeholder = Label(root, compound=LEFT, image=photo_img, bd=0, bg='#edeade')
image_placeholder.place(relx=0.75, rely=0.1, relwidth=0.205, relheight=0.425)

# ==================== buttons ==============================
upload_photo_button = Button(root, text='Upload Photo', fg=black_color, bg=white_color,
                             font=('yu gothic ui', label_font_size), width=20, bd=0, highlightthickness=2,
                             highlightbackground='blue', activebackground='blue', activeforeground=white_color,
                             command=upload_function)
upload_photo_button.place(relx=0.75, rely=0.6, relwidth=0.205, relheight=0.06)

save_button = Button(root, text='Save', fg=black_color, font=('yu gothic ui', label_font_size),
                     bg=white_color, width=20, bd=0, highlightthickness=2, highlightbackground='green',
                     activebackground='green', activeforeground=white_color, command=save_data)
save_button.place(relx=0.75, rely=0.7, relwidth=0.205, relheight=0.06)

reset_button = Button(root, text='Clear', fg=black_color, font=('yu gothic ui', label_font_size),
                      bg=white_color,width=20, bd=0, highlightthickness=2, highlightbackground='brown',
                      activebackground='brown', activeforeground=white_color, command=clear_input)
reset_button.place(relx=0.75, rely=0.8, relwidth=0.205, relheight=0.06)

exit_button = Button(root, text='Exit', fg=black_color, bg=white_color,
                     font=('yu gothic ui', label_font_size), width=20, bd=0, highlightbackground='red',
                     highlightthickness=2, activebackground='red', activeforeground=white_color, command=exit_program)
exit_button.place(relx=0.75, rely=0.9, relwidth=0.205, relheight=0.06)

root.mainloop()
