MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language
============================================================================================

This package containing the `MS-ASL dataset`, as proposed in MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language paper.  
For more information visit [the website](https://www.microsoft.com/en-us/research/project/ms-asl/).

Contents
-----------------
Adapting the original repository called 'msasl-video-downloader' that is gives errors
The file `IndependentDownload.py` is created to download the adapted 
dataset containing more than 25 occurrences

 * `MSASL_TRAIN25.json`: includes a json file of 16054 train samples.
 * `MSASL_TEST25.json`: includes a json file of 16054 train samples.
 * `MSASL_VAL25.json`: includes a json file of 16054 train samples.
 * `README_Independent.md`: this file.

How it works
---------------
This is a simplified version of the original by stripping away the user interface. 
There is no longer a way to choose which dataset 100, 200 etc. to use.

The script uses the specified json file in line 17 and will go through each video in the list, download the video at the highest resolution and then applies the start time & stop time to the subclip.
The subclip is stored with the '.mp4' extension in the folder path of the specific videos name.
The videos in the temporary 'untrimmed_videos' folder contains all of the full length videos and can be deleted afterwards.

*NOTE that they are not simply overwritten in the code to avoid file corruption that occurs and freezes the video.

What to do
---------------
1. Preferably create env
2. Install requirements
3. Test the script with 1 or 2 videos listen in the json
4. Change the name of the file used in train_json to desired file (eg. `MSASL_TEST25.json`)
5. run script
6. Delete 'untrimmed_videos' folder
7. Move all the videos to desired location
8. Change the script to `MSASL_VAL25.json`
9. Repeat 5 - 7 
10. Repeat 4 - 7 for `MSASL_TRAIN25.json`

Credits
---------------
Licensed under the Computational Use of Data Agreement (C-UDA). Please refer to [C-UDA-0.1_annotated_discussion.pdf](/C-UDA-0.1_annotated_discussion.pdf) for more information.
The original creator of msasl-video-downloader [https://github.com/iamgarcia/msasl-video-downloader.git](https://github.com/iamgarcia/msasl-video-downloader.git)


Citation
--------------

Please cite this in your publications if it help your research:

    `@InProceedings{vaezijoze2019ms-asl,
      author    = {Vaezi Joze, Hamid Reza and Koller, Oscar}
      title     = {MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language},
      booktitle = {The British Machine Vision Conference (BMVC)},
      year      = {2019},
      month = {September}
    }`


Contacts
------------------
- [Hamid Vaezi Joze](https://www.microsoft.com/en-us/research/people/hava/)
- [Oscar Koller](https://www.microsoft.com/en-us/research/people/oskoller/)
