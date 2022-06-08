letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
# 1
letter_to_points = {key:value for key, value in zip(letters, points)}
# print(letter_to_points)

# 2
letter_to_points[" "] = 0

# 3, 4, 5, 6
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# 7
brownie_points = score_word("BROWNIE")

# 8
print(brownie_points)

#9
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"]
}

# 10
player_to_points = {}

# 11, 12, 13, 14
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)