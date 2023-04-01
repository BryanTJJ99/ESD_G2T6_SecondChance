def handleError(data):
    errMsg = ''
    if data['channelID'] == '':
        errMsg = 'Please enter a channel ID for your item'
    elif data['token'] == '':
        errMsg = 'Please enter token for your item'
    return errMsg