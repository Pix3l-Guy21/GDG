#Question #4: user logger

#log file write
with open('log.txt', 'a') as file:
    file.write('User logged in\n')
    
with open('log.txt', 'r') as file:
    print(file.read())