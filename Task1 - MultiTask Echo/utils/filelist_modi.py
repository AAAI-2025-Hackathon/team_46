import pandas as pd
from tqdm import tqdm
import cv2
import os

def get_video_metadata(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return fps, nframes, width, height

def modify_filelist(csv_path, new_csv_path):
# metadata = pd.read_csv(r'Dataset\PSAX\FileList.csv')
    metadata = pd.read_csv(csv_path)

    metadata['FileName'] = metadata['FileName'].apply(lambda x: x.split('.')[0])
    metadata['Fold'] = metadata['Split'] 
    metadata['Split'] = metadata['Fold'].apply(lambda x: 'TRAIN' if x in range(8) else 'VAL' if x == 8 else 'TEST')

    for i, row in tqdm(metadata.iterrows(), total=len(metadata)):
        video_name = row['FileName'] + '.avi'
        video_path = os.path.join('Dataset', 'PSAX', 'Videos', video_name)
        fps, nframes, width, height = get_video_metadata(video_path)
        metadata.loc[i, ['FrameHeight','FrameWidth','FPS','NumberOfFrames']] = [height, width, fps, nframes]
        
    # new_csv_path = r'Dataset\PSAX\FileList_new.csv'
    metadata.to_csv(new_csv_path, index=False)
    print('Cleaned the Existing FileList File and saved to ', new_csv_path)
