import re
import os
import urllib
import urllib.parse
import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time = time.time()
playlistId = '' #Found in the url of the playlist
totalVideos = #input integer here for total # of videos in the playlist
APIkey = '' #input api key from youtube data analyatics
try:
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId='+playlistId + '&key=' + APIkey
    headers = {}
    headers ['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    totalPages = totalVideos//50
    respData = resp.read()
    nextPageToken = re.findall('"nextPageToken": "(.*?)"', str(respData))
    for page in range(totalPages):
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken='+ str(nextPageToken[page]) + '&playlistId='+ playlistId +'&key=' + APIkey
        headers = {}
        headers ['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData+= resp.read()
        nextPageToken = re.findall('"nextPageToken": "(.*?)"', str(respData))

except Exception as e:
    print(str(e))

video_id = re.findall('"videoId": "(.*?)"', str(respData))
video_title = re.findall('"title": "(.*?)"', str(respData))
video_files = []
for titles in video_title:
    titles += ".mp3"
    video_files.insert(len(video_files), titles)
dictionary = dict(zip(video_files, video_id))
video_dl = []
for eachP in dictionary.values():
    video_dl.insert(len(video_dl), 'https://www.youtubeinmp3.com/download/?video=https://www.youtube.com/watch?v=' + (str(eachP)))
dictionary = dict(zip(video_files, video_dl))
failed_dl = []
fp = webdriver.FirefoxProfile(r"C:\Users\Shlok Khandelwal\AppData\Roaming\Mozilla\Firefox\Profiles\4hlau0sw.Selenium")
driver = webdriver.Firefox(executable_path=r"C:\Users\Shlok Khandelwal\Desktop\geckodriver.exe", firefox_profile=fp)
driver.set_page_load_timeout(60)
videoCount = 0
songsToDelete = []

for delete in songsToDelete:
    del dictionary [delete]
while(len(dictionary)> 1):
    for eachLink in dictionary.values():
        try:
            alert = driver.switch_to_alert()
            alert.dismiss()
        except Exception as e:
            print("No alert")
        try:
            driver.get(eachLink)
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "download")))
            dlElement =  driver.find_element_by_id("download")
            dlElement.click()
        except Exception as e:
            print(e)
        songsDownloaded = os.listdir(r"Downloads")
        for titles in songsDownloaded:
            for downloaded in dictionary.keys():
                if(str(titles) == str(downloaded)):
                    songsToDelete.insert(len(songsToDelete), titles)
                    print("Deleted")
        for delete in songsToDelete:
            del dictionary [delete]
print(dictionary)
print(len(songsDownloaded)+ len(dictionary))
print(str(time.time()-start_time))
