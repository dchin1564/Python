from collections import Counter 

def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):
    # Write your code here
    text = text1.split()
    count_words = dict()

    for word in text:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    print(dict(sorted(count_words.items())))

    count = Counter(dictionary1)
    count1 = Counter(deduct)
    count.subtract(count1)
    print(dict(count))
    

    

