from datetime import datetime

now = datetime.now()
name = input('type your name:')
age = int(input('your age:'))
to_be = 100 - age
now = now.year + to_be
print (name,' you will turn 100 in ', now)
