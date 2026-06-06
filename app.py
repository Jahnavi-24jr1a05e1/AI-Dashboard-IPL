import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("IPL_Matches_2008_2022.csv")
st.sidebar.header("Filter")

season = st.sidebar.selectbox(
    "Select Season",
    sorted(df['Season'].unique())
)
filtered_df = df[df['Season'] == season]
st.title("🏏 IPL Dashboard")
st.subheader("Selected Season Data")
st.dataframe(filtered_df.head())
st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Dataset Information")
st.write("Rows and Columns:")
st.write(df.shape)
st.write("Column Names:")
st.write(df.columns)
st.subheader("Key Performance Indicators")
total_matches = len(df)

total_teams = pd.concat(
    [df['Team1'], df['Team2']]
).nunique()

total_venues = df['Venue'].nunique()

total_seasons = df['Season'].nunique()
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Matches",
    total_matches
)

col2.metric(
    "Teams",
    total_teams
)

col3.metric(
    "Venues",
    total_venues
)

col4.metric(
    "Seasons",
    total_seasons
)
st.subheader("Matches Per Season")

season_count = df['Season'].value_counts().sort_index()

fig = px.bar(
    x=season_count.index,
    y=season_count.values,
    labels={
        'x': 'Season',
        'y': 'Number of Matches'
    },
    title="Matches Played Each Season"
)

st.plotly_chart(fig)
st.subheader("Top Winning Teams")

winning_teams = df['WinningTeam'].value_counts().head(10)

fig2 = px.bar(
    x=winning_teams.index,
    y=winning_teams.values,
    labels={
        'x': 'Team',
        'y': 'Wins'
    },
    title="Top 10 Winning Teams"
)

st.plotly_chart(fig2)
st.subheader("Toss Winner Distribution")

fig3 = px.pie(
    df,
    names='TossWinner',
    title='Toss Winner Distribution'
)

st.plotly_chart(fig3)
st.subheader("Top Match Venues")

venues = df['Venue'].value_counts().head(10)

fig4 = px.bar(
    x=venues.index,
    y=venues.values,
    labels={
        'x': 'Venue',
        'y': 'Matches'
    },
    title='Top 10 Venues'
)

st.plotly_chart(fig4)
st.subheader("Top Player of the Match Winners")

players = df['Player_of_Match'].value_counts().head(10)

fig5 = px.bar(
    x=players.index,
    y=players.values,
    labels={
        'x': 'Player',
        'y': 'Awards'
    },
    title='Top Player of the Match Winners'
)

st.plotly_chart(fig5)
st.subheader("Data Cleaning")

st.write("Missing Values in Each Column")
st.write(df.isnull().sum())

st.write("Duplicate Rows")
st.write(df.duplicated().sum())
st.subheader("Top Player of the Match Winners")

players = df['Player_of_Match'].value_counts().head(10)

fig5 = px.bar(
    x=players.index,
    y=players.values,
    title="Top Player of the Match Winners"
)

st.plotly_chart(fig5)

st.subheader("Insights")

st.write("""
🏏 Mumbai Indians and Chennai Super Kings are among the most successful IPL teams.

🏟️ Some venues host significantly more matches than others.

🎯 A few players dominate the Player of the Match awards.

📈 The number of matches generally increased as IPL expanded.

🪙 Toss wins are fairly distributed across teams.
""")