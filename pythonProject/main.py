import string
from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

import data

#t = open('read.txt', encoding='utf-8').read()
st.title("SENTIMENT ANALYSIS")
st.image('Sent1.jpg')
st.markdown(""" This is a web app based on “Sentiment Analysis using Machine Learning”, 
 it will categorize the text into various categories like happy, angry, cheated, attracted,
loved, anxious, etc. and will make two types of graphs i.e. bar and plotted 
 based on these sentiments.
""")
t=st.text_area("Enter the input","")
if st.button("Graph"):
    lower_case = t.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
    tokenized_words = cleaned_text.split()
    #print(tokenized_words)
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    print(final_words)

    emotion_list = []
    # with open('emotions.json', 'r') as file:
    #     for line in file:
    #         clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
    #         word, emotion = clear_line.split(':')
    #
    #
    #         if word in final_words:
    #             #print("ggghgjhgkhg")
    #             emotion_list.append(emotion)
    # with open("emotions.json", 'r') as j:

    # with open("emotions.json", 'r') as r:
    #     emotion = json.loads(r.read())
    emotion = data.dic
    for i in final_words:
        if i in emotion.keys():
            emotion_list.append(emotion[i])

    #print(emotion_list)
    w=Counter(emotion_list)
    #print(w)

    fig , axl = plt.subplots()
    sc,ax=plt.subplots()
   # f, a= plt.subplots()
    #p, pi= plt.subplots()


    axl.bar(w.keys(),w.values())
    ax.plot(w.keys(),w.values())
   # a.scatter(w.keys(),w.values())


    #pi.pie(w.keys(),w.values())

    fig.autofmt_xdate()
    sc.autofmt_xdate()
    #plt.savefig('graph.png')
    #plt.show()
    st.title("RESULT")
    st.pyplot(fig)
    st.pyplot(sc)
   # streamlit run C:/Users/adity/PycharmProjects/pythonProject/main.py st.pyplot(f)

st.subheader("Developer: Aditya Sahai")