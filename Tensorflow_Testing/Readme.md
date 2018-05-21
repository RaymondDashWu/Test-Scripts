# Summary of Learnings

[![Tensorflow Logo](https://avatars0.githubusercontent.com/u/15658638?s=200&v=4)](https://github.com/tensorflow)



#### The Project
This project started off as a way for me to practice Tensorflow. I had done various tutorials  from Andrew Ng on Coursera and Sentdex on YouTube but those were lessons with predictable results. This was my first foray using knowledge that I've gained. The idea was to train Tensorflow to recognize empty parking spaces in a parking lot or structure using security cameras that the lots already had installed. These are typically at a high angle above the parking lot. That's when lightbulbs started coming on. There was bound to be plenty of footage online of people shooting footage over parking lots now that consumer drones are available and affordable.

Pie-in-the-sky this classifier could be used to make it easier for people to find parking in heavily populated cities like Los Angeles, New York, San Francisco, etc. It could be part of an app that is used to find out how many parking spaces are in a lot after using GPS to get to a destination. This way a GPS app can better suggest a parking location, parking attendant duties can be partially automated in that they won't have to signal oncoming cars with flags to indicate that there's parking, and less time is wasted on the consumer side if the parking lot is full. 

#### Method
Images were downloaded en masse via a Google image search for "parking lots". A total of 101 (20 test and 81 training) images were collected this way and then each empty parking spaces was labeled by hand via [LabelImg](https://github.com/tzutalin/labelImg). It should be noted that in the case of empty parking lots I limited myself arbitrarily to 10 labels spread over the image for the sake of brevity. From there Tensorflow was trained using the faster_rcnn_inception_v2_coco_2018_01_28 model. I wanted to prevent overfitting of the model so I stopped training at roughly 60,000 and 100,000 steps. Then the model was purposefully overtrained to 200,000 to give myself a visual representation of an overtrained model.

#### Limitations
- I imagine that this classifier would struggle with the various cameras that are being used in parking lots today. Particularly fisheye lenses and low light/night video.
- Images were trained on what could be described as stock images. As a result the images used were of much higher quality than typical security cameras. I was not able to find a compendium of photos featuring real life security parking lot images.
- ? Not all of my samples had empty parking spaces. I'm not sure if this helps or hinders training as of the writing of this.
- A small sample of 101 images was used
- The condition of parking lots with faintly visible lines or heavy asphalt repairs would make it very difficult to discern, even to a human.
- - ??? INSERT IMAGE
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF


- - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)

#### Results

#### Future Improvements

TL;DR - I attempted to train an object detection classifier using Tensorflow to look for empty parking spaces from an overhead perspective. The idea would be to integrate it into cameras of participating parking structures/lots and ultimately have an app that would tell you how many parking spots were nearby. It was quite successful in my limited testing but I'd like to learn how to improve it and there are scenarios where I know it wouldn't work.


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| Github | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
