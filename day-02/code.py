from pathlib import Path

inputFile = Path(__file__).with_name('input.txt').open('r')
data= inputFile.read().splitlines()

sum= 0
results= [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]
for line in data:
    player1, player2 = line.split(' ')
    row = ['X','Y','Z'].index(player2)
    col = ['A', 'B', 'C'].index(player1)
    sum += row + 1 + results[row][col]

print(sum)