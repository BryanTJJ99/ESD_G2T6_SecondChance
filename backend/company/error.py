def handleError(data):
    errMsg = ''
    if data['companyName'] == '':
        errMsg = 'Please enter a valid company name'
    return errMsg