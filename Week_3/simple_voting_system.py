def collect_votes():
    votes = {}
    for _ in range(6):
        x = str(input("Type Your Vote: "))
        if x not in votes:
            votes[x] = 1
        else:
            votes[x] += 1
    return votes

def find_winner(votes):
    max_count = 0
    winner = None
    for key, value in votes.items():
        if value > max_count:
            max_count = value
            winner = key
    
    return winner, max_count

votes = collect_votes()
winner, count = find_winner()

print("Winner:", winner)
print("Votes:", count)

               