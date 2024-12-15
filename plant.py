import random
import wave
import sys
import os
#sys.set_int_max_str_digits(10**8)
#for i in range(1,1001,1):
#    a=random.randint(-10**10000,10**100000)
#   with open("bnwav.txt",'w',encoding='utf-8') as file:
#        file.write(str(a))
a=int(input("Please set up the key:"))
size=input("the size(\ to \\):")
names=input("filename:")
with open(names,'rb') as data1:
    new_wav2=data1.read()
b = int.from_bytes(new_wav2, byteorder='little', signed=True)
b+=a
size = os.path.getsize(size+names)
new_wav2 = b.to_bytes(size, byteorder='little', signed=True) 
with wave.open("andf.wav",'rb') as data:
    new_wav=bytearray(data.readframes(-1))
with wave.open("newandf.wav",'wb') as data2:
    data2.setnchannels(2)
    data2.setsampwidth(4)
    data2.setframerate(22050)
    data2.writeframes(new_wav2)

