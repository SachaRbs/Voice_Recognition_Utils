import pyaudio
from pynput import keyboard
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 16000  # Record at 44100 samples per second
seconds = 20
filename = "voice_test.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

input("press enter to start record")
print('Recording')
print("press enter to stop recording")

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames
sec = 0
break_program = False

def on_press(key):
    global break_program
    print (key)
    if key == keyboard.Key.enter:
        break_program = True
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False and sec < int(fs / chunk * seconds):
        data = stream.read(chunk)
        frames.append(data)
    listener.join()

stream.stop_stream()
stream.close()
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()