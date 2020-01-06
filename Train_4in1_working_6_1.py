import requests
from bs4 import BeautifulSoup
import smtplib




# ------------------- E-mail list ------------------------
toAddress = ['nipa23pandya@gmail.com','neepa.pandya@cydar.co.uk']
# --------------------------------------------------------
page =requests.get("https://www.thameslinkrailway.com/travel-information/plan-your-journey/service-updates")
soup =BeautifulSoup(page.content, 'html.parser')
#print(soup)
#period = tonight.find(class_ ="period-name").get_text()
#seven_day = soup.find(id ="seven-day-forecast")
dirty_text ={}
seven_day =soup.find_all(class_ ="o-layout__left@lg o-grid__item@lg")
print(seven_day)
conn = smtplib.SMTP ( 'smtp.gmail.com' , 587 )  # smtp address and port
conn.ehlo ()  # call this to start the connection
conn.starttls ()  # starts tls encryption. When we send our password it will be encrypted.
conn.login ( 'trial0error0@gmail.com' , '0banana0' )
    # conn.sendmail ( 'trial0error0@gmail.com' , toAddress ,'Subject: weather Alert!\n\nAttention!\n\nAware about waether!\n\nCareful!:\nweather notifier' )
    # conn.quit()
report = ""
print ( 'Sent notificaton e-mails for the following recipients:\n' )
print ( toAddress )
dirty_text = '\n'.join([node.get_text() for node in seven_day])
print(dirty_text)
report = '\n'.join([node.get_text() for node in seven_day])
conn.sendmail ( 'trial0error0@gmail.com' , toAddress,"Subject: Train Alert!\n\nAttention!\n\nAware about Train Disturbance!\n{}".format(report))
conn.quit()


# for item in seven_day:
#print ( item.get_text () )
# for item in seven_day:


# #forecast_items = seven_day.find_all(class_ = "tombstone-container")
# # items = seven_day.find_all(class_ = "o-layout@lg o-grid@lg c-combined-messages__title")
# # tonight = items[0]
# # print(items)
# # print(tonight)
# # #print(forecast_items)
# # period = tonight.find(class_ ="o-layout__left@lg o-grid__item@lg").get_text()
# # # # period = forecast_items.find_all(class_ ="o-layout__left@lg o-grid__item@lg").get_text()
# # # # #period = soup.find(".c-disruptions-item__title c-combined-messages__link c-combined-messages__link--disruption .o-layout__left@lg o-grid__item@lg").get_text()
# # print(period)
#
