from datetime import datetime
text = 'Experiment Date 01/28/2005; Time 23::50::13'
dt = datetime.strptime(text, 'Experiment Date %m/%d/%Y, Time %H:%M:%S')
print(dt)