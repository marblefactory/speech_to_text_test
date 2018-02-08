import queue
import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 44100
# Recorded data is pushed to this, then popped for writing to the file.
recorded_queue = queue.Queue()

def callback(in_data, frames, time, status):
    if status:
        print('STATUS', status)

    recorded_queue.put(in_data.copy())


def record(file_name):
    """
    Records audio to the specified file.
    """

    print('Starting Record')

    with sf.SoundFile(file_name, mode='w', samplerate=SAMPLE_RATE, channels=1) as file:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback):
            input('Press to stop')

            while not recorded_queue.empty():
                file.write(recorded_queue.get())

            print('Written file')


while True:
    input('Press Enter to record/stop')
    record('output.wav')
