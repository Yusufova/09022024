f = {
  "tile": "N", "score": 1,
  "tile2": "K", "score2": 5,
  "tile3": "Z", "score3": 10,
  "tile4": "X", "score4": 8,
  "tile5": "D", "score5": 2,
  "tile6": "A", "score6": 1,
  "tile7": "E", "score7": 1
}
y = f.get("score")
u = f.get("score2")
s = f.get("score3")
v = f.get("score4")
a = f.get("score5")
o = f.get("score6")
d = f.get("score7")
i = y + u + s + v + a + o + d
print(i)