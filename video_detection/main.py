from utils import read_video,save_video
from trackers import Tracker

def main():
    #read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    #initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)

    #save Video
    save_video(video_frames, 'output_video/output_videos.avi')

if __name__ == "__main__":
    main()