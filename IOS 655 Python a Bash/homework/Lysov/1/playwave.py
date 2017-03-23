#!/usr/bin/env python3

required_libs = ['pyaudio', 'wave']

try:
    import pyaudio
    import wave
    import os

except ImportError:
        print("One of the required libraries is missing: {0}".format(required_libs), flush = True)

class playwave:
    """ This class allows to play '.wav' files synchronously.
    """
    pass

    @property
    def canPlay(self):
        """ canPlay property allows to check if the file can be played.
        """
        return self.__canPlay

    def play(self, filename):
        """ Plays '.wav' file.
        """

        if not os.path.exists(filename):
            print("Audio file {0} does not exists.".fomat(filename), flush = True)
            return False

        try:
            self.__wavefile = wave.open(filename, 'rb')

            # open stream
            stream = self.__pa.open( format = self.__pa.get_format_from_width(self.__wavefile.getsampwidth()),
                            channels = self.__wavefile.getnchannels(),
                            rate = self.__wavefile.getframerate(),
                            output = True)

            # read data
            data = self.__wavefile.readframes(1024)

            # play stream
            while len(data) > 0:
                stream.write(data)
                data = self.__wavefile.readframes(1024)

            # stop stream
            stream.stop_stream()
            stream.close()

        except NameError: return False
        except AttributeError: return False

        return True


    def __init__(self):
        """ Instantiates pyaudio.
        """
        self.__canPlay = False

        # instantiate PyAudio
        try:
            self.__pa = pyaudio.PyAudio()
           
            if (self.__pa is not None):
               self.__canPlay = True
               
        except NameError: pass
        except AttributeError: pass


    def __del__(self):
        """ Terminates pyaudio.
        """
        try:
            if (self.__pa is not None):
                self.__pa.terminate()

        except NameError: pass
        except AttributeError: pass


