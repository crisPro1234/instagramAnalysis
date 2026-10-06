from pathlib import Path
import time
import webbrowser
import json

FOLLOWERS_PATH = Path("instagramAnalysis/user_data/connections/followers_and_following/followers_1.json")
FOLLOWING_PATH = Path("instagramAnalysis/user_data/connections/followers_and_following/following.json")


followers_name = []

people_to_unfollow = {}

def return_following_dict():
    with open(FOLLOWING_PATH, "r") as following_json:
        return json.load(following_json)


def compare_followers_and_following(followes_dict):
    following_dict = return_following_dict()["relationships_following"]
    
    for profile in followers_dict:
        for value, data in profile.items():
            if not data: continue
            follower_user_name = data[0]["value"]
            followers_name.append(follower_user_name)

    for profile in following_dict:
        following_user_name = profile["title"]
        account_link = profile["string_list_data"][0]["href"]

        if not following_user_name in followers_name:
            people_to_unfollow[following_user_name] = {"account_link": account_link}
            #brian___schneiteger en ese quedamos
            print(f"User: {following_user_name} is not following you back. Account link: {account_link}")
            print("____________")

with open(FOLLOWERS_PATH, "r") as my_followers_json:
    followers_dict = json.load(my_followers_json)
    compare_followers_and_following(followers_dict)

    
