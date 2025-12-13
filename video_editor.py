from moviepy import *
clip = VideoFileClip("videos/3971351.mp4",fps_source="fps",target_resolution=(1080,1920))
print("Duration:",clip.duration)
print("FPS:",clip.fps)
print("Size:",clip.size)
txt_clip = TextClip(
        text="Testing the text interface",
        font_size=70,
        color="white"
    )
txt_clip = txt_clip.with_position("center").with_duration(clip.duration)
video = CompositeVideoClip([clip,txt_clip])
video.write_videofile("result.mp4")

