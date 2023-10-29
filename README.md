# YouTube Downloader

This is a simple web application that allows you to download YouTube videos by entering their URLs.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Start the application by running `python main.py`.

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Enter the URL of the YouTube video you want to download.
3. Click the "Download" button to download the video to your computer.

## Features

- Supports downloading YouTube videos in MP4 format.
- Automatically sanitizes the video filename to prevent errors.
- Shortens the video filename to a maximum of 50 characters to prevent long filenames.
- Displays error messages if the URL is invalid or the download fails.
- Allows you to download the video and immediately stream it to the client.

## Contributing

If you find a bug or have a feature request, please open an issue on GitHub. Pull requests are also welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.