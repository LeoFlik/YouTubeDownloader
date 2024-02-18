from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def download_file(url, save_path,progress_callback):
    
    try:
        if url and save_path:
            yt = YouTube(url, on_progress_callback=progress_callback)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            video_filename = os.path.splitext(os.path.basename(highest_res_stream.download(output_path=save_path)))[0]

            # Extract audio from the downloaded video
            video_clip = VideoFileClip(os.path.join(save_path, f"{video_filename}.mp4"))
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(os.path.join(save_path, f"{video_filename}_audio.mp3"))

            # Close the video and audio clips
            video_clip.close()
            audio_clip.close()
            
            return True
    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")
        return False

