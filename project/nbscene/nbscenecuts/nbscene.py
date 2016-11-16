import re
import scenedetect
fp = open("nbscene.txt","w")
fread= open("filename.txt","r")

for line in fread.readlines():
	videoname1 = str(line)
	videoname = videoname1[:-1]
	print(videoname),
	scene_list = []        # Scenes will be added to this list in detect_scenes().
	path = videoname  # Path to video file.

	# Usually use one detector, but multiple can be used.
	detector_list = [
	    scenedetect.detectors.ContentDetector(threshold = 30 )
	]

	video_framerate, frames_read = scenedetect.detect_scenes_file(
	    path, scene_list, detector_list)

	# scene_list now contains the frame numbers of scene boundaries.
	#print scene_list
	fp.write("%s - %s"%(videoname,str(len(scene_list))))
	fp.write("\n")
