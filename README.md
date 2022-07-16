# A Flask (Python) app which provides an endpoint to convert a whole PDF into one single image

The app can be run as any other Flask app, so before anything else, install the dependecies running the following command:

```sh
$ pip install -r requirements.txt
```

The recommended way to do this is creating a virtual environment previously using **virtualenv** or **pyenv**. Then run the app using

```sh
$ flask run
```

You can tweak a few things in the *.env* file

The other way to run (and deploy) the app is using **Docker**. Just run the following commands:

```sh
$ docker build . --tag pdftoimage
```

and then

```sh
docker run -d -p 5000:5000 pdftoimage
```

or

```sh
docker run --rm -p 5000:5000 pdftoimage
```

to just give it a try and remove it after stopping (*Ctrl+C*) the running container.
