####################################################################################################
#	Helper file for Plex2CSV
# Written by dane22 on the Plex Forums, UKDTOM on GitHub
#
# This one contains the valid fields and attributes for movies
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
singleCall = ['Level 1', 'Level 2']

# Define rows and element name for level 1 (Single call)
Level_1 = [
	('Media ID' , '@ratingKey'),
	('Title' , '@title'),
	('Sort title' , '@titleSort'),
	('Studio' , '@studio'),
	('Content Rating' , '@contentRating'),
	('Year' , '@year'),
	('Rating' , '@rating'),
	('Summary' , '@summary'),
	('Genres' , 'Genre/@tag')
]	

# Define rows and element name for level 2 (Single Call)
Level_2 = [
	('View Count' , '@viewCount'),
	('Last Viewed at' , '@lastViewedAt'),
	('Tagline' , '@tagline'),
	('Release Date' , '@originallyAvailableAt'),
	('Writers' , 'Writer/@tag'),
	('Country' , 'Country/@tag'),
	('Duration' , '@duration'),
	('Directors' , 'Director/@tag'),
	('Roles' , 'Role/@tag')
	]

# Define rows and element name for level 3 (One call pr. movie)
Level_3 = [
	('Labels' , 'Label/@tag'),
	('Locked Fields' , 'Field/@name'),
	('Extras' , 'Extras/@size'),
	('Collections' , 'Collection/@tag'),
	('Original Title' , '@originalTitle'),
	('Added' , '@addedAt'),	
	('Updated' , '@updatedAt'),
	('Audio Languages' , 'Media/Part/Stream[@streamType=2]/@languageCode'),	
	('Audio Title' , 'Media/Part/Stream[@streamType=2]/@title'),
	('Subtitle Languages' , 'Media/Part/Stream[@streamType=3]/@languageCode'),
	('Subtitle Title' , 'Media/Part/Stream[@streamType=3]/@title'),
	('Subtitle Codec' , 'Media/Part/Stream[@streamType=3]/@codec'),
	('Accessible' , 'Media/Part/@accessible'),	
	('Exists' , 'Media/Part/@exists'),
	('MetaDB Link' , '@guid'),
	('Poster url' , '@thumb'),
	('Art url' , '@art')
	]

# Define rows and element name for level 4 (One call pr. movie)
Level_4 = [
	('Video Resolution' , 'Media/@videoResolution'),
	('Bitrate' , 'Media/@bitrate'),
	('Width' , 'Media/@width'),
	('Height' , 'Media/@height'),
	('Aspect Ratio' , 'Media/@aspectRatio'),
	('Audio Channels' , 'Media/@audioChannels'),
	('Audio Codec' , 'Media/@audioCodec'),
	('Video Codec' , 'Media/@videoCodec'),
	('Container' , 'Media/@container'),
	('Video FrameRate' , 'Media/@videoFrameRate')
	]

# Define rows and element name for level 5 (Part info) (One call pr. movie)
Level_5 = [
	('Part File' , 'Media/Part/@file'),
	('Part Size' , 'Media/Part/@size'),
	('Part Size as Bytes' , 'Media/Part/@size'),
	('Part Indexed' , 'Media/Part/@indexes'),
	('Part Duration' , 'Media/Part/@duration'),
	('Part Container' , 'Media/Part/@container'),
	('Part Optimized for Streaming' , 'Media/Part/@optimizedForStreaming')
	]

