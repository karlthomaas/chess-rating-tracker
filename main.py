from bs4 import BeautifulSoup
import requests

link = 'https://www.chess.com/ratings'
result = requests.get(link)

rc = result.content
soup = BeautifulSoup(rc, features='html.parser')

# header box
header_box = soup.find('header', class_='post-category-header-component master-players-rating-header')
# time class from header box
time = header_box.find(class_='post-category-header-subtitle-small')

# removes time from header box
header_box.clear(time)

# new header variable
header = header_box

chess_rating_box = soup.find('div', class_='master-players-rating-wrapper table-responsive')
chess_rating_scoreboard = chess_rating_box.find('tbody')

player_dictionary = {}
count = 0

for player in chess_rating_scoreboard.find_all('tr'):
    count += 1
    # name
    name = player.find(class_='username').get_text(strip=True)
    # rank
    rank = player.find(class_='table-text-right').get_text(strip=True)
    # status
    status = player.find(class_='v-tooltip user-chess-title master-players-rating-user-title').get_text(strip=True)

    classical = player.find(class_='master-players-rating-player-rank master-players-rating-rank-active').get_text(strip=True)



    player_dictionary[count] = {
        'name': name,
        'rank': rank,
        'status': status,
        'rating': classical
    }

for value in player_dictionary.values():
    if not value["status"]:
        value["status"] = '-'

for user in player_dictionary.values():
    print(f'{user["rank"]}, {user["status"]}, {user["name"]}, Rating: {user["rating"]} ')


    # player_dictionary[count] = {'name': }
