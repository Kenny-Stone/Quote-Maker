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
from random import randint
from typing import Final
QUOTE_KEYWORDS : Final = ["fear","lifestyle", "motivation"]
USER_NAME : Final = "Kenny's quote of the day"
PROFILE_IMAGE : Final = "seashore.jpg"
PADDING_FROM_IMAGE : Final = 50    
def addUserNameToVideo(video : VideoEditor):
    video.addText(
        USER_NAME,
        _color="#ffffff",
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.35), # same as image
        size=(500,50),
        font_size=40,
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
        font_size=45,
        # 50 + the position of the image + the width
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.38),
        # _position=("center","top"),
        _color="#ffffff",
        size=(1080 - (50 + 160 + PADDING_FROM_IMAGE),850)
    )

def main():
    mainVideo = VideoEditor("3571264.mp4",0.4)
    addProfileToVideo(mainVideo)
    addUserNameToVideo(mainVideo)
    addQuoteToVideo(mainVideo)
    
    mainVideo.saveVideo("trial36.mp4")
    # mainVideo.addText(
    #     USER_NAME
    # )
    
if __name__ == "__main__":
    main()