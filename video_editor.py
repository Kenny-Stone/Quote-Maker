from moviepy import *
from PIL import Image, ImageFilter
class VideoEditor:
    def __init__(self,filename,shouldReduceBrightness : bool = False,_target_resolution = (1080,1920)):
        self.clips = []    # stores video to be added to clips
        self.filename = filename    # filename of video data to be read
        self.target_resolution = _target_resolution # preferred_resolution for video
        self.main_video_clip = VideoFileClip(filename,fps_source="fps",target_resolution=self.target_resolution,is_mask=True)    # main video that serves as background overlay
        if shouldReduceBrightness:
            self.main_video_clip = self.main_video_clip.with_effects([vfx.MultiplyColor(0.5)])
        self.main_video_clip.memoize = True
        self.clips.append(self.main_video_clip)    # adds main video to video list
    def addText(self,_text : str,font_size : int = 60 ,_color : str ="#000000",_bg_color : str = None,isCentered : bool = True,duration="complete",_font=None):
        txt_clip = TextClip(
            text=_text,
            font_size=font_size,
            color=_color,
            bg_color=_bg_color,
           font=_font,
        )
        txt_clip.memoize = True
        if isCentered:
            txt_clip = txt_clip.with_position("center")     # centers text
        if duration=="complete":
            txt_clip = txt_clip.with_duration(self.main_video_clip.duration)    # shows text until end of video
        else:
            txt_clip = txt_clip.with_duration(duration)     # shows text for value of duration in seconds
        self.clips.append(txt_clip)    # adds text to video list since it's also a clip
    def addImage(self,_img_location,_position = "center",_size = (20,20),_is_mask: bool = False,_is_transparent : bool = True):
        image_clip = ImageClip(_img_location,is_mask=_is_mask,transparent=_is_transparent,duration=self.main_video_clip.duration)
        image_clip.memoize = True
        image_clip.with_position(_position)
        image_clip.resized(_size)
        self.clips.append(image_clip)  # adds image to clip
        
    def saveVideo(self,edited_video_name):
        video = CompositeVideoClip(self.clips)
        video.memoize = True
        video.write_videofile(edited_video_name,fps=self.main_video_clip.fps)
        video.close()       # closes video writing
        print("Video saved successfully!")