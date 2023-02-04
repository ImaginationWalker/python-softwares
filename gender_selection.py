def gender_selected(radio):
    try:
        gender = radio.get()
        if gender == 1:
            gender = 'Male'
        
        elif gender == 2:
             gender = 'Female'
        
        else:
            gender = None
                            
        return gender
    except:
        pass                 
        