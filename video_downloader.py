import requests
class VideoDownloader:
    def __init__(self,video_type,video_duration=15,video_count=1,destination=None,verbose=True):
        self.url = "https://api.pexels.com/videos/search"
        self.video_type = video_type
        self.video_duration = video_duration
        self.video_count = video_count
        self.verbose = verbose
        self.destination = destination
        self.params = {"query" : self.video_type,"per_page": video_count}
        self.filename = None
        #TODO: store the API_KEY in an .env
        self.API_KEY = "3tNf3w5a65QOZ51YF9P95QNbcdABv6PhTBtSeD3LRdTaJbU0J553JRr"
        self.headers = {"Authorization" :self.API_KEY}
        self.response = requests.get(self.url,headers=self.headers,params=self.params)
    
    def getVideoDetails(self):
        return self.response
    def download(self):
        try:
            for video in self.response.json()["videos"]:
                if video["duration"] <= self.video_duration:
                    file_url = video["video_files"][0]["link"]
                    video_bytes = requests.get(file_url).content
                    if self.destination == None:
                        self.filename = f"{video["id"]}.mp4"
                    else:
                        self.filename = f"{self.destination}/{video["id"]}.mp4"
                    with open(self.filename,"wb") as f:
                        f.write(video_bytes)
                    if self.verbose:
                        print("Title", video.get("id"))
                        print("Download URL:",file_url)
                    print("Downloaded:",self.filename,"\n")
        except KeyError:
            print("Video Query seems invalid or is not allowed.")