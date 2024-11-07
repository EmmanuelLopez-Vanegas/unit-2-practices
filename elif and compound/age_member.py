ask = int(input('How old are you?'))
ask1 = input('Are you a member (yes/no)?')
if ask >= 18 and ask1 == 'yes':
    print('Acces Granted: You are a member')
elif ask >= 18 and ask1 == 'no':
    print('Access Granted: Please consider becoming a member')
elif ask < 18:
    print('Access Denied: you must be 18 or older')
else:
    print('invalid input')