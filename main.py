from video_editor import VideoEditor
from quote_downloader import QuoteDownloader
from random import randint
from typing import Final
QUOTE_KEYWORDS : Final = ["fear","lifestyle", "motivation"]
USER_NAME : Final = "Kenny Stone"
PROFILE_IMAGE : Final = "seashore.jpg"
PADDING_FROM_IMAGE : Final = 50    
def addUserNameToVideo(video : VideoEditor):
    video.addText(
        USER_NAME,
        _color="#ffffff",
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.35), # same as image
        size=(200,50),
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
        font_size=25,
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.38),
        # _position=("center","top"),
        _color="#ffffff",
        size=(1080 - (50 + 160),300)
    )

def main():
    mainVideo = VideoEditor("4438080.mp4",0.4)
    addProfileToVideo(mainVideo)
    addUserNameToVideo(mainVideo)
    addQuoteToVideo(mainVideo)
    
    mainVideo.saveVideo("trial30.mp4")
    # mainVideo.addText(
    #     USER_NAME
    # )
    
if __name__ == "__main__":
    main()