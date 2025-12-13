from video_downloader import VideoDownloader
from quote_downloader import Quote_Downloader
def main():
    quotes = Quote_Downloader("money")
    results = quotes.getResults()
    for result in results:
        print(f"{result["quote"]} - {result["author"]}")
    # video = VideoDownloader("friends",15,2,destination="videos")
    # video.download()

if __name__ == "__main__":
    main()