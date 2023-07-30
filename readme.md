# Facebook Post Data Collection and Analysis

This repository contains two Python scripts for collecting Facebook post data using the Facebook Graph API and analyzing the frequency of posts per hour.

## Requirements

To use these scripts, you'll need the following:

- Python 3.x
- Facebook API token (access token)

## Script 1: Facebook Data Collection (get_posts_data.py)

### Description

The `get_posts_data.py` script is responsible for collecting Facebook post data using the Facebook Graph API. It requests data for the user's posts, including fields like message, created time, description, caption, link, place, and status type. The script iterates over the posts, writes them to a JSON Lines file (`my_posts.jsonl`), and handles pagination to fetch all available posts.

### Instructions

1. Obtain a Facebook API token:  
   Before running the script, you need to obtain a valid Facebook API token. Save the token to a text file (e.g., `Your-Token`) in UTF-8 encoding.

2. Run the script:  
   To run the script, execute the following command in your terminal or command prompt:

   ```
   python get_posts_data.py
   ```

   The script will read the token from the file, fetch your posts data, and save it to the `my_posts.jsonl` file.

## Script 2: Facebook Post Statistics (facebook_statistics_posts.py)

### Description

The `facebook_statistics_posts.py` script performs data analysis on the Facebook post data collected in the previous step. It reads the data from the JSON Lines file (`my_posts.jsonl`) and processes the timestamps to calculate the frequency of posts per hour. The analysis results are visualized in a bar chart, showing post frequencies over 24 hours.

### Requirements

To run this script, ensure you have the following Python packages installed:

- json
- argparse
- dateutil
- numpy
- pandas
- matplotlib

You can install them using the following command:

```
pip install json argparse dateutil numpy pandas matplotlib
```

### Instructions

1. Prepare the JSON Lines file:  
   Make sure you have already collected Facebook post data using `get_posts_data.py`, and you have the `my_posts.jsonl` file in the same directory.

2. A demo my_posts1.jsonl is present in the repository.

3. Run the script:  
   To analyze the post data and generate the visualization, execute the following command in your terminal or command prompt:

   ```
   python facebook_statistics_posts.py --file my_posts.jsonl
   ```

   The script will read the data from the file, process it, create a bar chart, and save it as `posts_per_hour.png`.

## Note

Both scripts are standalone and can be run independently. Remember to replace `Your-Token` in `get_posts_data.py` with the path to your Facebook API token file.

For any issues or questions, please contact [Azim](mailto:syed.azim.q@gmail.com).

---
_This repository is hosted on GitHub. For more details, visit the GitHub page: [facebook-post-analysis](https://github.com/azim-qadri/facebook-post-analysis/Facebook-Analytics)
