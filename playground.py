import requests
import pandas as pd

# region - Get top
data_top_stories = requests.get(
    'https://hacker-news.firebaseio.com/v0/topstories.json'
)

# Extract top stories ID
data_top_stories_2 = data_top_stories.json()

# endregion

# region - Loop Through Stores
z_temp_data = pd.DataFrame()
for i in range(0, len(data_top_stories_2)):
    print(
        data_top_stories_2[i]
    )

    # Get data
    z_data = requests.get(
        f'https://hacker-news.firebaseio.com/v0/item/{data_top_stories_2[i]}.json?print=pretty'
    )

    # Extract content and convert to json
    z_data_2 = z_data.json()

    # TODO 1
        #Convert z_data_2 to dataframe 

    # TODO 2
        # extract columns and check if kids presents or whatever column is missing.

    # Remove kids as we want 1 row result
    z_data_2_kids = z_data_2.pop('kids')

    # Convert json to dataframe
    z_data_3 = pd.DataFrame(z_data_2, index = [0])

    # attach kids as a column
    z_data_3['kids'] = ','.join(str(x) for x in z_data_2_kids)

    z_temp_data = pd.concat(
        [
            z_temp_data,
            z_data_3
        ],
        axis = 0
    )

# endregion