import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

vote_count = []
count = 0
unique_candidate = []
candidate_list = []
vote_percent = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        count += 1
        candidate_list.append(row[2])
    for row in set(candidate_list):
        unique_candidate.append(row)
        num_vote = candidate_list.count(row)
        vote_count.append(num_vote)
        voter_percent = (num_vote/count) * 100
        vote_percent.append(voter_percent)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

print("-" * 32)
print("Election Results")
print('-'*32)
print(f"Total Votes: {count}")
print('-' * 32)
for i in range(len(unique_candidate)):
    print(f'{unique_candidate[i]} : {vote_percent[i]: .3f}%({vote_count[i]})')
print('-' * 32)
print(f'Winner: {winner}')
print('-' * 32)

with open('election_results.txt', 'w') as text:
    text.write("-" * 32 + '\n')
    text.write("Election Results\n")
    text.write('-' * 32 + '\n')
    text.write(f"Total Votes: {count}\n")
    text.write('-' * 32)
    for i in range(len(unique_candidate)):
        text.write(f'{unique_candidate[i]} : {vote_percent[i]}%({vote_count[i]})\n')
        text.write('-' * 32 + '\n')
        text.write(f'Winner: {winner}\n')
        text.write('-' * 32 + '\n')

