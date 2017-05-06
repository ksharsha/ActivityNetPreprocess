import os
classes = [name for name in os.listdir(".") if os.path.isdir(name)]
print('The number of directories present in this folder are',len(classes))
#print(classes)
text_file = open("ActNetClasses.txt", "w")
for i in range(0,len(classes)):
	text_file.write("{}: {}\n" .format(classes[i], i+1))

text_file.close()
