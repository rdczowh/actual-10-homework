#!/usr/bin/env python
def menu():
    print 'Registration: 1. Landing: 2'
    number = raw_input('Please select the operating:')
    return number

def work(n):
    f = open('userpassword.txt')
    passwd = {}
    for i in f.readlines():
        tmp = i.split(':')
        passwd[tmp[0]] = tmp[1]
    while True:
        if n == str(1):
	    username = raw_input('Registered user name:')
	    if passwd.has_key(username) == True:
	        print 'The user name is registered, please try again'
	        continue
	    password = raw_input('Set the password:')
	    passw = raw_input('Again to confirm password:')
	    if passw != password:
	        print 'sorry! Password error, please try again'
	        continue
	    else:
	        print 'Registration completed!'
	        f = open('userpassword.txt','a+')
	        f.write('%s:%s\n' % (username,password))
	        break
        elif n == str(2):
	    username = raw_input('user:')
	    password = raw_input('password:')
	    if passwd.has_key(username) == True:
	        paw = passwd[username]
	        if password in paw:
	            print 'Oh my god!Login to complete'
		    break
	        else:
		    print 'Sorry, authentication failed'
		    continue
	    else:
	        print 'User name does not exist, please return to register, thank you!'
	        continue
	else:
	    print ' sorry. Input is wrong, please input again.'
	    continue

num = menu()
work(num)
