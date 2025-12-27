from moviepy import *
class VideoEditor:
    '''
    :param audio_filename: If audio filename is empty there will be no audio in the video
    and also the function call to addAudio will be invalid and will raise an error
    :type audio_filename: str
    '''
    def __init__(
        self,
        video_filename,
        audio_filename = None,
        brightness_level : float = 1,
        target_resolution = (1080,1920),
        #uses default volume if None
        volume = None,
        ):  # new parameter for mask handling
    
        self.clips = []    # stores video to be added to clips
        self.audio_clip = None
        self.video_filename = video_filename    # video_filename of video data to be read
        self.audio_filename = audio_filename     # filename of audio data to be read
        self.target_resolution = target_resolution # preferred_resolution for video
        self.volume = volume
        self.main_video_clip = VideoFileClip(video_filename, fps_source="fps",
                                             target_resolution=self.target_resolution,
                                             is_mask=True)  # main video that serves as background overlay
        self.main_video_clip = self.main_video_clip.with_effects([vfx.MultiplyColor(brightness_level)]) # reduces video brightness level
        self.main_video_clip = self.main_video_clip.with_memoize(True)
        self.clips.append(self.main_video_clip)    # adds main video to video list
        
    def addText(self,_text : str,font_size : int = 60 ,
                _color : str ="#000000",
                _bg_color : str = None,
                _position = (50,50),
                duration="complete",
                _font=None,
                size=(100,100)):
        '''
        :param _text: Text to be added to video
        :type _text: str
        :param font_size: font size of text
        :type font_size: int
        :param _color: color of text eg: `#f4f4f4`
        :type _color: str
        :param _bg_color: background color of text
        :type _bg_color: str
        :param isCentered: sets text to be centered
        :type isCentered: bool
        :param duration: seconds text should be shown on video. Use default if you want
        it to be displayed till end of video
        :param _font: The font to render the text in. NOTE: use location of the font not just the name
        '''
        txt_clip = TextClip(
            text=_text,
            font_size=font_size,
            color=_color,
            bg_color=_bg_color,
           font=_font,
           size=size,
           horizontal_align="left",
           vertical_align="left",
           method="caption"
        )
        txt_clip = txt_clip.with_memoize(True)
        txt_clip = txt_clip.with_position(_position)
        if duration=="complete":
            txt_clip = txt_clip.with_duration(self.main_video_clip.duration)    # shows text until end of video
        else:
            txt_clip = txt_clip.with_duration(duration)     # shows text for value of duration in seconds
        self.clips.append(txt_clip)    # adds text to video list since it's also a clip
        
        
    def addImage(self,_img_location,_position = ("center","center"),
                 size = (20,20),_is_mask: bool = False,_is_transparent : bool = True):
        '''
        :param _img_location: The location of the image to be added.
        :type _img_location: str
        :param _position: position of the image which is a `tuple`. eg (`center`,`left`),`(50,50)`
        :type _position: str | tuple
        :param _size: The size to be used for the image. reduces the image to the specified `width`,`height` or `both`.
        :type _size: tuple | float
        :param _is_mask: Description
        :type _is_mask: bool
        :param _is_transparent: Set to true if you wan't image to be transparent
        :type _is_transparent: bool
        '''
        image_clip  = ImageClip(
            _img_location,
            is_mask=_is_mask,
            transparent=_is_transparent,
            duration=self.main_video_clip.duration).resized(width=size[0],height=size[1]
        )
        image_clip = image_clip.with_memoize(True)
        image_clip = image_clip.with_position(_position)
        # image_clip.with_effects([vfx.Resize(_size)])      # resizes image
        self.clips.append(image_clip)  # adds image to clip
        
    def addAudio(self):
        if self.audio_filename is None:
            raise AttributeError("Sound file not found. Make sure to include audio file in constructor before calling this function")
        
        # create audio clip object
        
        # if self.volume is not None:
        audio_clip : AudioFileClip = AudioFileClip(filename=self.audio_filename)
        # audio_clip = audio_clip.with_volume_scaled(self.volume)
        # audio_clip = audio_clip.set_duration(self.main_video_clip.duration)  # makes audio duration same as video duration
        # audio_clip.duration = self.main_video_clip.duration
        # add audio to video clip
        audio_clip = audio_clip.with_duration(self.main_video_clip.duration)
        self.audio_clip = audio_clip
        # if user sets volume
        self.main_video_clip = self.main_video_clip.with_audio(audio_clip)
        # replace the first clip with the new one since moviepy is immutable the array is storing
        # the previous clip that do not contain a sound
        # the first video is created as soon as the class is created
        self.clips[0] = self.main_video_clip    
        # self.main_video_clip.audio = audio_clip
        
        
        
        
    def saveVideo(self,edited_video_name,threads=None):
        video : CompositeVideoClip = CompositeVideoClip(self.clips)
        print(self.clips)
        video = video.with_memoize(True)
        video.write_videofile(edited_video_name,
                            audio_codec = "aac",
                            codec="libx264",
                            temp_audiofile = "temp-audio.m4a",
                            fps=self.main_video_clip.fps,
                            audio_bitrate="192k",
                            remove_temp = True,
                            threads=threads)
        video.close()       # closes video writing
        print("Video saved successfully!")
        
