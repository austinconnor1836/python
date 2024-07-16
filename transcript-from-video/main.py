from moviepy.editor import VideoFileClip
import speech_recognition as sr
import os

def video_to_transcript(video_path, audio_path="extracted_audio.wav", transcript_path="transcript.txt"):
    # Extract audio from video
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    audio_file = sr.AudioFile(audio_path)
    
    # Recognize the speech in the audio file
    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    # Save the transcript to a text file
    with open(transcript_path, "w") as file:
        file.write(text)
    
    return text

# Get paths from environment variables
video_path = os.getenv('VIDEO_PATH', 'default_video_path.mp4')
audio_path = os.getenv('AUDIO_PATH', 'default_audio_path.wav')
transcript_path = os.getenv('TRANSCRIPT_PATH', 'default_transcript.txt')

# Usage
transcript = video_to_transcript(video_path, audio_path, transcript_path)
print(f"Transcript saved to {transcript_path}")
