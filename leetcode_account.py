import requests


class Account:
    api_url = "https://leetcode-stats.tashif.codes/{username}"
    username = None
    stats = None
    easy, medium, hard = None, None, None

    def __init__(self):
        self.get_username()
        self.fetch_leetcode_stats()
        self.check_stats_status()
        self.analyse_data()

    def get_username(self):
        self.username = input("Enter your LeetCode username: ").strip()

    def fetch_respone(self):
        url = self.api_url.format(username=self.username)
        response = requests.get(url)
        return response

    def fetch_leetcode_stats(self):
        response = self.fetch_respone()
        while response.status_code == 404:
            print(f"User not found")
            response = self.fetch_respone()
        response.raise_for_status()
        self.stats = response.json()

    def check_stats_status(self):
        if not self.stats or self.stats.get('status') != 'success':
            raise Exception("Failed to retrieve data.")

    def analyse_data(self):
        self.easy = self.stats.get('easySolved', 0)
        self.medium = self.stats.get('mediumSolved', 0)
        self.hard = self.stats.get('hardSolved', 0)

