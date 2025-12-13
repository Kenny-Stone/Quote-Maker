import time
from video_downloader import VideoDownloader
from quote_downloader import Quote_Downloader
from video_editor import VideoEditor
def storeDataInFile(location : str, data : str):
    with open(location,"a+") as r:
        r.write(data)
def main():
    quotes = Quote_Downloader("fear")
    quote = quotes.getResults()[0]["quote"]
    storeDataInFile(f"quotes/{time.time()}.txt",quote)
    video_edit = VideoEditor("3831853.mp4",shouldReduceBrightness=True)
    video_edit.addText(f"\'{quote}\'")
    # video_edit.addImage("seashore.jpg")
    # video_edit.addText("They buried him along his friends",font_size=70)
    video_edit.saveVideo("trial3.mp4")
    
if __name__ == "__main__":
    main()