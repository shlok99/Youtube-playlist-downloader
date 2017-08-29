# YTplaylistTomp3
Downloads all the youtube videos in a playlist as an mp3 using python 3.6

# Dependencies
1. re  
Using pip run the command pip install -re in the terminal window    
2. urllib  
Using pip run the command pip install -urllib in the terminal window      
3. selenium  (gecko driver must be installed)  
Using pip run the command pip install -selenium in the terminal window  
To install the geckodriver https://github.com/mozilla/geckodriver/releases  
# How To Use
1. Make sure all the dependencies are installed  
2. Copy the path of the gecko driver into driver (first parameter)  
3. Copy the path of the firefox profile you wish to use into fp  
4. Change the playlist id to the playlist id that you want to download  
5. Go to google's api developer, create an account and request for an api key for youtube data
6. Input the key into API key
7. Find the total number of videos in the playlist and insert it into the totalVideos variable
8. Run the file

# Version 1.0  
Can download approximately 60% of the videos in a playlist

# Version 2.0
Added error handling of alerts that would stop flow of downloads  
Increased user usability  
Can download approximately 90% of videos in a playlist

# Version 3.0
Added cross checking with files downloaded to all the youtube playlist 
Increased user usability 

# Goals
Be able to control server overload for file downloads

