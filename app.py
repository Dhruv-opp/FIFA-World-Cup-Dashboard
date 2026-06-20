import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="FIFA World Cup Analytics Dashboard",
    page_icon="⚽",
    layout="wide"
)
st.title("⚽ FIFA World Cup Analytics Dashboard")
st.write("Explore historical FIFA World Cup statistics from 1930 to 2014.")


st.markdown("""Explore historical FIFA World Cup data from **1930–2014** and uncover insights into:.

This dashboard provides insights into:

- 📈 Tournament trends
- ⚽ Team performances
- 🏆 Match statistics
- 📊 Advanced analytics""")

df=pd.read_csv("data/WorldCupMatches.csv")
df.columns=df.columns.str.strip()
df.columns=df.columns.str.replace(" ","_")
df=df.drop_duplicates(subset="MatchID")
df["Total_Goals"]=df["Home_Team_Goals"]+df["Away_Team_Goals"]
st.sidebar.title("Dashboard Filters")
selected_year=st.sidebar.selectbox("Select Year",sorted(df["Year"].unique()))

filtered_df=df[df["Year"]==selected_year]

total_matches = len(filtered_df)

total_goals = filtered_df["Total_Goals"].sum()

avg_goals = round(
    total_goals / total_matches,
    2
)

highest_attendance = int(
    filtered_df["Attendance"].max()
)


goals_per_year = df.groupby("Year")["Total_Goals"].sum()
attendance_per_year = df.groupby("Year")["Attendance"].sum()
df["Decade"] = (df["Year"] // 10) * 10

goals_by_decade = (df.groupby("Decade")["Total_Goals"].sum()
)
df["Goal_Difference"] = (df["Home_Team_Goals"]- df["Away_Team_Goals"]).abs()

goal_diff_year = (df.groupby("Decade")["Goal_Difference"].mean())
home_goals = df.groupby("Home_Team_Name")["Home_Team_Goals"].sum()

away_goals = df.groupby("Away_Team_Name")["Away_Team_Goals"].sum()

Most_scoring_teams = (
    home_goals.add(
        away_goals,
        fill_value=0
    )
    .sort_values(ascending=False)
    .head(10)
)
home_teams = df["Home_Team_Name"]

away_teams = df["Away_Team_Name"]

Top_Team_app = (pd.concat([home_teams, away_teams]).value_counts().head(10))
top_matches = (df.sort_values(by="Total_Goals",ascending=False).head(10))

goals_scored = (home_goals.add(away_goals,fill_value=0))

home_conceded = (df.groupby("Home_Team_Name")["Away_Team_Goals"].sum())

away_conceded = (df.groupby("Away_Team_Name")["Home_Team_Goals"].sum())

goals_conceded = (home_conceded.add(away_conceded,fill_value=0))

top_teams = (goals_scored.sort_values(ascending=False).head(10))

top_conceded = goals_conceded.loc[top_teams.index]

top_matches = (df.sort_values(by="Total_Goals",ascending=False).head(10))
match_labels = (top_matches["Home_Team_Name"]+ " vs "+ top_matches["Away_Team_Name"])

stage_mapping={ # Group stages
    "First round":"Group Stage",
    "Group 1": "Group Stage",
    "Group 2": "Group Stage",
    "Group 3": "Group Stage",
    "Group 4": "Group Stage",
    "Group 5": "Group Stage",
    "Group 6": "Group Stage",
    "Group A": "Group Stage",
    "Group B": "Group Stage",
    "Group C": "Group Stage",
    "Group D": "Group Stage",
    "Group E": "Group Stage",
    "Group F": "Group Stage",
    "Group G": "Group Stage",
    "Group H": "Group Stage",

    # Quarter-finals
    "Quarter-finals": "Quarter-finals",

    # Semi-finals
    "Semi-finals": "Semi-finals",

    # Finals
    "Final": "Final",

    "Match for third place": "Third Place",
    "Third place": "Third Place",
    "Play-off for third place" : "Third Place",

    "Preliminary round":"Group Stage",
    "Round of 16  ":"Round of 16  "

    
    }
df["Stage_Clean"] = df["Stage"].replace(stage_mapping)
matches_per_stage=df.groupby("Stage_Clean")["MatchID"].count()
avg_goals_stage=df.groupby("Stage_Clean")["Total_Goals"].mean()

st.divider()

tab0,tab1,tab2,tab3,tab4=st.tabs([ "🏠 Home","📈 Tournament Trends",
        "⚽ Team Analysis",
        "🏆 Match Analysis",
        "📊 Advanced Insights"
])

with tab1:
    st.header("Tournament Trends")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(
        x=goals_per_year.index,
        y=goals_per_year.values,
        markers=True,
        title="Goals Scored per Tournament")

        fig.update_layout(xaxis_title="Year",yaxis_title="Goals")

        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.line(x=attendance_per_year.index,y=attendance_per_year.values,markers=True,title="Attendance per Tournament")

        fig.update_layout(xaxis_title="Year",yaxis_title="Attendance")

        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()    
    fig = px.line(
    x=goals_by_decade.index,
    y=goals_by_decade.values,
    markers=True,title="Goals by Decade")

    fig.update_layout(xaxis_title="Decade",yaxis_title="Goals")

    st.plotly_chart(fig, use_container_width=True)    

with tab2:
    st.header("Team Analysis")
    col1,col2=st.columns(2)
    with col1:
        fig = px.bar(
        x=Most_scoring_teams.values,
        y=Most_scoring_teams.index,
        orientation="h",
        title="Highest Scoring Teams"
        )

        fig.update_layout(
            xaxis_title="Goals",
            yaxis_title="Team"
        )

        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(
        x=Top_Team_app.values,
        y=Top_Team_app.index,
        orientation="h",
        title="Top Nations by World Cup Appearances"
        )

        fig.update_layout(
            xaxis_title="Appearances",
            yaxis_title="Team"
        )

        st.plotly_chart(fig, use_container_width=True)
    st.divider()
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Goals Scored",
            x=top_teams.index,
            y=top_teams.values
        )
    )

    fig.add_trace(
        go.Bar(
            name="Goals Conceded",
            x=top_conceded.index,
            y=top_conceded.values
        )
    )

    fig.update_layout(
        title="Goals Scored vs Goals Conceded",
        xaxis_title="Team",
        yaxis_title="Goals",
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)

