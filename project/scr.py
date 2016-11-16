import scenedetect

scene_list = []        # Scenes will be added to this list in detect_scenes().
for i in range(10):
	scene_list = []   
	path = 'ACCEDE0000'+str(i)+'.mp4'  # Path to video file.

	# Usually use one detector, but multiple can be used.
	detector_list = [
	    scenedetect.detectors.ThresholdDetector(threshold = 8, min_percent = 0.5)
	]

	video_framerate, frames_read = scenedetect.detect_scenes_file(
	    path, scene_list, detector_list)

	# scene_list now contains the frame numbers of scene boundaries.
	print(len(scene_list))#.size()
	print(scene_list)
