import requests
import pandas as pd
import datetime

# region - Get top
data_top_stories = requests.get(
    'https://hacker-news.firebaseio.com/v0/topstories.json'
)

# Extract top stories ID
data_top_stories_2 = data_top_stories.json()

# endregion

# # region - Loop Through Stores
# ## Create a blank dataframe
# z_temp_data = pd.DataFrame()

# ## Create a perfect list
# z_perfect_list = ['by', 'descendants', 'id', 'score', 'time', 'title', 'type', 'url', 'kids']

# for i in range(0, len(data_top_stories_2)):
#     print(
#         data_top_stories_2[i]
#     )

#     # Get data
#     z_data = requests.get(
#         f'https://hacker-news.firebaseio.com/v0/item/{data_top_stories_2[i]}.json?print=pretty'
#     )

#     # Extract content and convert to json
#     z_data_2 = z_data.json()

#     # Extract keys of z_data_2
#     z_data_2_keys = list(z_data_2.keys())

#     # Check if any missing
#     z_data_2_keys_2_missing = list(set(z_perfect_list) - set(z_data_2_keys))

#     # If missing, create a new key and blank value
#     for j in range(0, len(z_data_2_keys_2_missing)):
#         z_data_2[z_data_2_keys_2_missing[j]] = ''

#     # Remove kids as we want 1 row result
#     z_data_2_kids = z_data_2.pop('kids')

#     # Convert json to dataframe
#     z_data_3 = pd.DataFrame(z_data_2, index = [0])

#     # attach kids as a column
#     z_data_3['kids'] = ','.join(str(x) for x in z_data_2_kids)

#     z_temp_data = pd.concat(
#         [
#             z_temp_data,
#             z_data_3
#         ],
#         axis = 0
#     )

# # endregion

# # region - add a datetime column
# z_temp_data['extracted_datetime'] = datetime.datetime.now()


# # endregion - add a datetime column