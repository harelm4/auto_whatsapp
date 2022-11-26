import pywhatkit
import pandas as pd
import math
from datetime import datetime
def send(phone,msg):
    pywhatkit.sendwhatmsg_instantly(phone, msg ,tab_close=True)
    print('sent to {p}'.format(p=phone))
csv=pd.read_csv('x.csv')
lst=[]
msg="""
היי מה נשמע?
נעים מאוד, קוראים לי הראל ואני מוביל קהילה בזיכרון בסלון.
ראיתי שאירחת מפגש של זיכרון בסלון ביום השואה האחרון, מקווה שהיה מפגש משמעותי!
אנחנו מגייסים בימים אלה מתנדבים לזיכרון בסלון בבאר שבע ורציתי להזמין אותך למפגש מתעניינים🙂
המתנדבים שלנו מפעילים את המיזם בעיר ומקדמים את הפעילות למען זיכרון השואה ושורדי השואה
במפגש אתן פרטים נוספים ואסביר הכל.
במידה וזה מעניין אותך , אשמח לאישור בהודעה🤚
ואם כן, אשלח לך את פרטי המפגש בהודעה מסודרת.
מקווה לראות אותך איתנו!

"""
for p in csv['טלפון איש קשר']:
    try:
        lst.append('+'+str(math.floor(p)))
    except:
        continue
print(lst)
# lst=['+9720503603033','+9720503603033']
# for p in lst:
#     send(p,msg)

print(len(lst))

