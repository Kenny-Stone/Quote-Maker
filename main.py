'''
###################################################################################
# USES `pexels` api to get videos                                                 #
# NOTE: pexels api requires an api key which can be                               #
# obtained by creating an account and requesting for an api key                   #
#                                                                                 #
# Uses zenquotes api to get quotes                                                #
# :see: https://zenquotes.io/api/quotes/`your-query`                             #
# Author: Kenny Stone                                                             #
#                                                                                 #
###################################################################################
'''
from video_editor import VideoEditor
from video_downloader import VideoDownloader
from quote_downloader import QuoteDownloader
from datetime import datetime
from random import randint
from typing import Final
# QUOTE_KEYWORDS : Final = ["fear","lifestyle", "motivation"]
VIDEO_KEYWORDS = [
    "people",
    "nature",
    "city",
    "street",
    "walking",
    "office",
    "food"
]
# VIDEO_KEYWORDS = [
# "person walking on street",
#     "man walking in city",
#     "woman walking outdoors",
#     "people walking in city",
#     "crowd walking on street",
#     "person talking on phone",
#     "people talking together",
#     "friends walking together",
#     "person working on laptop",
#     "man typing on laptop",
#     "woman using smartphone",

#     # City / Urban
#     "city street traffic",
#     "cars driving on road",
#     "people walking in city street",
#     "night city street",
#     "urban street traffic",
#     "busy city street",
#     "downtown street view",
#     "aerial view of city",
#     "cars on highway",

#     # Nature
#     "forest with trees",
#     "river flowing",
#     "water flowing in river",
#     "waves crashing on beach",
#     "sunset over ocean",
#     "sunrise in mountains",
#     "rain falling",
#     "snow falling",
#     "trees moving in wind",
#     "waterfall in forest",

#     # Work / Business
#     "people working in office",
#     "person typing on laptop",
#     "coworkers working together",
#     "business meeting in office",
#     "man working at desk",
#     "woman working on computer",
#     "office desk workspace",

#     # Technology
#     "coding on laptop",
#     "programmer typing code",
#     "computer screen with code",
#     "server room",
#     "data center hallway",
#     "person using computer",
#     "typing on keyboard",

#     # Fitness
#     "person running outdoors",
#     "people exercising in gym",
#     "woman doing yoga",
#     "man lifting weights",
#     "stretching exercise",
#     "cycling on road",

#     # Food
#     "person cooking in kitchen",
#     "chef preparing food",
#     "coffee being poured",
#     "cutting vegetables",
#     "street food cooking",
#     "food being prepared",

#     # Travel
#     "airplane taking off",
#     "people walking in airport",
#     "driving on road",
#     "road trip driving",
#     "hotel room interior",
#     "beach vacation"
# ]




QUOTE_KEYWORDS = [
"Anxiety",
"Change",
"Choice",
"Confidence",
"Courage",
"Death",
"Dreams",
"Excellence",
"Failure",
"Fairness",
"Fear",
"Forgiveness",
"Freedom",
"Future",
"Happiness",
"Inspiration",
"Kindness",
"Leadership",
"Life",
"Living",
"Love",
"Pain",
"Past",
"Success",
"Time",
"Today",
"Truth",
"Work"
]




USER_NAME : Final = "Quote of the day"
PROFILE_IMAGE : Final = "logo.png"
PADDING_FROM_IMAGE : Final = 65    
def addUserNameToVideo(video : VideoEditor) -> None:
    video.addText(
        USER_NAME,
        _color="#cdcccc",
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.35), # same as image
        size=(500,50),
        font_size=30,
    )
    
def addMusicToVideo(video : VideoEditor) -> None:
    video.addAudio()
    

def addProfileToVideo(video : VideoEditor) -> None:
    '''
    #### Adds an image preferrable the profile image to the video
    #### Note By Author:
            This function exist because I wanted a way to add my own brand image to stand out.
            Basically any video I posted will contain that image at a certain postion. This will
            mostly be my accounts profile
            
    :param video: Takes an object of the class VideoEditor as an argument
    :type video: VideoEditor
    '''
    video.addImage(
        PROFILE_IMAGE,
        _position = (50,video.target_resolution[1] * 0.35),  #  (width,height)   image should be displayed at 30% from the top
        size = (100,100)
    )
    

def addQuoteToVideoFromInternet(video : VideoEditor) -> None:
    '''
    Requires internet connection to fetch the quotes from the internet.
    
    :param video: object of the `VideoEditor` class
    :type video: VideoEditor
    '''
    quotes = QuoteDownloader(QUOTE_KEYWORDS[randint(0,len(QUOTE_KEYWORDS) - 1)])
    quotes.storeQuotes()
    # quotes = quote.getQuote()
    quotes = quotes.getResults()    # get quotes with author name and gets a random index
    quote = quotes[randint(0,len(quotes) - 1)]
    quoteFormat = f"{quote["quote"]}\n- {quote["author"]}"        # formats quote
    
    video.addText(
        quoteFormat,
        font_size=43,
        # 50 + the position of the image + the width
        _position=(50+150 + PADDING_FROM_IMAGE,video.target_resolution[1] * 0.38),
        # _position=("center","top"),
        _color="#ffffff",
        size=(1080 - (50 + 150 + PADDING_FROM_IMAGE),850)
    )

def addQuoteToVideo(video : VideoEditor,filename : str,index = None) -> None:
    '''
    Fetches quote from file and adds it to video.
    
    This requires each quote to be on a new line
    
    Then a random quote on any of the line is selected
    
    But if you prefer to select an index you can.
    
    
    :param video: object of `VideoEditor` class
    :type video: VideoEditor
    :param filename: directory of file to fetch quote from
    :type filename: str
    '''    
    quotes = []
    with open(filename,"r") as reader:
        results : str = reader.read()
    quotes : list = results.split("\n")
    if index is not None:
        quote = quotes[index]
    else:
        quote : str = quotes[randint(0,len(quotes) - 1)]  # select random quote
    quote_quote = quote.split("-")[0].strip()   # gets only quote from quote data and remove whitespaces
    quote_author = quote.split("-")[1].strip()  # gets only author from quote data and remove whitespaces
    quote_format = f"{quote_quote}\n\n- {quote_author}"
    
    video.addText(
        quote_format,
        font_size = 43,
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
                  _color="#A8A6A6",
                  size=(150,150),
                  _position=(50,
                             video.target_resolution[1] * 0.38 + 100))


def main():
    try:
        # set video file to read data from
        # set audio file to read data from
        video = VideoDownloader(
            video_type=VIDEO_KEYWORDS[randint(0,len(VIDEO_KEYWORDS) - 1)],
            destination="dVideos",verbose=True
            )
        video_filename = video.download()
        mainVideo = VideoEditor(video_filename=video_filename,
                                audio_filename=f"audio/audio {randint(1,5)}.mp3",
                                volume=1,
                                brightness_level=0.4)
    except TypeError as a:
        print("Video query seems invalid", a)
    except Exception as e:
        print("Error during processing: ",e)
        
    else:
        addProfileToVideo(mainVideo)
        addUserNameToVideo(mainVideo)
        # addQuoteToVideoFromInternet(mainVideo)    # requires internet connection
        addQuoteToVideo(mainVideo,"quotes/quotes.txt")
        addDateToVideo(mainVideo)
        addMusicToVideo(mainVideo)

        mainVideo.saveVideo("tiktok1.mp4",threads = 4)
    finally:
        print("Process Completed...")
    
if __name__ == "__main__":
    # TODO: take in arguments and that will decide the name of the file
    main()