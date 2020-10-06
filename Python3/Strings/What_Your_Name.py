first_name = input()
last_name = input()
if len(first_name) <= 10 and len(last_name) <= 10:
    print("Hello {} {}! You just delved into python.".format(first_name,last_name))