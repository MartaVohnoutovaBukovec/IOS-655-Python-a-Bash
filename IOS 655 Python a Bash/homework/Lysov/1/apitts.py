#!/usr/bin/env python3

# There is only one function in a class
# but it could be extended and reused for other projects

required_libs = ['requests']

try:
    import requests

except ImportError:
        print("One of the required libraries is missing: {0}".format(required_libs), flush = True)

class apitts:
    """ This class connects to the api tts service to GET text converted to the '.wav' file.
    """
    pass

    def text2wave(self, text, filename):
        """ Creates '.wav' file by sending GET to api.ai tts service.
        """
        
        url = 'https://api.api.ai/v1/tts?v=20150910' # current version is 20150910
        headers = {'Authorization' : 'Bearer 09604c7f91ce4cd8a4ede55eb5340b9d',
                   'Accept-Language' : 'en-US'}

        try:
            __t = text.strip()
            __t = __t.replace(' ','+')
            
        except AttributeError:
            print("Wrong parameter type for 'text'.", flush = True)
            return False
        
        query = '&text=' + __t

        try:
            __r = requests.get(url+query, headers=headers)
            
        except requests.exceptions.ConnectionError as err:
                print ("Connection Error: {}".format(err), flush = True)
                return False
               
        try:
            with open(filename, 'wb') as fd:
                for chunk in __r.iter_content(chunk_size=128):
                    fd.write(chunk)

            fd.close()

        except OSError:
            print("Wrong parameter type for filename.", flush = True)
            return False            
        except NameError: # because of connection error
            fd.close()
            return False
                
        return True


    def __init__(self): pass


    def __del__(self): pass

