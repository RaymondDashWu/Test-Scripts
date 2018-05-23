# Summary of Learnings

[![Tensorflow Logo](https://avatars0.githubusercontent.com/u/15658638?s=200&v=4)](https://github.com/tensorflow)

Updated 5/22/18

#### The Project
This project started off as a way for me to practice Tensorflow. I had done various tutorials  from Andrew Ng on Coursera and Sentdex on YouTube but those were lessons with predictable results. This was my first foray using knowledge that I've gained. The idea was to train Tensorflow to recognize empty parking spaces in a parking lot or structure using security cameras that the lots already had installed. These are typically at a high angle above the parking lot. That's when lightbulbs started coming on. There was bound to be plenty of footage online of people shooting footage over parking lots now that consumer drones are available and affordable.

Pie-in-the-sky this classifier could be used to make it easier for people to find parking in heavily populated cities like Los Angeles, New York, San Francisco, etc. It could be part of an app that is used to find out how many parking spaces are in a lot after using GPS to get to a destination. This way a GPS app can better suggest a parking location, parking attendant duties can be partially automated in that they won't have to signal oncoming cars with flags to indicate that there's parking, and less time is wasted on the consumer side if the parking lot is full. 

#### Method
Images were downloaded en masse via a Google image search for "parking lots". A total of 101 (20 test and 81 training) images were collected this way and then each empty parking spaces was labeled by hand via [LabelImg](https://github.com/tzutalin/labelImg). These can be found in [here](https://github.com/RaymondDashWu/Test-Scripts/tree/master/Tensorflow_Testing/models/research/object_detection/images). It should be noted that in the case of empty parking lots I limited myself arbitrarily to 10 labels spread over the image for the sake of brevity. From there Tensorflow was trained using the faster_rcnn_inception_v2_coco_2018_01_28 model. I wanted to prevent overfitting of the model so I stopped training at roughly 60,000 and 100,000 steps. Then the model was purposefully overtrained to 200,000 to give myself a visual representation of an overtrained model.

#### Limitations
- I imagine that this classifier would struggle with the various cameras that are being used in parking lots today. Particularly fisheye lenses and low light/night video.
- Images were trained on what could be described as stock images. As a result the images used were of much higher quality than typical security cameras. I was not able to find a compendium of photos featuring real life security parking lot images.
- Not all of my samples had empty parking spaces. I'm not sure if this helps or hinders training as of the writing of this.
- A small sample of 101 images was used
- The condition of parking lots with faintly visible lines or heavy asphalt repairs would make it very difficult to discern, even to a human.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture6.PNG">

#### Results
As was explained earlier testing was stopped at 60,000 and 100,000 steps. These models can be found in the "Backup" folder [here](https://github.com/RaymondDashWu/Test-Scripts/tree/master/Tensorflow_Testing/models/research/object_detection/training). After this I referenced it against some test videos that I pulled from Youtube. There featured aerial drone footage of various parking lots from different angles. They are labeled parkinglot[1-3] and can be found [here](https://github.com/RaymondDashWu/Test-Scripts/tree/master/Tensorflow_Testing/models/research/object_detection).

As with many instances of prototyping there's always the anxiety that something may not work or go wrong. I don't have much experience with Tensorflow so this was a bit more nerve wracking. However, after 3 hours and 60,000 steps later I was glad to see that it was successful. It was able to detect many of the parking spots. However, this was only true for the first video. It was not able to detect parking spaces on the other 2 test videos. I decided that more training was needed.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture.PNG">

At the 100,000 mark I was glad to see that there was marked improvement over the original. As you can see in the following screenshot it was able to identify one more parking spot in the top right of the image. However, I was a bit disappointed that the model still wasn't able to see the spaces at the back of the video. I'm not sure why at this moment. In addition, it was still having difficulty with cross hatched spaces. This was unfortunately the best that I knew how to do at my current level.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture2.PNG">

On the third parking lot video it was finally able to identify multiple parking spots, although not all of them. My current hypothesis is that the shadows caused by sunset is what threw off the model as we can see that it tries to identify a spot at the top middle with a 94% accuracy. I do not currently know why it doesn't detect the spot to the right of it though.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture3.PNG">

This was when I decided to take it to an extreme. At this point I was happy enough with the results I had gotten and wanted to see what an overfitted model would look like. In concept I knew what overfitting was and that any further training would likely cause it. And at 200,000 it seems I was correct. In the first video it detected a previously unrepresented section that was actually part of a building, some spots that were detected at 100,000 were no longer detected, and parking spots that weren't actually empty were now labeled as such. I couldn't have asked for a better representation of overfitting a model!
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture4.PNG">

Last I'm putting in various graphs from Tensorboard. Unfortunately I didn't know what the majority of them mean. I'll list the ones that I do understand though! Looking at the total loss graph we can see that it gradually decreases. While it isn't a super smooth line it eventually levels out after around 80,000 where the losses stay mostly under .05 . That is until we get to right about 200,000 steps. At this point there's a huge spike and the model is overfitted.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture7.PNG">

This learning rate graph baffles me. I know that learning rate gradually decreases over time but according to Tensorboard's graph it leveled out slightly after 40,000. Perhaps when I look at this graph in the future I'll know what this means.
<img src="https://github.com/RaymondDashWu/Test-Scripts/blob/master/Tensorflow_Testing/models/research/object_detection/Capture8.PNG">

#### Future Improvements
- Need more samples from more angles, low light/infrared, and possibly photos featuring fisheye distortion
- Unsure of how to implement regularization or if it would even help
- Testing against videos of indoor parking structure
- Figure out how to ignore handicapped and cross hatched spaces.


TL;DR - I attempted to train an object detection classifier using Tensorflow to look for empty parking spaces from an overhead perspective. The idea would be to integrate it into cameras of participating parking structures/lots and ultimately have an app that would tell you how many parking spots were nearby. It was quite successful in my limited testing but I'd like to learn how to improve it and there are scenarios where I know it wouldn't work.
