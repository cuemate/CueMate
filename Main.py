import glob
import os
import shutil

#--------------------------------------------Cue Fix
#pull file name from specified extension file 
CueFileDir = glob.glob('*.cue')
#print the first file in the list from the file direcory with .cue extentions
print(CueFileDir[0])

with open(CueFileDir[0], 'r') as CueFile:
    Cuedata=CueFile.read()
	
	#replaces the unsupported char to utf-8 freindly,
	#then (Acute accent or u'\x92') 			to 	(Apostrophe or u"\u0027"), 
	#then (Grave accent or u'\xb4') 			to 	(Apostrophe or u"\u0027"), 
	#then encodes it back to latin-1/ANSI with friendly supported ANSI chars, 
	#this is called FixCueData
FixCueData = Cuedata.replace( u"\u2018" , u"\u0027").replace( u"\u2019" , u"\u0027").replace(u"\u2010" , u"\u002D").replace(u"\u201D" , '').replace(u"\u201C" , '')

#final write to cue file with fixed data
FinalCue = open(CueFileDir[0], "w")
FinalCue.write(str(FixCueData))
FinalCue.close()

#--------------------------------------------WAV/FLAC Fix

#pull file name from specified extension file 
DirNameList = []
print(DirNameList)
#pull file name from specified extension files like wav, flac and soon mp3
DirNameListWAVS = glob.glob('*.wav')
print(DirNameListWAVS)
DirNameListFLACS = glob.glob('*.flac')
print(DirNameListFLACS)
#if wav files exist they will be added the main list
DirNameList = DirNameList + DirNameListFLACS + DirNameListWAVS

#numList is the number of items in list
numList = len(DirNameList)

#empty containter for nanfile list
FixDirNameList = []

#loop variable i from 0 - numlist with steps adding 1 each loop
for i in range(0, numList, 1):
	#replaces the unsupported char to utf-8 freindly,
	#then (Acute accent or u'\x92') 			to 	(Apostrophe or u"\u0027"), 
	#then (Grave accent or u'\xb4') 			to 	(Apostrophe or u"\u0027"), 
	#then encodes it back to latin-1/ANSI with friendly supported ANSI chars, 
	#this is called FixDirName
	FixDirName = DirNameList[i].replace( u"\u2018", u"\u0027").replace( u"\u2019", u"\u0027").replace(u"\u2010", u"\u002D").replace(u"\u201D", '').replace(u"\u201C", '')
	#add the created item to list FixDirNameList
	FixDirNameList.append(FixDirName)
	
for y in range(0,numList,1):
	print(DirNameList[y] + ' to ' + FixDirNameList[y])
	os.rename(os.path.abspath(DirNameList[y]), FixDirNameList[y])
	
#--------------------------------------------create folders

#-------------------1

#glob get all files in directory
allFileList = glob.glob('*')

#how many elements are in the allFileList. call this allFilenumList
allFilenumList = len(allFileList)

#setup for multiple list creation for py, and its nots
py = '.py' or '.pyc'
pyFileList = []
notpyFileList = []

wav = '.wav'
cue = '.cue'
log = '.log' 
file = '.file'
jpeg = '.jpeg'
gif = '.gif'
png = '.png'
jpg = '.jpg'

#if the file has a py in it put it in the pyFileList. if not put it in the notpyFileList
for i in range(0,allFilenumList,1):
	if py in allFileList[i]: 
		pyFileList.append(allFileList[i])
	if wav in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if cue in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if log in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if file in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if jpeg in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if gif in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if png in allFileList[i]: 
		notpyFileList.append(allFileList[i])
	if jpg in allFileList[i]: 
		notpyFileList.append(allFileList[i])
		
	#if os.path.isfile(allFileList[i]) and not pyFileList:
		#notpyFileList.append(allFileList[i])
		
#how many elements are in the notpyFileList. call this numnotpyFileList
numnotpyFileList = len(notpyFileList)
#--------------2 pull title and artist for folder creation and placement
FixCueDataPerformer = FixCueData.find('PERFORMER')
FixCueDataTitle = FixCueData.find('TITLE')
artist = FixCueData[FixCueDataPerformer+11:FixCueDataTitle-2]

		
#-------------------3 folder absolute paths
CueFileName = CueFileDir[0].replace(".cue", "")

if not os.path.exists(artist + '\\' + CueFileName):
    os.makedirs(artist + '\\' + CueFileName)

for i in range(0,numnotpyFileList,1):	
	src0 = os.path.abspath(notpyFileList[i])
	dst0 = os.path.abspath(CueFileDir[0]).replace('\\' + CueFileDir[0], '\\' + artist + "\\" + CueFileDir[0].replace(".cue", "\\").replace('.','') + notpyFileList[i])
	shutil.move(src0, dst0)
