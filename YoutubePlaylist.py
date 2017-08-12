import re
import urllib
import urllib.parse
import urllib.request
import time
from selenium import webdriver

start_time = time.time()

try:
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=PLeI9sYpZVfZVl4B665SV5OzqJ3z4WARDr&key=AIzaSyCdSQ6WHMBZZdIUTfl5dJYGg1CaM9NZdNk'
    headers = {}
    headers ['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    totalVideos = 590
    totalPages = 590//50
    respData = resp.read()
    nextPageToken = re.findall('"nextPageToken": "(.*?)"', str(respData))
    for page in range(totalPages):
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken='+ str(nextPageToken[page]) + '&playlistId=PLeI9sYpZVfZVl4B665SV5OzqJ3z4WARDr&key=AIzaSyCdSQ6WHMBZZdIUTfl5dJYGg1CaM9NZdNk'
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


video_dl = []
for eachP in video_id:
    video_dl.insert(len(video_dl), 'https://www.youtubeinmp3.com/download/?video=https://www.youtube.com/watch?v=' + (str(eachP)))
driver = webdriver.Firefox(executable_path=r"C:\Users\Shlok Khandelwal\Desktop\geckodriver.exe")
driver.set_page_load_timeout(30)
for eachLink in video_dl:
    try:
        driver.get(eachLink)
        dlElement =  driver.find_element_by_id("download")
        dlElement.click()
    except Exception as e:
        print(eachLink)
        print(str(e))
print(str(time.time()-start_time))