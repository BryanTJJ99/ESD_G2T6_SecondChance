def handleError(data):
    errMsg = ''
    if data['name'] == '':
        errMsg = 'Please enter a name for your item'
    elif data['itemPicture'] == '':
        errMsg = 'Please submit a picture for your item'
    elif data['itemDescription'] == '':
        errMsg = 'Please enter a description for your item'
    elif data['itemCategory'] == '':
        errMsg = 'Please select a category for your item'
    return errMsg