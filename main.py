#import the necessary modules
from pytube import YouTube
from flask import Flask, render_template, request, redirect, url_for, send_file, flash, after_this_request
import os
from werkzeug.utils import secure_filename


# create the flask app
app = Flask(__name__)
app.secret_key = 'lsdgvfkuhgfkiiksdgfffozisdiygkkjhvitr87'

#defiine the main route
@app.route('/')
def index():
    return render_template('index.html')

#the download route to the console
@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        flash('Error: URL field is empty')
        return redirect(url_for('index'))
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = secure_filename(video.default_filename)
        filepath = os.path.join(app.static_folder, filename)
        video.download(app.static_folder)
        flash('Download successful')
        return send_file(filepath, as_attachment=True)
    except ValueError:
        flash('Error: Invalid URL')
    except Exception as e:
        flash(f'Error: {e}')
    return redirect(url_for('index'))

#the download route to the browser
@app.route('/download2', methods=['POST'])
def downloadq():
    url = request.form.get('url')
    if not url:
        flash('Error: URL field is empty')
        return redirect(url_for('index'))
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = secure_filename(video.default_filename)
        filepath = os.path.join(app.static_folder, filename)
        video.download(app.static_folder)
        flash('Download successful')
        @after_this_request
        def remove_file(response):
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except Exception as error:
                    app.logger.error("Error removing downloaded file handle: %s", error)
            return response
        return send_file(filepath, as_attachment=True)
    except ValueError:
        flash('Error: Invalid URL')
    except Exception as e:
        flash(f'Error: {e}')
    return redirect(url_for('index'))

#start the app
if __name__ == '__main__':
    app.run(debug=True)