import os, sys, json, m3u8_to_mp4
os.system("clear")

list_of_m3u8_files = os.listdir("m3u8/")

#print(list_of_m3u8_files)

for files in list_of_m3u8_files:
    print(files)
    file_name = "m3u8/" + files
    m3u8_to_mp4.download(file_name) 

    break