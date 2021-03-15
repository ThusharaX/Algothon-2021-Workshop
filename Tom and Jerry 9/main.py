candiesAmount = int(input())
players = ["Tom", "Jerry"]

if candiesAmount < 7:
    winner = 0

elif candiesAmount % 2 == 1:
    winner = 0

elif candiesAmount % 3 == 0:
    winner = 0

elif candiesAmount % 5 == 0:
    winner = 0    

else:
    winner = 1
    
print(players[winner])