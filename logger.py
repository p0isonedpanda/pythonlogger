if __name__ == '__main__':
    print('this logger is not meant to be run on it\'s own. please include this in your project instead.')

# 0 = no loging
# 1 = info logging 
# 2 = warning logging
# 3 = error logging
logging = 0

logLevel = {
    1 : "[INFO] ",
    2 : "[WARNING] ",
    3 : "[ERROR] "
}

# call this to set the level of logging in your program
def set_logging(state):
    if state < 0 or state > 3:
        print('[ERROR] you cannot set logging to ' + str(state))
        return
    
    global logging
    logging = state

def log(message, level=1):
    if level <= logging and level > 0:
        print(logLevel[level], end='')
        print(message)
