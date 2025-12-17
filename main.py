'''
###################################################################################
# USES `pexels` api to get videos                                                 #
# NOTE: pexels api requires an api key which can be                               #
# obtained by creating an account and requesting for an api key                   #
#                                                                                 #
# Uses zenquotes api to get quotes                                                #
# :see: https://zenquotes.io/api/quoutes/`your-query`                             #
# Author: Kenny Stone                                                             #
#                                                                                 #
###################################################################################
'''
from video_editor import VideoEditor
from quote_downloader import QuoteDownloader
from datetime import datetime
from random import randint
from typing import Final
QUOTE_KEYWORDS : Final = ["fear","lifestyle", "motivation"]
USER_NAME : Final = "Kenny's quote of the day"
PROFILE_IMAGE : Final = "seashore.jpg"
PADDING_FROM_IMAGE : Final = 65    
def addUserNameToVideo(video : VideoEditor):
    video.addText(
        USER_NAME,
        _color="#cdcccc",
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.35), # same as image
        size=(500,50),
        font_size=30,
    )

def addProfileToVideo(video : VideoEditor):
    video.addImage(
        PROFILE_IMAGE,
        _position = (50,video.target_resolution[1] * 0.35),  #  (width,height)   image should be displayed at 30% from the top
        size = (100,100)
    )
    

def addQuoteToVideo(video : VideoEditor):
    quote = QuoteDownloader(QUOTE_KEYWORDS[randint(0,len(QUOTE_KEYWORDS) - 1)])
    quote.storeQuotes()
    quotes = quote.getQuote()
    video.addText(
        quotes[randint(0,len(quotes) - 1)],
        font_size=43,
        # 50 + the position of the image + the width
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.38),
        # _position=("center","top"),
        _color="#ffffff",
        size=(1080 - (50 + 160 + PADDING_FROM_IMAGE),850)
    )

def addDateToVideo(video : VideoEditor):
    year = datetime.now().date().year
    month = datetime.now().date().month
    day = datetime.now().date().day
    hour = datetime.now().time().hour
    hour = str(hour).zfill(2)   # Pads a string with leading zeros until it reaches the specified width.
    minute = datetime.now().time().minute
    minute = str(minute).zfill(2) # Pads a string with leading zeros until it reaches the specified width.
    DATE_PADDING_TOP_FROM_IMAGE : Final = 20
    date_format = f"{day}/{month}/{year} {hour}:{minute}"
    print(f"{day}/{month}/{year} {hour}:{minute}")
    video.addText(date_format,
                  font_size=25,
                  _color="#888787",
                  size=(150,150),
                  _position=(50,
                             video.target_resolution[1] * 0.38 + 100))


def main():
    mainVideo = VideoEditor("4438080.mp4",0.4)
    addProfileToVideo(mainVideo)
    addUserNameToVideo(mainVideo)
    addQuoteToVideo(mainVideo)
    addDateToVideo(mainVideo)
    mainVideo.saveVideo("trial44.mp4")
    # mainVideo.addText(
    #     USER_NAME
    # )
    
if __name__ == "__main__":
    main()