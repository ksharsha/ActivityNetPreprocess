# ActivityNetPreprocess
Scripts useful to parse ActivityNet dataset.

Download the Activity Net dataset using the [crawler]:https://github.com/activitynet/ActivityNet 

place the ActivityNetparser.py file in the same directory and create three sub directories training, testing, validation.

Make sure you have ffmpeg installed, if not install it from [here]:https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg .

Install moviepy from [here]:http://zulko.github.io/moviepy/install.html 

place the json file containing the activity net data in the same directory.

Then run this command "python ActivityNetParser.py" in the command line.

This would parse the videos in the current directory, trim the videos according to the duration in which the action is taking place in the current video and puts it inside (or creates if it fdoesn't exist) a folder having the name of the action class inside the  training/testing/validation folder accordingly.
