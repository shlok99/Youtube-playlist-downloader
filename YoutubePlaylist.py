import re
import urllib
import urllib.parse
import urllib.request
import time
from selenium import webdriver
start_time = time.time()
playlistId = ''
totalVideos = 597
try:
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId='+playlistId + '&key={API KEY}'
    headers = {}
    headers ['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    totalPages = totalVideos//50
    respData = resp.read()
    nextPageToken = re.findall('"nextPageToken": "(.*?)"', str(respData))
    for page in range(totalPages):
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken='+ str(nextPageToken[page]) + '&playlistId='+ playlistId +'&key={API KEY}'
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
failed_dl = []
fp = webdriver.FirefoxProfile(r"C:\Users\Shlok Khandelwal\AppData\Roaming\Mozilla\Firefox\Profiles\4hlau0sw.Selenium")
driver = webdriver.Firefox(executable_path=r"C:\Users\Shlok Khandelwal\Desktop\geckodriver.exe", firefox_profile=fp)
driver.set_page_load_timeout(60)
driver.get(video_dl[0])
video_dl.pop(0)
dlElement =  driver.find_element_by_id("download")
dlElement.click()
videoCount = 0
for eachLink in video_dl:
    try:
            alert = driver.switch_to_alert()
            alert.dismiss()
    except Exception as e:
        print("No alert")
    try:
        driver.get(eachLink)
        dlElement =  driver.find_element_by_id("download")
        while dlElement.is_enabled == False:
            pass
        dlElement.click()
    except Exception as e:
        print(e)
        failed_dl.insert(len(failed_dl), eachLink)
        
    videoCount+=1
    print(videoCount)
    print(failed_dl)
if (len(failed_dl)>0):
    for eachLink in failed_dl:
        try:
            driver.get(eachLink)
            dlElement =  driver.find_element_by_id("download")
            while dlElement.is_enabled == False:
                pass
            dlElement.click()
        except Exception as e:
            try:
                alert = driver.switch_to_alert()
                alert.dismiss()
                driver.get(eachLink)
                dlElement =  driver.find_element_by_id("download")
                while dlElement.is_enabled == False:
                    pass
                dlElement.click()
            except Exception as e:
                print(eachLink)
                print(e)
else:
    pass
print(str(time.time()-start_time))
