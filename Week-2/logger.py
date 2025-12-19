#Question #4: user logger

#log file write
def logger(logFile):
    with open(logFile, 'a') as file:
        file.write('User logged in\n')
        
    with open(logFile, 'r') as file:
        print(file.read())
    
logger('log.txt')