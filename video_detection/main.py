from utils import read_video,save_video

def main():
    #read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    #save Video
    save_video(video_frames, 'output_video/output_videos.mp4')

if __name__ == "__main__":
    main()