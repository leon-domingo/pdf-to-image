# A Flask (Python) app which provides a couple of endpoints to convert a whole PDF into one single image

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
$ docker build . --tag pdftoimage:1.0.0
```

and then

```sh
docker run -d -p 5000:5000 pdftoimage:1.0.0
```

or

```sh
docker run --rm -p 5000:5000 pdftoimage:1.0.0
```

to just give it a try and remove the container after you stop it (*Ctrl+C*).

## API

### /pdfToJson

Options:
  - /pdfToJson
  - /pdfToJson/FORMAT
  - /pdfToJson/FORMAT/MODE

*FORMAT* can be **png** (default) or **jpg**. It's the format of the generated image.
*MODE* can be **vertical** (default) or **horizontal**. It's the way the resulting image will be generated. More on this later.

Method: **POST**
Content-Type: **application/json**
Body:

```json
{
  "pdfContent": "..."
}
```

*pdfContent* is the content of the **PDF** file encoded in **Base64**

Status: **200 OK**
Content-Type: **application/json**
Response:

```json
{
  "contentType": "image/...",
  "imageContent": "...",
  "timestamp": "2022-07-31T12:34:56.999999+00:00"
}
```

*contentType* is **image/png** or **image/jpg** depending on the given *format*.
*imageContent* is the binary content of the image encoded in **Base64**. Depending on the *mode* it will be a single image with every page on top of each other from the given **PDF** (*vertical*), or all the pages side-by-side (*horizontal*).
*timestamp* is the date and time (UTC-based) when the request was made.

### /pdfToImage

Options:
  - /pdfToImage
  - /pdfToImage/FORMAT
  - /pdfToImage/FORMAT/MODE

*FORMAT* can be **png** (default) or **jpg**. It's the format of the generated image.
*MODE* can be **vertical** (default) or **horizontal**. It's the way the resulting image will be generated. More on this later.

Method: **POST**
Content-Type: **application/json**
Body:

```json
{
  "pdfContent": "..."
}
```

*pdfContent* is the content of the **PDF** file encoded in **Base64**

Status: **200 OK**
Content-Type: **image/png** or **image/jpg**, depending on the *format*
Response: The binary content of the generated image based on the given parameters. Depending on the *mode* it will be a single image with every page on top of each other from the given **PDF** (*vertical*), or all the pages side-by-side (*horizontal*).
