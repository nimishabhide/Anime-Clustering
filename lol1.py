import streamlit as st

from collections import Counter 
from string import punctuation
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stop_words

#uploaded_file = st.file_uploader("Upload your input txt file", type="txt")

"""with open(uploaded_file) as f:
    mylist = [line.rstrip('\n') for line in f]

#F = open(uploaded_file,'r')
"""

user_input = st.text_area("label goes here")
text = user_input


def tokenizer(s):
    tokens = []
    for word in s.split(' '):
        tokens.append(word.strip().lower())
    return tokens

def sent_tokenizer(s):
    sents = []
    for sent in s.split('.'):
        sents.append(sent.strip())
    return sents
#tokens = tokenizer(text)
#sents = sent_tokenizer(text)
def count_words(tokens):
    word_counts = {}
    for token in tokens:
        if token not in stop_words and token not in punctuation:
            if token not in word_counts.keys():
                word_counts[token] = 1
            else:
                word_counts[token] += 1
    return word_counts

#word_counts = count_words(tokens)

def word_freq_distribution(word_counts):
    freq_dist = {}
    max_freq = max(word_counts.values())
    for word in word_counts.keys():  
        freq_dist[word] = (word_counts[word]/max_freq)
    return freq_dist

#freq_dist = word_freq_distribution(word_counts)

def score_sentences(sents, freq_dist, max_len=40):
    sent_scores = {}  
    for sent in sents:
        words = sent.split(' ')
        for word in words:
            if word.lower() in freq_dist.keys():
                if len(words) < max_len:
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = freq_dist[word.lower()]
                    else:
                        sent_scores[sent] += freq_dist[word.lower()]
    return sent_scores

#sent_scores = score_sentences(sents, freq_dist)

def summarize(sent_scores, k):
    top_sents = Counter(sent_scores) 
    summary = ''
    scores = []
    
    top = top_sents.most_common(k)
    for t in top: 
        summary += t[0].strip()+'. '
        scores.append((t[1], t[0]))
    return summary[:-1], scores
#summary, summary_sent_scores = summarize(sent_scores, 3)
#st.write(summary)




def main():

    tokens = tokenizer(text)
    sents = sent_tokenizer(text)
    word_counts = count_words(tokens)
    freq_dist = word_freq_distribution(word_counts)
    sent_scores = score_sentences(sents, freq_dist)
    summary, summary_sent_scores = summarize(sent_scores, 3)
    st.write(summary)
    
if st.button('summarize'):
    main()