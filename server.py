from flask import Flask
from datetime import datetime, date


app = Flask(__name__)

# date object containing todays date
today = date.today()

# datetime object containing current date and time
now = datetime.now()

# d = date(2002, 12, 31)

def is_weekday():
    """Show homepage"""
    while now : 
        if now.isoweekday() in range(1, 6):
            print ("YAY!! ITS A WEEKDAY")
            if now.hour == 8:
                print("It is 8am on a weekday. I need to send a slack message to say Hi")
            if now.hour == 5:
                print("It is 5pm on a weekday. I need to send a slack message to say Bye")
                    
        else:
            
            print ("ITS A WEEKEND!!") 
            break 
is_weekday()        

 

@app.route('/')
def index():
    """Show homepage"""
    if now.isoweekday() in range(1, 6):
        print ("YAY!! ITS A WEEKDAY", now.hour)
        if now.hour == 8:
            print("It is 8am on a weekday. I need to send a slack message to say Hi")
        if now.hour == 5:
            print("It is 5pm on a weekday. I need to send a slack message to say Bye")
                  
    else:
        print ("ITS A WEEKEND!!")  
        


    print("Today's date:", today.weekday())
    print("now:", now.weekday())
    # Monday is 0 and Sunday is 6: 0-4 are weekdays 
    # print("DATE:", d.weekday())

    return """
    <html>
    <body>
      <h1>I am the landing page</h1>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')