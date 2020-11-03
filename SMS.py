import yagmail
import time

t = time.localtime()
time = time.strftime("%I:%M %p", t)

receiver = '3852313335@pm.sprint.com'
# receiver = 'calebdtest@gmail.com'
# receiver = '8013691583@txt.att.net'

subject = "Tee Hee"
body = "This message was sent from Yagmail at {}".format(time)

attachPath = "/Users/tom/Downloads/tenor.gif"

# yag = yagmail.SMTP({'calebdtest@gmail.com': 'ur mom'})
for t in range(150):
    yag = yagmail.SMTP('calebdtest')
    print("Sending...")
    yag.send(
        to=receiver,
        # subject=subject,
        contents=body,
        # attachments=attachPath
    )
