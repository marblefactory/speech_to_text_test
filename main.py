import queue
import sounddevice as sd
import soundfile as sf

q = queue.Queue()
SAMPLE_RATE = 44100

def callback(indata, frames, time, status):
    if status:
        print('STATUS', status)

    q.put(indata.copy())


def record(file_name):
    """
    Records audio to the specified file.
    """

    global should_record
    should_record = True

    print('Starting Record')

    with sf.SoundFile(file_name, mode='w', samplerate=44100, channels=2) as file:
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            input('Press to stop')

            while not q.empty():
                file.write(q.get())

            print('Written file')


while True:
    input('Press Enter to record/stop')
    record('output.wav')
