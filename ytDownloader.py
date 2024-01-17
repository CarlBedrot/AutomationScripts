from pytube import YouTube
from sys import argv 

def clean_link(link):
    return link.replace('\\', '')

link = argv[1]
cleaned_link = clean_link(link)
yt = YouTube(cleaned_link)

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download('/Users/carlbedrot/Desktop/Youtube')
print("Download completed!!")

# Run: python3 ytDownloader.py "link"