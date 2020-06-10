from os import path
from os.path import basename
import os
# pip install pydub
from pydub import AudioSegment   
# AudioSegment.ffmpeg ="C:\ffmpeg-20200610-9dfb19b-win64-static\bin"

directory = raw_input("What dataset would you like to convert?\n Enter dataset\\\"Directory Name\\\" : ")

mp3_files=[]
for file in os.listdir("./dataset/{}".format(directory.strip())):
    if file.endswith(".mp3"):
        mp3_files.append(file)

# sound=AudioSegment.from_mp3("./dataset/Music/000002.mp3")

for i,file in enumerate(mp3_files):
    mp3_file = "./dataset/{}/{}".format( directory.strip(), file)
    sound = AudioSegment.from_mp3(mp3_file)
    wav_file = "./dataset/{}/{}.wav".format( directory.strip(), os.path.splitext(file)[0])
    sound.export(wav_file , format='wav')
    os.remove(mp3_file)
    print("{} {:3.2f} %".format(wav_file, (float(i)/len(mp3_files)*100)) )


print(len(mp3_files))