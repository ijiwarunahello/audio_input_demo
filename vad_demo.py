import collections
import webrtcvad
import pyaudio
import wave

# 録音のパラメータ設定
CHUNK = 480
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = "output_vad.wav"

vad = webrtcvad.Vad(3)
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []
silent_frames = 0
has_voice = False
while True:
    data = stream.read(CHUNK)
    if vad.is_speech(data, RATE):
        print("Speech detected.")
        frames.append(data)
        silent_frames = 0
        has_voice = True
    else:
        print("Silence detected.")
        silent_frames += 1
        if has_voice and silent_frames > 20:  # Adjust this value for your needs
            break

print("* done recording")

stream.stop_stream()
stream.close()
pa.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(pa.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
