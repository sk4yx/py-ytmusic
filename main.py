# Powered By Skay

# =====================================================
# Usage: Type the name of a song, copy the ID of some
# result and paste it into the input, and then it will
# download the song and play it
# =====================================================

import os
from playsound import playsound
from pytube import YouTube,Search

def download_link(link):
	link_download = link
	yt = YouTube(link_download) 
	global name
	stream = yt.streams.filter(only_audio=True).first()

	stream.download()
	os.rename(stream.default_filename, stream.default_filename+".mp3")
	test = stream.default_filename+".mp3"
	name = test

def downloadd_link():
    link =  input("LINK >> ")
    download_link(link)

def search_download():
	search_name = input("NAME >> ")
	s = Search(search_name)
	print("RESULTS FOUND: " + str(len(s.results)))
	print(str(s.results))
	play_search = input("https://www.youtube.com/watch?v=")
	download_link("https://www.youtube.com/watch?v="+play_search)
	os.system(f'"{name}"')
	
search_download()
