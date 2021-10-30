from flask import Flask, render_template, Response
from camera import Video
video_camera = None
global_frame = None

# Define app
app = Flask(__name__)

# Route to index.html file


@app.route('/')
def index():
    return render_template('index.html')

# Route to library camera
# Panggil function camera
def gen():
    global video_camera
    global global_frame
    
    if video_camera is None:
        video_camera = Video()
    while True:
        # Get camera frame 
        frame = video_camera.gen_frames()
        if frame is not None:
            global_frame = frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')
        

@app.route('/video')
def video():
    return Response(gen(),
        mimetype='multipart/x-mixed-replace; boundary = frame')

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
