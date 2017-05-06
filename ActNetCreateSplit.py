import os
import fnmatch

#Opening the file to write
text_file = open("ActNetTrainSplit.txt", "w")
def countframes(filelist):
	rgb_prefix = 'img_'
	flow_x_prefix = 'flow_x_'
	flow_y_prefix = 'flow_y_'
	prefix_list = (rgb_prefix, flow_x_prefix, flow_y_prefix)
	cnt_list=[len(fnmatch.filter(filelist, x+'*')) for x in prefix_list]
	return cnt_list

f=open("/data01/mscvproject/code/temporal-segment-networks/data/ActNet_splits/ActNetClasses.txt")
classes=f.read()
classeslist=classes.split("\n")
#cdict will be a dictionary containing the mapping from the class name to its index
cdict={}
for i in range(0,200):
	d=classeslist[i]
	e=d.split(":")
	str1=(str(e[0]))
	cdict[str1]=int(e[1])


print(len(cdict))
#We will now go into all the directories and create the split file
classnames = [name for name in os.listdir(".") if os.path.isdir(name)]
for i in range(0,len(classnames)):
	print('In the directory number',i)
	index = cdict[classnames[i]]
	substr = "./" + str(classnames[i])
	#print('The sub folder is',substr)
	for root, dirs, files in os.walk(substr):
		subroot=root.split("/")
		#We want the directories inside the labels only
		if(len(subroot)==3):
			#print(subroot)
			rootpath=str(os.path.dirname(os.path.abspath(root))) + "/" +  subroot[2]
			filepath = substr + "/" +  subroot[2]
			#print(rootpath)
			#print(filepath)
			for rootsub, dirsub, filesub in os.walk(filepath):
				counts=countframes(filesub)
				#print(min(counts))
				#Taking minimum just to be on the safe side, ideally they should be equal
				if min(counts)>0 :
					finalpath = rootpath + " " + str(min(counts)) + " " + str(index)
					#print(finalpath)
					text_file.write("{}\n" .format(finalpath))



text_file.close()
	#print('The number of subdirectories inside this folder is',len(subclasses))
