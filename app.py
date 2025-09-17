import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df = df[['title', 'abstract', 'publish_time', 'authors', 'journal', 'source_x']]
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    df = df.dropna(subset=['title', 'publish_time'])
    return df

df = load_data()

# Filters
year_range = st.slider("Select year range", 2015, 2023, (2019, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications per year
st.subheader("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud
st.subheader("Word Cloud of Paper Titles")
titles = " ".join(filtered_df['title'].dropna())
if titles:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
    st.image(wordcloud.to_array())

# Sample Data
st.subheader("Sample Data")
st.write(filtered_df[['title', 'publish_time', 'journal']].head(20))
