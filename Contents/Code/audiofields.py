####################################################################################################
#	Helper file for Plex2CSV
# Written by dane22 on the Plex Forums, UKDTOM on GitHub
#
# This one contains the valid fields and attributes for audio
# 
# To disable a field not needed, simply put a # sign in front of the line, and it'll be ommited.
# After above, a PMS restart is sadly req. though
# Note though, that this will be overwritten, if/when this plugin is updated
#
# If level has the number 666 in it, a column named 'PMS Media Path' will
# automaticly be added to the end
####################################################################################################

# Fields that contains a timestamp and should return a date
dateTimeFields = ['addedAt', 'updatedAt', 'lastViewedAt']

# Fields that contains a timestamp and should return a time
timeFields =['duration']

# Levels that only req. a single call towards PMS
singleCall = ['Level 1', 'Level 2', 'Level 3', 'Level 4']

# Define rows and element name for level 1 (Single call)
Level_1 = [
	('Track ID' , '@ratingKey'),
	('Title' , '@title'),
	('Artist' , '@grandparentTitle'),
	('Album' , '@parentTitle')
	]	

Level_2 = [
	('Rating Count' , '@ratingCount'),
	('Track No' , '@index'),
	('Duration' , '@duration'),
	('Added' , '@addedAt'),
	('Updated' , '@updatedAt')
	]

Level_3 = [
	('Media ID' , 'Media/@id'),
	('Bitrate' , 'Media/@bitrate'),
	('Audio Channels' , 'Media/@audioChannels'),
	('Audio Codec' , 'Media/@audioCodec'),
	('Container' , 'Media/@container'),
	('Media Title' , 'Media/@title')
	]

Level_4 = [
	('Part Duration' , 'Media/Part/@duration'),
	('Part File' , 'Media/Part/@file'),
	('Part Size' , 'Media/Part/@size'),
	('Part Container' , 'Media/Part/@container')
	]

Level_5 = [
	('Stream Selected' , 'Media/Part/Stream[@streamType=2]/@selected'),
	('Stream Codec' , 'Media/Part/Stream[@streamType=2]/@codec'),
	('Stream Index' , 'Media/Part/Stream[@streamType=2]/@index'),
	('Stream Channels' , 'Media/Part/Stream[@streamType=2]/@channels'),
	('Stream Bitrate' , 'Media/Part/Stream[@streamType=2]/@bitrate'),
	('Stream Audio Channel Layout' , 'Media/Part/Stream[@streamType=2]/@audioChannelLayout'),
	('Stream Bitrate Mode' , 'Media/Part/Stream[@streamType=2]/@bitrateMode'),
	('Stream Duration' , 'Media/Part/Stream[@streamType=2]/@duration'),
	('Stream Sampling Rate' , 'Media/Part/Stream[@streamType=2]/@samplingRate')
	]

Level_6 = [
	]

Level_7 = [
	]

Level_8 = [
	]

Level_9 = [
	]

Level_666 = [
	]


