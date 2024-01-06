#import the necessary modules
from pytube import YouTube 
from flask import Flask, render_template, request
from flask import redirect, url_for, Response
from urllib.request import urlopen
from flask import stream_with_context
import re 
# end of imports

#function to sanitize the filename 
def sanitize_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = filename[:45] # limit filename length because long names cause bugs 
    return filename.replace(' ', '_')


#create flask object
app = Flask(__name__)


#home page 
@app.route('/')
def home():
    return render_template('index.html')

#route to  get the url
@app.route('/download2', methods=['POST'])
def get_url():
    url = request.form['url']
    return redirect(url_for('stream', pathurl=url))

#route to download the video
@app.route('/stream/<path:pathurl>')
def stream(pathurl):
    yt = YouTube(pathurl)
    video = yt.streams.first()
    stream_url = video.url
    video_title = sanitize_filename(yt.title)
    print(video_title)


    def generate():
        with urlopen(stream_url) as f:
            for chunk in iter(lambda: f.read(4096), b''):
                yield chunk

    response = Response(stream_with_context(generate()), mimetype='video/mp4')
    response.headers['Content-Disposition'] = f'attachment; filename={video_title}.mp4'
    return response


if __name__ == '__main__':
    app.run(debug=True)