with tab3:

    st.header("Match Analysis")
    col1,col2=st.columns(2)

    with col1:
        fig = px.bar(
        x=top_matches["Total_Goals"],
        y=match_labels,
        orientation="h",
        title="Highest Scoring Matches"
        )

        fig.update_layout(xaxis_title="Total Goals",yaxis_title="Match")

        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(
        x=avg_goals_stage.values,
        y=avg_goals_stage.index,
        orientation="h",
        title="Average Goals by Stage"
        )

        fig.update_layout(
            xaxis_title="Average Goals",
            yaxis_title="Stage"
        )

        st.plotly_chart(fig, use_container_width=True)
with tab4:

    st.header("Advanced Insights")

    fig = px.line(
    x=goal_diff_year.index,
    y=goal_diff_year.values,
    markers=True,
    title="Average Goal Difference by Decade"
)

    fig.update_layout(
        xaxis_title="Decade",
        yaxis_title="Average Goal Difference"
    )

    st.plotly_chart(fig, use_container_width=True)


with tab0:
    with st.container():
        st.header(f"{selected_year} World Cup Overview")
        col1,col2,col3,col4=st.columns(4)

        col1.metric("Matches",f"{total_matches:,}")
        col2.metric("Total Goals",f"{int(total_goals):,}")
        col3.metric("Goals per Match",f"{avg_goals:.2f}")
        col4.metric("Highest Attendance",f"{int(highest_attendance):,}")
        st.divider()
    with st.expander("📜 View Matches"):
        st.header(f"Matches in the {selected_year} FIFA World Cup")
        st.dataframe(filtered_df[[ "Home_Team_Name",
                "Away_Team_Name",
                "Home_Team_Goals",
                "Away_Team_Goals",
                "Stage"]])
    st.divider()
all_teams = sorted(
    set(df["Home_Team_Name"].dropna()).union(
        set(df["Away_Team_Name"].dropna())
    )
)

selected_team = st.sidebar.selectbox(
    "Select Team",
    all_teams
)

team_matches = df[
    (df["Home_Team_Name"] == selected_team)
    |
    (df["Away_Team_Name"] == selected_team)
]
with tab0:
    

    st.header("🏠 Team Explorer")
    matches_played=len(team_matches)
    goals_scored=team_matches.loc[team_matches["Home_Team_Name"]==selected_team,"Home_Team_Goals"].sum()+team_matches.loc[team_matches["Away_Team_Name"]==selected_team,"Away_Team_Goals"].sum()
    goals_conceded=team_matches.loc[team_matches["Home_Team_Name"]==selected_team,"Away_Team_Goals"].sum()+team_matches.loc[team_matches["Away_Team_Name"]==selected_team,"Home_Team_Goals"].sum()

    goals_per_match=round(goals_scored/matches_played,2)

    col1,col2,col3,col4=st.columns(4)
    col1.metric("Total Matches Played ",matches_played)
    col2.metric("Total Goals Scored",int(goals_scored))
    col3.metric("Goals Conceded",int(goals_conceded))
    col4.metric("Goals per Match",f"{goals_per_match:.2f}")


    wins=((team_matches["Home_Team_Name"]==selected_team)
        &
        (team_matches["Home_Team_Goals"]>team_matches["Away_Team_Goals"])
        |
        (team_matches["Away_Team_Name"]==selected_team)
        &
        (team_matches["Away_Team_Goals"]>team_matches["Home_Team_Goals"])
        ).sum()
    draws=(team_matches["Away_Team_Goals"]==team_matches["Home_Team_Goals"]).sum()
    loss=matches_played-wins-draws
    win_percentage = round(wins/matches_played*100,1)

    col1,col2,col3,col4=st.columns(4)
    col1.metric("Total Wins",
                int(wins))
    col2.metric("Total loses",int(loss))
    col3.metric("Total draws",int(draws))
    col4.metric("Win percentage",f"{win_percentage}%")
    st.divider()
    fig = go.Figure(
            data=[
                go.Pie(
                    labels=["Wins", "Draws", "Loss"],
                    values=[wins, draws, loss],
                    hole=0.6,
                    marker=dict(
                        colors=["#00CC96", "#636EFA", "#EF553B"]
                    )
                )
            ]
        )

    fig.update_layout(title=f"{selected_team} Match Results",showlegend=True)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader(f"{selected_team} Matches")
    with st.expander("📜 View Match History"):

        st.dataframe(
            team_matches[
                [
                    "Year",
                    "Home_Team_Name",
                    "Home_Team_Goals",
                    "Away_Team_Goals",
                    "Away_Team_Name",
                    "Stage"
                ]
            ]
        )


st.divider()

st.caption(
    "Created by Dhruv Singh | FIFA World Cup Analytics Dashboard (1930–2014)   " \
    "Built with Python • Pandas • Plotly • Streamlit"
)

