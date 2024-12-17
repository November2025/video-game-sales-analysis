import pandas as pd

# Load the dataset
file_path = './data/archive/vgsales.csv'

video_game_data = pd.read_csv(file_path)

# Display the first few rows
print(video_game_data.head())

