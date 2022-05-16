#Time Conversiobr - www.101computing.net/time-conversion/ 

time=input("Enter a time in the hh:mm format (e.g 18:36) ")

hours = int(time[:2])
stand = ''
minutes = time[3:]
if hours == 0:
  stand = str(12) +":"+ minutes +"am"
elif hours <12:
  stand = str(hours)+ ':'+ minutes + 'am'
elif hours == 12:
  stand = str(hours) + ':'+ minutes + 'pm'
else:
  stand = str(hours - 12) + ':' + minutes + 'pm'
print(stand)
