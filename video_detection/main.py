from utils import read_video,save_video
from trackers import Tracker
from team_assigner import TeamAssigner
import cv2

def main():
    #read Video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    #initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/tracks.pkl')

    '''
    #Draw Cropped image of a plyer 
    for track_id,player in tracks['Player'][0].items():
        bbox = player['bbox']
        frame= video_frames[0]

        #crop bbox from frame 
        cropped_image = frame[int(bbox[1]):int(bbox[3]),int(bbox[0]):int(bbox[2])]

        #save cropped image
        cv2.imwrite(f'output_video/cropped_player.jpg', cropped_image)
        break
    # We dont need this in out code as of now it was a one time process
    ''' 

    #Assign Player Teams 
    team_assigner = TeamAssigner()
    team_assigner.assign_team_colors(video_frames[0], tracks['Player'][0])
    for frame_num,player_track in enumerate(tracks['Player']):
        for player_id, track in player_track.items():
            team = team_assigner.player_team(video_frames[frame_num], track['bbox'], player_id)

            tracks['Player'][frame_num][player_id]['team'] = team
            tracks['Player'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]
           
    #Draw Output 
    #Draw Object Tracks 
    Output_video_frames = tracker.draw_annotations(video_frames, tracks)
    #save Video
    save_video(Output_video_frames, 'output_video/output_videos.avi')

if __name__ == "__main__":
    main()