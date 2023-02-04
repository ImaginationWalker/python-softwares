from datetime import date


def todays_date():
    today_date = date.today()
    current_date = today_date.strftime('%d/%m/%Y')
    
    return current_date    
    