#region - Load packages
import requests
import pandas as pd
import datetime
#endregion - Load packages

# region - Get top News
data_top_stories = requests.get(
    'https://hacker-news.firebaseio.com/v0/topstories.json'
)

# Extract top stories ID
data_top_stories_2 = data_top_stories.json()

# endregion - Get top News

# region - Create a Loop

z_temp_dict = {}
for i in range(0, len(data_top_stories_2)):
#for i in range(0, 5):

    print(i)

    z_data = requests.get(
    f'https://hacker-news.firebaseio.com/v0/item/{data_top_stories_2[i]}.json?print=pretty'
    )

    z_data_2 = z_data.json()

    z_temp_dict[i] = z_data_2

# endregion - Create a loop

# region - Convert to DF 
data = pd.DataFrame.from_dict(z_temp_dict, orient='index')
data['extracted_time'] = datetime.datetime.now()

# endregion - Convert to DF