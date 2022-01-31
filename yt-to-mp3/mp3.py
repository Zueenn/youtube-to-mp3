from pytube import YouTube
import os

link = input("İndirmek istediğiniz videonun linki: ")
directory = input("İndirmek istediğiniz dosyanın adı: ")

try:
    yt = YouTube(link)
except:
    print("Link bulunamadı.")
    exit()

mp3 = yt.streams.filter(only_audio=True).first()

print("İndiriliyor...")

output = mp3.download(directory)

base, ext = os.path.splitext(output)
to_mp3 = base + ".mp3"
os.rename(output, to_mp3)

print("İndirme tamamlandı!")