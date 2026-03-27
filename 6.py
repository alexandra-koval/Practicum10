def check_message(message):
    '''
    Returns the full message if it is less than 160 characters,
    otherwise returns only the first 160 characters
    '''
    return message if len(message) < 160 else message[:160]


msg = input()
print(check_message(msg))
