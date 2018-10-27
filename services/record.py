import pyaudio
import wave
import math
import audioop
import time
import logging
from collections import deque
from decorators.profile import profile
#from ctypes import *

class record:
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1    
    RATE = 44000
    THRESHOLD = 1300  # The threshold intensity that defines silence
                  # and noise signal (an int. lower than THRESHOLD is silence).
    SILENCE_LIMIT = 2  # Silence limit in seconds. The max ammount of seconds where
                   # only silence is recorded. When this time passes the
                   # recording finishes and the file is delivered.
    PREV_AUDIO = 1  # Previous audio (in seconds) to prepend. When noise
                  # is detected, how much of previously recorded audio is
                  # prepended. This helps to prevent chopping the beggining
                  # of the phrase.
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "resources/recording.wav"

    @profile
    def record_by_silence(self, threshold=THRESHOLD, num_phrases=1):
        """
        Listens to Microphone, extracts phrases from it and sends it to 
        Google's TTS service and returns response. a "phrase" is sound 
        surrounded by silence (according to threshold). num_phrases controls
        how many phrases to process before finishing the listening process 
        (-1 for infinite). 
        """
        print('loading pyaudio')
        #Open steam
        #SWALLOW PI WARNINGS
        #ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
        
        #def py_error_handler(filename, line, function, err, fmt):
        #   do_nothing = 1

        #c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

        #asound = cdll.LoadLibrary('libasound.so')
        # Set error handler
        #asound.snd_lib_error_set_handler(c_error_handler)
        ## END SWALLOW
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        logging.info('* Listening mic. ')
        audio2send = []
        cur_data = ''  # current chunk  of audio data
        rel = 16000/self.CHUNK#self.RATE/self.CHUNK
        slid_win = deque(maxlen=int(self.SILENCE_LIMIT * rel))
        #Prepend audio from 0.5 seconds before noise was detected
        prev_audio = deque(maxlen=int(self.PREV_AUDIO * rel))
        started = False
        n = num_phrases
        while (num_phrases == -1 or n > 0):
            cur_data = stream.read(self.CHUNK)
            slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
            #print(slid_win[-1])
            print(sum([x > self.THRESHOLD for x in slid_win]))
            if(sum([x > self.THRESHOLD for x in slid_win]) > 0):
                if(not started):
                    logging.debug('Starting record of phrase')
                    started = True
                audio2send.append(cur_data)
            elif (started is True):
                logging.debug('Finished')
                # The limit was reached, finish capture and deliver.
                filename = self.save_speech(list(prev_audio) + audio2send, p)
                # Reset all
                started = False
                slid_win = deque(maxlen=int(self.SILENCE_LIMIT * rel))
                prev_audio = deque(maxlen=int(0.5 * rel) )
                audio2send = []
                n -= 1
            else:
                prev_audio.append(cur_data)

        logging.info('* Done recording')
        stream.close()
        p.terminate()

        return filename


    def audio_int(self, num_samples=50):
        """ Gets average audio intensity of your mic sound. You can use it to get
            average intensities while you're talking and/or silent. The average
            is the avg of the 20% largest intensities recorded.
        """

        print("Getting intensity values from mic.")
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        values = [math.sqrt(abs(audioop.avg(stream.read(self.CHUNK), 4))) 
                for x in range(num_samples)] 
        values = sorted(values, reverse=True)
        r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
        print("Finished")
        print("Average audio intensity is", r)
        stream.close()
        p.terminate()
        return r


    def save_speech(self, data, p):
        """ Saves mic data to temporary WAV file. Returns filename of saved 
            file """
        #filename = 'resources/output_'+str(int(time.time()))
        filename = 'resources/record.wav'
        # writes data to WAV file
        data = b''.join(data)
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)  
        wf.writeframes(data)
        wf.close()
        return filename

