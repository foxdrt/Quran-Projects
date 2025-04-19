import requests 
from bs4 import BeautifulSoup
import time
import json
import re
import os # just to clear the terminal for testing
import random
# Getting pinterest image
WebhookDebugg = ""
pintrest_API = "" # i have it now, change the way script

user = "Quran_Project"
TargetUrl = f"https://www.pinterest.com/{user}/"
def MAINFUNCTION():
        def FilterFunction(InsertedRequest):
            InsertedRequest = requests.get(TargetUrl)

            # check if the list is a list , and check if the request is vaild 
            if  str(type(InsertedRequest)) == "<class 'requests.models.Response'>" :
                # for Thing in HtmlFile:
                HtmlFile = BeautifulSoup(InsertedRequest.text,'html.parser') # the returned html page 
                Tags = HtmlFile.find_all("script")

                for script in Tags:
                    time.sleep(0.1)
                    if script.string:
                        if len(script.string) > 15:
                            ImageList = list()
                            print("found it")
                            JsonString = str(HtmlFile)
                            StarterIndex = JsonString.find('"template_type":null},') # remove later
                            EndIndex = JsonString.rfind(',"traceLoggerData"') # remove later
                            if EndIndex != -1 :
                                JsonString = JsonString[:EndIndex]
                                pattern = re.compile(r'https://i\.pinimg\.com/(?!upload|30x30)[^"]+\.jpg') # idk some of this magic but  here what it does
                                # find any url start with https//i/.pinimg.com/dont inculd any url that has upload or 30x30/more stuff /.jpg has to stop at jpg

                                matches = pattern.finditer(JsonString)
                                for match in matches:
                                    try:
                                         if ImageList.index(match.group(0)):
                                              continue
                                    except ValueError:
                                        ImageList.append(match.group(0))

                                        continue

                                return ImageList
                            else:
                                print("error ")
                                return "error"
                else:
                    # print an error 
                     WhatWrong = f"Error with the respond, respond type = '{InsertedRequest.status_codes}' "
                     
                     print(f"Error = {WhatWrong}, ")
                     return "error"
                    
        Reqest = requests.get(TargetUrl)
        print(type(Reqest),Reqest)
        ImageList = FilterFunction(Reqest)
        if ImageList != "error":

             return ImageList
        else:
             print("ERROR",exit)


        # print(HtmlFile.prettify())
        
        # print(f"\n \n {Tags.string} tt")
    



def randomImage():
     
    imageSet = MAINFUNCTION()

    return imageSet[random.randint(0,len(imageSet)-1)]




