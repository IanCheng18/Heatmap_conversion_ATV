# Python program to read json file

import json
import subprocess
from methods import *

# user need to input REPOSITORY NAME
# merge pages together for all commit
REPO_NAME = "training_test"


def main():
    # Opening JSON file
    f = open('training_api.json')

    # returns JSON object as a dictionary
    json_array = json.load(f)

    count = 0
    for items in json_array:

        commit_id = get_commit_id()
        user_id = get_user_id(json_array[count]["commit"]["author"]["name"])
        repo_id = get_repo_id(REPO_NAME)
        content = ""
        unit_time = to_unix_time(json_array[count]["commit"]["author"]["date"])
        print("Unix Time: ", unit_time)
        # repo_name = get_repo_name(json_array["url"]) # Let user self key-in repo name


        # Print query content
        print(commit_id, user_id, user_id, repo_id, content, unit_time)
        # Sending Query to database
        cmd_string = "mysql -uremoteroot -h192.168.2.189 -proot -sse \"INSERT INTO gitea.action VALUES ({}, {}, 5, {}, {}, 0, 0, 'master', 0, {}, {});\"".format(commit_id, user_id, user_id, repo_id, content, unit_time)
        print(cmd_string)
        cmd = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)

    # Closing file
    f.close()


if __name__ == '__main__':
    main()
