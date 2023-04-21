from pathlib import Path
import moviepy.editor


video_path = Path('test_video.mp4')

video = moviepy.editor.VideoFileClip(f'{video_path}')
audio = video.audio
audio.write_audiofile(f'{video_path.stem}.mp3')
