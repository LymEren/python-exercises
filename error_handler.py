# Handle the received error and save it to the errLog.txt file

from datetime import datetime


def addNumbers(a, b):
    try:
        return a + b
    except Exception as log_err:
        errLog = f'{datetime.now()} - Operation could not be completed, error description: ' + str(log_err) + ".\n"

        # To prevent overwrite, append mode was used instead of write.
        with open('errLog.txt', 'a') as errHandler:
            errHandler.write(errLog)
        return errLog

