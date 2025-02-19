import pandas as pd


def modify_volumetracings(csv_path, new_csv_path):
    # csv_path = r'Dataset/PSAX/VolumeTracings.csv'
    df = pd.read_csv(csv_path)
    df[["X", "Y", "Frame"]] = df[["X", "Y", "Frame"]].apply(pd.to_numeric, errors='coerce')
    df = df.groupby("FileName", group_keys=False).apply(lambda g: g.ffill().bfill()).reset_index(drop=True)
    df['Frame'] = df['Frame'].astype(int)
    df['X'] = df['X'].astype(int)
    df['Y'] = df['Y'].astype(int)
    # new_csv_path = r'Dataset/PSAX/VolumeTracings_new.csv'
    df.to_csv(new_csv_path, index=False)
    print('Cleaned the Existing Volume Tracing Files and saved to ', new_csv_path)
