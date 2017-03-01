import json
from pprint import pprint
import glob
import os
import shutil
import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
with open('activity_net.v1-3.min.json') as data_file:    
    data = json.load(data_file)

dataref=data["database"]
#pprint(len(dataref))
#videos= glob.glob("")
videos=os.listdir("validation")
str1="t e s t i n g"
str2="t r a i n i n g"
str3="v a l i d a t i o n"
#stind=int(sys.argv[1])
#print('The start index is',stind)
print('The number of videos are',len(videos))
for i in range(1,len(videos)):

	print('Processing video number ',i)
	video=videos[i]
	if video[0]!='v' or video[1]!='_':# or video[len(video)-2]=='1':# or video[len(video)-2]=='2':
		continue
	print('The video is',video)
	vl1=dataref[video[2:len(video)-2]]["annotations"]
	print(vl1)
	v2=dataref[video[2:len(video)-2]]["annotations"]
	seglen=len(v2)
	#print('The segments are',v2)
	#print('The length of segments are',seglen)
	print('The video is',video)
	
	subs=dataref[video[2:len(video)-2]]["subset"]
	vl= " ".join(str(x) for x in vl1)
	s1= " ".join(str(x) for x in subs)
	print('The idenitifed subset is',s1)
		
	#if os.path.isdir('testing/random')==0:
	#	print('Random directry Found')
	if s1==str1:
		print('testing')
		#shutil.copy2(video,'testing')
	if s1==str2:
		print('training')
		start = vl.find('label')+10
                end=vl.find('}',start)-1
                label=vl[start:end]
		newdir='training'+'/'+label
		if os.path.isdir(newdir)==0:
			print('Hi')
			#os.mkdir(newdir)
		for j in range(0,10):
                	#stri=v2[j].items()
                	#seg=stri[0]
                	#t=seg[1]
                	#tstart=t[0]
                	#tend=t[1]
			#orig='training'+
                	#print('The starting and ending time intervals are',tstart,tend)
			vstr='training/'+video[0:len(video)-1]+str(j)
			print('The directory is',vstr)
			if os.path.isdir(vstr):
				print(vstr)
				#shutil.move(vstr,newdir)
			#print('The new target folder is',vstr)
			#shutil.move(vstr,newdir)	
		#shutil.copy2(video,newdir)
                #print(label)
	if s1==str3:
		print('validation')
		start = vl.find('label')+10
		end=vl.find('}',start)-1
		label=vl[start:end]
		newdir='validation'+'/'+label
		if os.path.isdir(newdir)==0:
			print('Hi from validation')
                        os.mkdir(newdir)
		for j in range(0,10):
                	#stri=v2[j].items()
                	#seg=stri[0]
                	#t=seg[1]
                	#tstart=t[0]
                	#tend=t[1]
                	#print('The starting and ending time intervals are',tstart,tend)
			vstr='validation/'+video[0:len(video)-1]+str(j)
                        print('The directory is',vstr)
			print('The storing directory is',newdir)
			if os.path.isdir(vstr):
				print(vstr)
				shutil.move(vstr,newdir)	
		#shutil.copy2(video,newdir)

	#print(dataref[video[2:len(video)-4]]["annotations"])
	#print(dataref[video[2:len(video)-4]]["subset"])
	


