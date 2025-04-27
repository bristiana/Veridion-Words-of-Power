import requests
from time import sleep
import random

host = ""
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

NUM_ROUNDS = 10


def what_beats(word):
    sleep(random.randint(1, 3)) # TODO
    return random.randint(1, 77)

def play_game(player_id):

    def get_round():
        response = requests.get(get_url)
        print(response.json())
        sys_word = response.json()['word']
        round_num = response.json()['round']
        return (sys_word, round_num)

    submitted_rounds = []
    round_num = 0

    while round_num != NUM_ROUNDS :
        print(submitted_rounds)
        sys_word, round_num = get_round()
        while round_num == 0 or round_num in submitted_rounds:
            sys_word, round_num = get_round()
            sleep(0.5)

        if round_num > 1:
            status = requests.post(status_url, json={"player_id": player_id}, timeout=2)
            print(status.json())

        choosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": choosen_word, "round_id": round_num}
        response = requests.post(post_url, json=data, timeout=5)
        submitted_rounds.append(round_num)
        print("POST: !!!!!!!!!!!!!!!!")
        print(response.json())