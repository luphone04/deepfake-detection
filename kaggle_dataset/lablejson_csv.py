# coding: utf-8

import pandas as pd
import os 


path_json = r"C:\Users\GPU2SHOP\Downloads\deepfake-detection\kaggle_dataset\train_sample_videos\metadata.json"
path_csv = r"C:\Users\GPU2SHOP\Downloads\deepfake-detection\kaggle_dataset\metadata.csv"

if not os.path.exists(path_json):
    print(f"File not found: {path_json}")
else:
    try:
        # Read the JSON file
        read_json = pd.read_json(path_json)
        df = pd.DataFrame(read_json)
        df_2 = pd.DataFrame(df.transpose())

        # Save to CSV
        df_2.to_csv(path_csv)
        print(f"CSV created: {path_csv}")

        # Read and adjust CSV
        read_csv = pd.read_csv(path_csv)
        read_csv.columns = ["URI", "label", "split", "original"]
        read_csv.to_csv(path_csv, index=False)
        print(f"CSV updated with correct column names")

        # Display first 5 rows
        print(read_csv.head(5))

    except Exception as e:
        print(f"An error occurred while processing {path_json}: {e}")