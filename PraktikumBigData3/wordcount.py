def map_function(text):
    for word in text.split():
        yield (word, 1)

def reduce_function(word, counts):
    return (word, sum(counts))

from collections import defaultdict
data = open("C:/Users/afifa/OneDrive/Documents/bigdata3.txt", "r")


mapped = []
for text in data:
    mapped.extend(map_function(text))

reduced = defaultdict(list)
for word, count in mapped:
    reduced[word].append(count)

result = []
for word, counts in reduced.items():
    result.append(reduce_function(word, counts))

for word, count in result:
    print(f"{word} : {count}")