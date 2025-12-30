#!/usr/bin/env python3
"""
Day 15: NLP (Natural Language Processing)
Basic text processing and sentiment analysis
"""

import re
from collections import Counter

print("=== Day 15: NLP Text Processing ===")

# Sample text
text = """Natural Language Processing is amazing!
It helps computers understand human language.
NLP is used in chatbots, translation, and sentiment analysis.
"""

print("\n1. Original Text:")
print(text)

# 2. Tokenization (split into words)
print("\n2. Tokenization:")
words = re.findall(r'\w+', text.lower())
print(f"   Words found: {len(words)}")
print(f"   First 10 words: {words[:10]}")

# 3. Remove stopwords
print("\n3. Removing Stopwords:")
stopwords = {'the', 'is', 'and', 'in', 'a', 'of', 'to', 'it', 'language'}
filtered_words = [w for w in words if w not in stopwords]
print(f"   Words after filtering: {len(filtered_words)}")
print(f"   Filtered words: {filtered_words[:10]}")

# 4. Frequency analysis
print("\n4. Word Frequency Analysis:")
word_freq = Counter(filtered_words)
print(f"   Top 5 most common words:")
for word, count in word_freq.most_common(5):
    print(f"      '{word}': {count} times")

# 5. Simple sentiment analysis
print("\n5. Sentiment Analysis:")
positive_words = {'amazing', 'great', 'good', 'excellent', 'helpful'}
negative_words = {'bad', 'terrible', 'awful', 'poor'}

pos_count = sum(1 for w in words if w in positive_words)
neg_count = sum(1 for w in words if w in negative_words)

print(f"   Positive words found: {pos_count}")
print(f"   Negative words found: {neg_count}")

if pos_count > neg_count:
    print(f"   Sentiment: POSITIVE 😊")
elif neg_count > pos_count:
    print(f"   Sentiment: NEGATIVE 😞")
else:
    print(f"   Sentiment: NEUTRAL 😐")

# 6. Text normalization
print("\n6. Text Normalization:")
normalized = text.lower().strip()
print(f"   Normalized text (first 50 chars): {normalized[:50]}...")

# 7. N-grams
print("\n7. Bigrams (2-word combinations):")
bigrams = [' '.join(words[i:i+2]) for i in range(len(words)-1)]
print(f"   First 5 bigrams: {bigrams[:5]}")

print("\n=== Concepts Learned ===")
print("1. Tokenization - splitting text into words")
print("2. Stopword removal - removing common words")
print("3. Frequency analysis - counting word occurrences")
print("4. Sentiment analysis - determining text emotion")
print("5. Text normalization - standardizing text")
print("6. N-grams - word sequences")
