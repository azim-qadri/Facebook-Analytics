import json
import facebook
import requests


def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()


if __name__ == '__main__':
    token = getTokenFromFile(r"Your-Token")  # Path to your facebook api token
    graph = facebook.GraphAPI(token)
    all_fields = {
        'message',
        'created_time',
        'description',
        'capiton',
        'link',
        'place',
        'status_type'
    }

    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me', 'posts', fields=all_fields)
    while True:
        try:
            with open('my_posts1.jsonl', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post) + "\n")
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
