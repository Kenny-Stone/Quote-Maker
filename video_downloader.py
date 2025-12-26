'''Downloads video from pexels using your API_KEY'''
import requests
from envReader import *
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

        self.API_KEY = getEnv("api_key")        # get's value from .env file
        self.headers = {"Authorization" :self.API_KEY}
        self.response = requests.get(self.url,headers=self.headers,params=self.params)
    
    def getVideoDetails(self):
        return self.response
    def download(self):
        try:
            for video in self.response.json()["videos"]:
                if video["duration"] <= self.video_duration:
                    file_url = video["video_files"][0]["link"]
                    with requests.get(file_url,stream=True) as r:
                        r.raise_for_status()
                        if self.destination == None:
                            self.filename = f"{video["id"]}.mp4"
                        else:
                            self.filename = f"{self.destination}/{video["id"]}.mp4"
                        with open(self.filename,"wb") as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                if chunk:    
                                    f.write(chunk)
                        if self.verbose:
                            print("Title", video.get("id"))
                            print("Download URL:",file_url)
                    print("Downloaded:",self.filename,"\n")
        except KeyError:
            print("Video Query seems invalid or is not allowed.")