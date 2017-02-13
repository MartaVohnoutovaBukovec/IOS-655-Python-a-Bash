# ch09_05.py
# custom error


class MySimpleError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return repr(str(self.code) + ":" + self.message)

    def save_to_database(self):
        print('save this error into database..')


# how to use custom error
try:
    print('demo custom error')
    print('raise error now')
    raise MySimpleError(100,'This is custom error')

except MySimpleError as e:
    print(e)
    e.save_to_database()

