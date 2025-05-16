

# After making the video call the function that do make the video after that do this +
# post the video to tiktok + youtube under the name of Quran_Project


# clip.save_frame("test.png",t=0)
from makeVideo import *
from dotenv import load_dotenv,dotenv_values
import requests
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload



load_dotenv()


Webhook = os.getenv("WEBHOOK")

# youtube set up
YoutubeClientId = os.getenv("Youtube_ClientID")
YoutubeClientSecret = os.getenv("Youtube_ClientSecret")
YouTube_REDIRECT_URI =  os.getenv("YouTube_REDIRECT_URI")
# testing
print(f"Youtube Client Id = {YoutubeClientId}, Youtube Client Secret =  {YoutubeClientSecret} , web hook = {Webhook}")

hours = 0  # if the hours is 24 than do this -> make the hours 0 again -> incress day by one 
day = 1 
howmanyhourseTopost = 6 # like how many times a video get uploaded so i have 6 so there would be 4 videos each day
videonumber =  1
StarterTick = time.time()

client_config_youtube = {
    "installed": {
        "client_id": YoutubeClientId,
        "client_secret": YoutubeClientSecret,
        "redirect_uris": [YouTube_REDIRECT_URI],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }
}


def StartFlow():
    flow = InstalledAppFlow.from_client_config(
    client_config_youtube,
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
    
    )

    credentials = flow.run_local_server(port=8080)
    print(f"your credentials is: {str(credentials):^5} ")
    return credentials



def post_Youtube(video): # this function take a video than post it to a youtube channl
    if YoutubeClientSecret and YoutubeClientId:
        # continue 
        print()
        credentials = StartFlow()
        youtube = build("youtube","v3",credentials=credentials)
        request_body = {
            "snippet": {
                "title": f"قران كريم يوم {day}\n مقطع رقم #  {videonumber}",
                "description": f"قران كريم مشروع انشاء مقاطع قران تلقائي شوف github \n github: https://github.com/foxdrt/Quran-Projects", # وصف المقطع
                "tags": ["قرآن", "Quran","قران كريم","github","Quran"],
                "categoryId": "27"
            },
            "status": {
                "privacyStatus": "public"  
            }
        }
        # start to post the video
        media = MediaFileUpload(video)
        upload_request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        )
        response = upload_request.execute()
        print(f" response = \n {response}")

    else:
        print("Error , u haven't set a youtube , client secret / id \n if u dont enter it than it will continue the code but wont post it to youtube") # bro just add the Client secret and id what is the point of the script without it 😭😭
        
    print(2)
# post_Youtube("QuranVideo1v1.mp4")






while True:
        StarterTick = time.time()
        FinalPath,imagepath,videopath = makeVideo()
        # فتح الملف بصيغة "rb" (قراءة ثنائية)
        with open(FinalPath, 'rb') as video_file:

            files = {
                'file': (os.path.basename(FinalPath), video_file, 'video/mp4')  # ممكن تغيّر الامتداد حسب نوع الفيديو
            }
            data = {
                "content": f"Quran_Project - نشر تلقائي للفيديو 🎥 v1.5.3 ,video number = {videonumber} \n video took {time.time() - StarterTick:^5.2f}s ⏰"
            }
            # إرسال الطلب
            if Webhook:
                  response = requests.post(Webhook, data=data, files=files)
            post_Youtube(FinalPath)
            
        videonumber += 1
        hours += howmanyhourseTopost
        if hours >= 24:
                hours = 0
                day += 1

        print(f"THe programm took {time.time() - StarterTick:>3.2f} seconds to finish")
        print("programm finished")
        time.sleep(howmanyhourseTopost*3600) # soo every hour X 3600 second to make it wait time before upload the next video
