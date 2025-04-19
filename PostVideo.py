

# After making the video call the function that do make the video after that do this +
# post the video to tiktok + youtube under the name of Quran_Project


# from moviepy.editor import TextClip
# from moviepy.config import change_settings
# change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


# clip = TextClip("Quran Project", fontsize=70,color="#FFD4FF", font="VIP_Hala")
# clip.save_frame("test.png",t=0)
from makeVideo import *
from dotenv import load_dotenv,dotenv_values
import requests
import os
load_dotenv()



Webhook = os.getenv("WEBHOOK")



for i in range(1,5):
    FinalPath = makeVideo()
# فتح الملف بصيغة "rb" (قراءة ثنائية)
    with open(FinalPath, 'rb') as video_file:
        # تحضير البيانات
        files = {
            'file': (os.path.basename(FinalPath), video_file, 'video/mp4')  # ممكن تغيّر الامتداد حسب نوع الفيديو
        }
        data = {
            "content": "Quran_Project - نشر تلقائي للفيديو 🎥"
        }
        # إرسال الطلب
        response = requests.post(Webhook, data=data, files=files)

    # طباعة نتيجة الإرسال
    print(response.status_code)
    print(response.content)