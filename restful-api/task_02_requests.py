#!/usr/bin/python3
"""Module for fetch_and_print_posts and fetch_and_save_posts methods"""
import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/posts')
status_code = response.status_code
posts = response.json()


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder,
    Print the status code of the response and
    print the titles of all the posts"""
    print("Status Code: {}".format(status_code))
    if status_code == 200:
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder and
    write this data into a CSV file called posts.csv
    with columns corresponding to the dictionary keys"""
    if status_code == 200:
        with open("posts.csv", "w", encoding='utf-8', newline='') as csvFile:
            fieldnames = ["id", "title", "body"]
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writeheader()
            for post in posts:
                csvWriter.writerows([{key: post[key] for key in fieldnames}])
