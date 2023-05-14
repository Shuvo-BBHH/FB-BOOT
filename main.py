from pytube import YouTube
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		# Get the YouTube video URL from the form
		video_url = request.form['video_url']

		# Download the video using pytube
		yt = YouTube(video_url)
		stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
		stream.download()

		# Get the download link
		download_url = stream.url

		# Render the download link on the page
		return render_template_string('<a href="{{ url }}" download>Download</a>', url=download_url)

	# Render the HTML form
	return render_template_string('''<!DOCTYPE html>
<html>
<head>
	<title>Download YouTube Video</title>
</head>
<body>
	<h1>Download YouTube Video</h1>
	<form method="post">
		<label for="video_url">YouTube Video URL:</label>
		<input type="text" name="video_url" id="video_url">
		<button type="submit">Download</button>
	</form>
</body>
</html>''')

if __name__ == '__main__':
	app.run(debug=True)
