
![Uploading QuranProject.jpg…]()


# Quran Automatic Video Maker
  This project creates a video using a random Quran verse and a random image.
  It then combines the verse with the image into a video,
  and finally uploads the video (currently supports posting to a Discord webhook or YouTube).
# code expalinstion
  
  # Fetch image py file 
  ```py
  MAINFUNCTION()
  ```
  This function sends a request to a Pinterest user who posts Islamic or nature images.
  It returns an array of image URLs from that user.

  Why?
  Because we need a random image to use in the video. That’s where the next function comes in:
```py 
randomImage()

```
As the name suggests, this function takes the array from MAINFUNCTION and picks a random image from it.

That’s it for the first part of the code.
2. makeVideo file
As the name implies, this file is responsible for creating the video.
It uses a random image (from randomImage) and adds a random Quran verse from a YouTube playlist.

You can change the playlist from here:
```py

  # Example YouTube playlist URL:
  # https://www.youtube.com/playlist?list=PLKB9puQeauyBTnMmRWsB4VVfbbWR0tKCc
  
  # To add or edit a playlist:
  # 1. Go to any YouTube playlist you want to use.
  # 2. Copy the part of the URL **after** the question mark (?) — specifically, the value of `list=`.
  #    For example, from the URL above, you would copy:
  #    list=PLKB9puQeauyBTnMmRWsB4VVfbbWR0tKCc
  
  # Now paste it below inside the VideoLists array:
  
  VideoLists = [
      "list=PLKB9puQeauyAxadEXopBm_CC8ldI_yUjL",
      "list=PLKB9puQeauyDkqQ2TBxuZj30UMKA51Yds",
      "list=PLKB9puQeauyDbnCis9xagtEQ-vtEgUOHr"
  ]
```


# . Posting the Video
In the final step, the video is uploaded.
You need to have a .env file with the following variables:
```py

WEBHOOK = "Discord webhook URL (optional)"
Youtube_ClientID = "Your YouTube client ID"
Youtube_ClientSecret = "Your YouTube client secret"
YouTube_REDIRECT_URI = "http://localhost:8080"
```
What does PostVideo.py do?
PostVideo.py connects to your YouTube channel using your credentials,
then automatically uploads a video every set number of hours.

You can change how often it posts by modifying this variable:

```py
# Set how many hours to wait between each video upload
hours = 6  # Change this to the number of hours you want

```

# Set how many hours to wait between each video upload
hours = 6  # Change this to the number of hours you want


# What’s Next?
I plan to deploy this script to the cloud so it can run automatically 24/7 without needing a computer to be on.

This means the script will:

Randomly generate a video every few hours

Upload it to YouTube or send it to a Discord webhook

All without manual work!

If you need any help or have questions, feel free to contact me on Discord:
foxdrt
