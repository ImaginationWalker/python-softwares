from tkinter import filedialog
from PIL import Image, ImageTk
import os


def file_opened(placeholder):
    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), 
             title='Select Image File', filetypes=(('JPG File', '*.jpg'),
                                                   ('PNG File', '*.png'),
                                                   ('JPEG File', '*.jpeg')))
        
        try:
            profile_image = Image.open(filename)
            resized_image = profile_image.resize((248, 248))
            student_image = ImageTk.PhotoImage(resized_image)
            placeholder.config(image=student_image)
            placeholder.image = student_image
        
            return profile_image
        
        except AttributeError or UnboundLocalError:
            pass
    
    except:
        pass        