import wave
import os
s=int(input("Please enter the key:"))
size=input("the size(\ to \\):")
name=input("newfile_name:")

with wave.open("newandf.wav",'rb') as data3:
    new_txt=data3.readframes(-1)

b = int.from_bytes(new_txt, byteorder='little', signed=True)
b-=s
size = os.path.getsize(size+"newandf.wav")
new_txt = b.to_bytes(size, byteorder='little', signed=True) 
    
with open(name,'wb') as f:
    f.write(new_txt)
