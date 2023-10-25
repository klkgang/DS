from pytube import YouTube # Import the YouTube class from the pytube module
from flask import Flask, render_template, request, redirect, url_for, flash     # Import the Flask class from the flask module

app = Flask(__name__) # Create a Flask app
app.secret_key = 'lsdgvfkuhgfkiiksdgfffozisdiygkkjhvitr87' # This is a secret key used by Flask to encrypt session cookies

@app.route('/') # This is the route to which the user will be redirected when they visit the website
def index(): # This function will be called when the user visits the index page
    return render_template('index.html') # Render the index.html template

@app.route('/download', methods=['GET', 'POST']) # This is the route to which the form in index.html will be submitted
def download(): # This function will be called when the user submits the form
    if request.method == 'POST': # If the user submitted the form
        if 'url' in  request.form: # If the URL field is empty
            try: # Try to do this
                url = request.form['url'] # Get URL from form
                yt = YouTube(url) #`yt` is an object of type `YouTube
                video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() # Get the first video with the highest resolution
                video.download('static') # Download the video
                return redirect(url_for('index')) # Redirect to the index page
            except ValueError: # If the URL is invalid
                flash('Error: Invalid URL') # Show an error message
                return redirect(url_for('index')) # Redirect to the index page
        else:
            print('URL field is empty or not found or not valid')
            flash('Error: URL field is empty')
            return redirect(url_for('index')) # Redirect to the index page
    else: # If the user tries to access the page directly
        return redirect(url_for('index')) # Redirect to the index page

if __name__ == '__main__': # If the script is run directly
    app.run(debug=True) # Run the app in debug mode