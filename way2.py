from pydub import AudioSegment
from pydub.utils import make_chunks
song = AudioSegment.from_wav("./m1.wav")
MIN_VAL = 0.1
li = []
li1 = []
max_amp = song.max_dBFS
average = song.dBFS
trigger_dbfs = average - average*MIN_VAL
chunk_length_ms = 5000 # pydub calculates in millisec
chunks = make_chunks(song, chunk_length_ms)
s= 0
start = False
for i in chunks:
    if round(trigger_dbfs,1) <= round(i.dBFS,1):
        if not start:
            start = True

        li.append(i)
    elif start==True:
        li1.append(sum(li, AudioSegment.empty()))
        li = []
        start = False

for i in range(len(li1)):
    li1[i].export(f"audio/{i}.mp3", format="mp3")
a = sum(li1, AudioSegment.empty())
a.export(f"full.mp3", format="mp3")