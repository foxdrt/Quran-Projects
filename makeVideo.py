
import moviepy.Clip
import moviepy.editor
import moviepy.video
import pytubefix.contrib
import pytubefix.contrib.playlist
import moviepy.editor as mp


from moviepy.editor import *
from moviepy.video.fx.all import *

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


#
import requests
import os 
import pytubefix 
from pytubefix import *
import time
from fetchImage import *

import pygame
StarterTick = time.time()
print("start counter")
VideoList = "list=PLKB9puQeauyBTnMmRWsB4VVfbbWR0tKCc"
PlayList = f"https://www.youtube.com/playlist?{VideoList}"
ImageCounter = 0
VideoCounter = 0
fontpath = r"Path\quran project" # use ur own path!

# https://www.youtube.com/playlist?list=PLKB9puQeauyBTnMmRWsB4VVfbbWR0tKCc

# start of functions



def downloadImage():
    global ImageCounter # for some reason py is weird that cant accesee tho is just above it 😭

    if 1 == 1: # yes 1==1 always true i know -- change later
        
        StartCount = time.time()
        

        RandomImageURl = randomImage()
        RequestDownLoadImage = requests.get(RandomImageURl)
        FileName = f"Image{ImageCounter}.jpg"
        with open(FileName,"wb") as IMAGE:
            IMAGE.write(RequestDownLoadImage.content)

        print(f"Video Took {time.time() - StartCount:>5.2f} s to finish downloading")
        ImageCounter += 1 
        return FileName
    else:
        print(f"url is not  a string ")

def downloadVideo(url:str):
    global VideoCounter
    if isinstance(url,str):
        print(url)
        FileName = f"TempoyVideo{VideoCounter}.mp4"
        Video = pytubefix.YouTube(url)
        Video = Video.streams.get_highest_resolution()
        Video = Video.download(filename=FileName)
        StartCount = time.time()
        print(f"Video Took {time.time() - StartCount:>5.4f} s to finish downloading")
        VideoCounter += 1
        return FileName
    else:
        print(f"url is not  a string {str(type(url)) :>5}")

def RandomVideoFromPlayList(List):
    if str(type(List)) == "<class 'pytubefix.contrib.playlist.Playlist'>":

            randomIndex = random.randint(0,len(List.video_urls)-1) # -1 cuz list start with 0 so if we have 5 items it would be 4 but len would return 5 
            print(f"your random index is {randomIndex}")
            return List[randomIndex]
    else:
        print(f"List is not a list , {str(type(List)):>5} ")
        print("error")

def getPlayList(ListUrl):
    PlayListVideos = pytubefix.contrib.playlist.Playlist(ListUrl)
    for Video in PlayListVideos:
         continue
    return PlayListVideos # just safe the list for futrue use

def EditVideo(Video,Image):
    if Video and Image:
        ImageMaskPath = r"C:\Users\alsyd\OneDrive\Desktop\quran project\Imagemask.png" # USE UR OWN PATH !!!!
        videoClip:mp.VideoClip = mp.VideoFileClip(Video).set_position("center","center").fx(vfx.fadein,0.5).fx(vfx.fadeout,0.5)
        imageclip:mp.ImageClip = mp.ImageClip(Image,duration=videoClip.duration).set_position("center","center").fx(vfx.fadein,0.5).fx(vfx.fadeout,0.5)
        videoClip = videoClip.resize(height=880)
        imageclip = imageclip.resize(height=1250)
        background:mp.ColorClip = mp.ColorClip(size=(1094, 1920), color=(0,0,0), duration=videoClip.duration).fx(vfx.fadein,0.5).fx(vfx.fadeout,0.5)
        TheEndSeen:mp.ColorClip = mp.ColorClip(size=(1094, 1920), color=(0,0,0), duration=3).set_start(videoClip.duration).fx(vfx.fadein,0.5).fx(vfx.fadeout,0.5)
        textClip:mp.TextClip  = mp.TextClip(txt="Quran Project\n check github"
                            ,fontsize=60
                            ,font="VIP_Hala", # aka custom font
                            color="#FFFFFF", # dont use words like white , dont use rgb format, use hex code for color
                            
        ).set_start(videoClip.duration).set_duration(3).set_position(("center","center")).fx(vfx.fadein,0.5).fx(vfx.fadeout,0.5)
        videoClip = videoClip.fx(mp.vfx.mask_color,color=[0,0,0],s=5,thr=100) # remove the black color
        ImageMask = mp.ImageClip(ImageMaskPath,ismask=True)
        imageclip =imageclip.set_mask(mask=ImageMask)
        croppedIMage = imageclip.crop(width=1000, height=1250, x_center=imageclip.w / 2, y_center=imageclip.h / 2)
        croppedVideo = videoClip.crop(width=1000, height=880, x_center=videoClip.w / 2, y_center=videoClip.h / 2)



                                        #the order matter cuz it is the layering, so background would be the first item  after it the image after it the video and last the text 
        final_Clop = CompositeVideoClip([background, # 1
                                        croppedIMage, # 2
                                        croppedVideo,# 3 
                                        TheEndSeen,# 4
                                        textClip # 5
                                        ])

        final_Clop.write_videofile("QuranVideo1v.mp4", codec="libx264", audio_codec="mp3")
        return final_Clop
    else:
        print("error")
print("getting the playlist , it may take a bit of time")


def makeVideo():
    global PlayList
    print("ok")
    PlayList = getPlayList(PlayList)

    VideoUrl =  RandomVideoFromPlayList(PlayList)
    VideoMp4 = downloadVideo(VideoUrl)
    Image = downloadImage()
    print(VideoUrl,VideoMp4,Image)
    # path to go first time it is  the py  file , but i dont want the py  file , so i get the parent aka the folder than i get the paths of the image and the video 
    PathToGo = os.path.realpath(__file__)
    EndIndex = PathToGo.rfind("\\") # just to get the father , aka parent of this script
    if PathToGo != -1:
        PathToGo = PathToGo[:EndIndex]
        ImagePath = f"{PathToGo}\{Image}"# getting path
        VideoPath = f"{PathToGo}\{VideoMp4}"# getting path
        EditVideo(VideoPath,ImagePath)
        return f"{PathToGo}\QuranVideo1v.mp4"




    else:
        print("Error , couldn't get the path")


# end of functions


# print(len(PlayList))

# VideoLink = RandomVideoFromPlayList(PlayList)
# downloadVideo(VideoLink)
# downloadImage()
# use hex for the colores


print(f"THe programm took {time.time() - StarterTick:>3.2f} seconds to finish")
print("programm finished")
