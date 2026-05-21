from utils import read_video,save_video
from trackers import Tracker

def main():
    #read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    #initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/tracks.pkl')

    #Draw Output 
    #Draw Object Tracks 
    Output_video_frames = tracker.draw_annotations(video_frames, tracks)
    #save Video
    save_video(Output_video_frames, 'output_video/output_videos.avi')

if __name__ == "__main__":
    main()