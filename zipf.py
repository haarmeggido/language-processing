import matplotlib.pyplot as plt

# Read the data from the "words.txt" file
data = {}
with open("words.txt", "r") as file:
    for line in file:
        word, count = line.strip().split(":")
        data[word] = int(count)

# Sort the data by word count in descending order
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

# Extract the word counts and create a list of ranks
word_counts = [count for word, count in sorted_data]
ranks = list(range(1, len(word_counts) + 1))

# Create the Zipf's law graph
plt.figure(figsize=(12, 6))
plt.plot(ranks, word_counts, marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('log')
plt.title("Zipf's Law")
plt.xlabel("Rank (log scale)")
plt.ylabel("Word Count (log scale)")
plt.grid(True)


plt.savefig("zipfs_law_plot.png")
# Display the graph
plt.show()