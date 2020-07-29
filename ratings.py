"""Restaurant rating lister."""

get_file = open("scores.txt")

ratings = {}

for line in get_file:
    line = line.rstrip().split(":")
    rest_name = line[0]
    rest_score = line[1]
    ratings[rest_name] = int(rest_score)
    
for rest_name, rest_score in sorted(ratings.items()):
    print(f"{rest_name} is rated at {rest_score}.")






# put your code here
