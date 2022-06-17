from moviepy import editor

video = editor.VideoFileClip('vid.mp4')
video.audio.write_audiofile('vid.mp3')