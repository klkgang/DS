from pytube import YouTube
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'lsdgvfkuhgfkiiksdgfffozisdiygkkjhvitr87'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        if 'url' in  request.form:
            try:
                url = request.form['url']
                yt = YouTube(url)
                video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                video.download('static')
                return redirect(url_for('index'))
            except ValueError:
                flash('Error: Invalid URL')
                return redirect(url_for('index'))
            except Exception as e:
                flash(f'Error: {e}')
                return redirect(url_for('index'))
        else:
            flash('Error: URL field is empty')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