# Define rows and element name for level 6 (Video Stream Info) (One call pr. movie)
Level_6 = [
	('Video Stream Title' , 'Media/Part/Stream[@streamType=1]/@title'),
	('Video Stream Default' , 'Media/Part/Stream[@streamType=1]/@default'),
	('Video Stream Index' , 'Media/Part/Stream[@streamType=1]/@index'),
	('Video Stream Pixel Format' , 'Media/Part/Stream[@streamType=1]/@pixelFormat'),
	('Video Stream Profile' , 'Media/Part/Stream[@streamType=1]/@profile'),
	('Video Stream Ref Frames' , 'Media/Part/Stream[@streamType=1]/@refFrames'),
	('Video Stream Scan Type' , 'Media/Part/Stream[@streamType=1]/@scanType'),
	('Video Stream Stream Identifier' , 'Media/Part/Stream[@streamType=1]/@streamIdentifier'),
	('Video Stream Width' , 'Media/Part/Stream[@streamType=1]/@width'),
	('Video Stream Pixel Aspect Ratio' , 'Media/Part/Stream[@streamType=1]/@pixelAspectRatio'),
	('Video Stream Height' , 'Media/Part/Stream[@streamType=1]/@height'),
	('Video Stream Has Scaling Matrix' , 'Media/Part/Stream[@streamType=1]/@hasScalingMatrix'),
	('Video Stream Frame Rate Mode' , 'Media/Part/Stream[@streamType=1]/@frameRateMode'),
	('Video Stream Frame Rate' , 'Media/Part/Stream[@streamType=1]/@frameRate'),
	('Video Stream Codec' , 'Media/Part/Stream[@streamType=1]/@codec'),
	('Video Stream Codec ID' , 'Media/Part/Stream[@streamType=1]/@codecID'),
	('Video Stream Chroma Sub Sampling' , 'Media/Part/Stream[@streamType=1]/@chromaSubsampling'),
	('Video Stream Cabac' , 'Media/Part/Stream[@streamType=1]/@cabac'),
	('Video Stream Anamorphic' , 'Media/Part/Stream[@streamType=1]/@anamorphic'),
	('Video Stream Language Code' , 'Media/Part/Stream[@streamType=1]/@languageCode'),
	('Video Stream Language' , 'Media/Part/Stream[@streamType=1]/@language'),
	('Video Stream Bitrate' , 'Media/Part/Stream[@streamType=1]/@bitrate'),
	('Video Stream Bit Depth' , 'Media/Part/Stream[@streamType=1]/@bitDepth'),
	('Video Stream Duration' , 'Media/Part/Stream[@streamType=1]/@duration'),
	('Video Stream Level' , 'Media/Part/Stream[@streamType=1]/@level'),
	('Audio Stream Selected' , 'Media/Part/Stream[@streamType=2]/@selected'),
	('Audio Stream Default' , 'Media/Part/Stream[@streamType=2]/@default'),
	('Audio Stream Codec' , 'Media/Part/Stream[@streamType=2]/@codec'),
	('Audio Stream Index' , 'Media/Part/Stream[@streamType=2]/@index'),
	('Audio Stream Channels' , 'Media/Part/Stream[@streamType=2]/@channels'),
	('Audio Stream Bitrate' , 'Media/Part/Stream[@streamType=2]/@bitrate'),
	('Audio Stream Language' , 'Media/Part/Stream[@streamType=2]/@language'),
	('Audio Stream Language Code' , 'Media/Part/Stream[@streamType=2]/@languageCode'),
	('Audio Stream Audio Channel Layout' , 'Media/Part/Stream[@streamType=2]/@audioChannelLayout'),
	('Audio Stream Bit Depth' , 'Media/Part/Stream[@streamType=2]/@bitDepth'),
	('Audio Stream Bitrate Mode' , 'Media/Part/Stream[@streamType=2]/@bitrateMode'),
	('Audio Stream Codec ID' , 'Media/Part/Stream[@streamType=2]/@codecID'),
	('Audio Stream Duration' , 'Media/Part/Stream[@streamType=2]/@duration'),
	('Audio Stream Profile' , 'Media/Part/Stream[@streamType=2]/@profile'),
	('Audio Stream Sampling Rate' , 'Media/Part/Stream[@streamType=2]/@samplingRate'),
	('Subtitle Stream Codec' , 'Media/Part/Stream[@streamType=3]/@codec'),
	('Subtitle Stream Index' , 'Media/Part/Stream[@streamType=3]/@index'),
	('Subtitle Stream Language' , 'Media/Part/Stream[@streamType=3]/@language'),
	('Subtitle Stream Language Code' , 'Media/Part/Stream[@streamType=3]/@languageCode'),
	('Subtitle Stream Codec ID' , 'Media/Part/Stream[@streamType=3]/@codecID'),
	('Subtitle Stream Format' , 'Media/Part/Stream[@streamType=3]/@format'),
	('Subtitle Stream Title' , 'Media/Part/Stream[@streamType=3]/@title'),
	('Subtitle Stream Selected' , 'Media/Part/Stream[@streamType=3]/@selected')
	]

# Define rows and element name for extreme level 7 (One call pr. movie)
Level_7 = [
	]

# Define rows and element name for extreme level 8 (One call pr. movie)
Level_8 = [
	]

# Define rows and element name for extreme level 9 (One call pr. movie)
Level_9 = {
	}

# Define rows and element name for level 666 (Two calls pr. movie)
Level_666 = [
#	('PMS Media Path' , 'hash')   # Field auto added
	]

# Define rows and element name for Special level 1 (one call pr. movie)
SLevel_1 = [
	('Title' , '@title'),
	('Year' , '@year'),
	('Release Date' , '@originallyAvailableAt'),
	('Audio Languages' , 'Media/Part/Stream[@streamType=2]/@languageCode')
	]

# Define rows and element name for Special level 2 (one call pr. movie)
SLevel_2 = [
	]

# Define rows and element name for Special level 3 (one call pr. movie)
SLevel_3 = [
	]

# Define rows and element name for Special level 4 (one call pr. movie)
SLevel_4 = [
	]

# Define rows and element name for Special level 4 (two call pr. movie)
SLevel_666 = [
	]

# Define rows and element name for Special level 4 (two call pr. movie)
SLevel_666_2 = [
	]


