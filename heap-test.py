# importing "heapq" to implement heap queue
import heapq
import collections

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", end = "")
print(list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end = "")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end = "")
print(heapq.heappop(li))

print('*********************')
print(li[0])
print(li[1])
print(li[2])
# 5
print(len(li))


##############
# heapq.nlargest on the Counter's items()

words = [
    'apple', 'banana', 'apple', 'orange', 'banana', 'apple',
    'grape', 'banana', 'kiwi', 'apple'
]

# Use Counter to get frequencies
word_counts = collections.Counter(words)

# word_counts looks like:
# Counter({'apple': 4, 'banana': 3, 'orange': 1, 'grape': 1, 'kiwi': 1})

# Use heapq.nlargest on the Counter's items()
# The 'key=lambda item: item[1]' tells nlargest to compare the counts (the second element in the tuple)

top_3_items = heapq.nlargest(3, word_counts.items(), key=lambda e: e[1])

# same as: top_2_items = heapq.nlargest(2, word_counts, key=word_counts.get)
top_2_items = heapq.nlargest(2, word_counts.keys(), key=word_counts.get)

print(f"Top 3 most frequent items (Word, Count):")
print(top_3_items)
print(top_2_items)