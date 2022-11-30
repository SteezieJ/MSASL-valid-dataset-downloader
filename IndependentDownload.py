import os
import shutil
import json
from pytube import YouTube
from moviepy.editor import *
import moviepy.editor as mpy


# where to save
SAVE_PATH = "MS-ASL100"  # to_do
temp_path = SAVE_PATH + "/untrimmed_videos"

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
if not os.path.exists(temp_path):
    os.makedirs(temp_path)

try:

    # replace test name with each of the desired files.
    # first test 1 video, then list of 2, then the test or val set.
    # the following files are included
    # MSASL_test.json, MSASL_TEST25.json, MSASL_VAL25.json, MSASL_TRAIN25.json
    train_json = open('MSASL_test.json')
    videos = json.load(train_json)
    train_json.close()
except:
    print("Connection Error")

# loop through the videos in the dataset
len = len(videos)
for i in range(len):
    try:
        # setup reads info from json and creates groups videos by name
        url = videos[i]['url']
        start_time = videos[i]['start_time']
        end_time = videos[i]['end_time']
        label = videos[i]['label']
        pretitle = videos[i]['clean_text']
        video_title = pretitle + str(i)
        output_title = video_title + ".mp4"
        temp_file_path = temp_path + "/" + video_title

        folder_path = SAVE_PATH + "/" + pretitle
        output_path = folder_path + "/" + video_title

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        print(video_title)
        print('Setup Completed!')

        # If video is private or not exist it will give error and go to next
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        # stream = yt.streams.get_highest_resolution()

        streamclip = stream.download(temp_path, video_title)        #untrimmed-> afraid5
        print('Download Completed!')

        # the downloaded full video is saved as subclip
        clip = VideoFileClip(temp_file_path).subclip(start_time, end_time)
        output = os.path.join(folder_path, output_title)            #afraid-> afraid5.mp4
        clip.write_videofile(output)
        print('Task Completed!')

    #     note that the temp file is still there, add .mp4 to the filename for the full video
    #     Without keeping it and simply overwriting corrupts the output file
    #     To add the mp4 extension to them use output_title instead of video_title in temp_file_path
    except:
        print("Some Error!")


        # # Actually saves the trimmed file
        # clip.write_videofile(filename=f"trimmed_{uniqueid}.mp4", codec="libx264", audio_codec="aac", remove_temp=True)