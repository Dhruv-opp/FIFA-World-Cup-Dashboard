# understanding the data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("data/WorldCupMatches.csv")
# print(df.head())

#understand the colums
#print(df.columns)

#understand the shape
#print(df.shape)

#checking for null values
#print(df.isnull().sum())

#print(df.describe())

# cleaning column names

df.columns=df.columns.str.strip()
df.columns=df.columns.str.replace(" ","_")
# print(df.columns)


#h_g=df.groupby('Home_Team_Name')['Home_Team_Goals'].sum()
#print(h_g)

#visualization of top home goals teams


# top_teams = h_g.sort_values(ascending=False).head(10)

# top_teams.plot(kind="bar")

# plt.title("Top Goal Scoring Teams")
# plt.xlabel("Team")
# plt.ylabel("Goals")
# plt.savefig("visualizations/top_teams")

# plt.show()


##print(df.columns)

df["Total_goals"]=df['Home_Team_Goals']+df["Away_Team_Goals"]
# print(df[["Total_goals"]].head())
goals_per_year=df.groupby("Year")["Total_goals"].sum()
# print(goals_per_year)

# plt.figure(figsize=(12,6))

# plt.plot(
#     goals_per_year.index,
#     goals_per_year.values,
#     marker='o',
#     linewidth=2
# )

# plt.title("Goals Scored by FIFA World Cup Tournament", fontsize=16)
# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Total Goals", fontsize=12)

# plt.xticks(goals_per_year.index, rotation=45)

# plt.grid(True, linestyle='--', alpha=0.7)

# plt.tight_layout()

# plt.savefig(
#     "visualizations/goals_per_year.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()

# print(df["Total_goals"])
highs_scoring_matches=df.sort_values(by="Total_goals",ascending=False)
# print(highs_scoring_matches[["Year",
#             "Home_Team_Name",
#             "Away_Team_Name",
#             "Total_goals",
#             "MatchID"]].head(10))

# plt.figure(figsize=(12,6))

# top_matches = df.sort_values(
#     by="Total_goals",
#     ascending=False
# ).head(10)

# labels = (
#     top_matches["Home_Team_Name"]
#     + " vs "
#     + top_matches["Away_Team_Name"]
# )

# plt.barh(
#     labels,
#     top_matches["Total_goals"]
# )

# plt.title(
#     "Top 10 Highest-Scoring FIFA World Cup Matches",
#     fontsize=16
# )
# plt.xlabel("Total Goals", fontsize=12)
# plt.ylabel("Match", fontsize=12)

# plt.grid(
#     axis='x',
#     linestyle='--',
#     alpha=0.7
# )

# plt.gca().invert_yaxis()

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Matches_with_most-goals.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()

highest_attendance_per_match=df.sort_values(by="Attendance",ascending=False)
# print(highest_attendance_per_match[["Year","Attendance",
#             "Home_Team_Name",
#             "Away_Team_Name",
#             "Total_goals",
#             "MatchID"]].head(10))

attendance_per_year=df.groupby("Year")["Attendance"].sum()
highest_attendance_per_year=attendance_per_year.sort_values(ascending=False)
# print(highest_attendance_per_year.head(10))

# plt.figure(figsize=(12,6))

# plt.plot(
#     attendance_per_year.index,
#     attendance_per_year.values,
#     marker='o',
#     linewidth=2
# )

# plt.title(
#     "FIFA World Cup Attendance by Tournament",
#     fontsize=16
# )

# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Attendance", fontsize=12)

# plt.xticks(
#     attendance_per_year.index,
#     rotation=45
# )

# plt.grid(
#     True,
#     linestyle='--',
#     alpha=0.7
# )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Attendance_per_year.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()

most_goals_scored_peryear=goals_per_year.sort_values(ascending=False)
#print(most_goals_scored_peryear.head())

df = df.drop_duplicates(subset="MatchID")
df["Total_goals"]=df['Home_Team_Goals']+df["Away_Team_Goals"]
goals_per_year=df.groupby("Year")["Total_goals"].sum()
most_goals_scored_per_year=goals_per_year.sort_values(ascending=False)
# plt.figure(figsize=(12,6))

# plt.plot(
#     goals_per_year.index,
#     goals_per_year.values,
#     marker='o',
#     linewidth=2
# )

# plt.title(
#     "Total Goals by FIFA World Cup Tournament",
#     fontsize=16
# )

# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Total Goals", fontsize=12)

# plt.xticks(
#     goals_per_year.index,
#     rotation=45
# )

# plt.grid(
#     True,
#     linestyle='--',
#     alpha=0.7
# )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Goals_per_Year.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()
#print(most_goals_scored_peryear.head())


#print(df["Stage"].unique())
#print(df.columns)


goal_per_stage=df.groupby("Stage")["Total_goals"].sum()
#print(goal_per_stage)

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
#print(matches_per_stage)
avg_goals=df.groupby("Stage_Clean")["Total_goals"].mean()
#print(avg_goals)

# plt.figure(figsize=(12,6))

# plt.bar(
#     avg_goals.index,
#     avg_goals.values
# )

# plt.title(
#     "Average Goals per Match Across Tournament Stages",
#     fontsize=16
# )

# plt.xlabel("Stage", fontsize=12)
# plt.ylabel("Average Goals per Match", fontsize=12)

# plt.xticks(
#     avg_goals.index,
#     rotation=45
# )

# plt.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.7
# )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Goals_per_Stage.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()




goals_by_home=df.groupby("Home_Team_Name")["Home_Team_Goals"].sum()
goals_by_away=df.groupby("Away_Team_Name")["Away_Team_Goals"].sum()
Team_goals=goals_by_home.add(goals_by_away,fill_value=0)
Most_scoring_teams=Team_goals.sort_values(ascending=False).head(10)
# print(Most_scoring_teams)

# plt.figure(figsize=(12,7))

# plt.barh(
#     Most_scoring_teams.index,
#     Most_scoring_teams.values
# )

# plt.title(
#     "Top 10 Highest-Scoring Nations in FIFA World Cup History",
#     fontsize=16
# )

# plt.xlabel("Total Goals", fontsize=12)
# plt.ylabel("Nation", fontsize=12)

# plt.grid(
#     axis='x',
#     linestyle='--',
#     alpha=0.7
# )

# # Put the highest-scoring team at the top
# plt.gca().invert_yaxis()

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Most_Scoring_Teams.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()

df["Decade"] = (df["Year"] // 10) * 10
goals_by_decade=df.groupby("Decade")["Total_goals"].sum()
# print(goals_by_decade)

# plt.figure(figsize=(12,6))

# plt.plot(
#     goals_by_decade.index,
#     goals_by_decade.values,
#     marker='o',
#     linewidth=2
# )

# plt.title(
#     "Goals Scored by Decade in FIFA World Cup History",
#     fontsize=16
# )

# plt.xlabel("Decade", fontsize=12)
# plt.ylabel("Total Goals", fontsize=12)

# plt.xticks(
#     goals_by_decade.index,
#     rotation=45
# )

# plt.grid(
#     True,
#     linestyle='--',
#     alpha=0.7
# )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Goals_by_decade.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()
Home_teams = df[["Year", "Home_Team_Name"]]
Away_teams = df[["Year", "Away_Team_Name"]]

Home_teams.columns = ["Year", "Team"]
Away_teams.columns = ["Year", "Team"]

Teams = pd.concat([Home_teams, Away_teams])

Teams_app=Teams.groupby("Team")["Year"].nunique()
Top_Team_app=Teams_app.sort_values(ascending=False).head(10)
# print(Top_Team_app)

# plt.figure(figsize=(12,7))

# Top_Team_app = Top_Team_app.sort_values()

# plt.barh(
#     Top_Team_app.index,
#     Top_Team_app.values
# )

# plt.title(
#     "Top 10 Nations by FIFA World Cup Appearances (1930–2014)",
#     fontsize=16
# )

# plt.xlabel("Number of Appearances", fontsize=12)
# plt.ylabel("Nation", fontsize=12)

# plt.grid(
#     axis='x',
#     linestyle='--',
#     alpha=0.7
# )

# # Display values at the end of each bar
# for i, value in enumerate(Top_Team_app):
#     plt.text(
#         value + 0.2,
#         i,
#         str(value),
#         va='center'
#     )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Top Teams by Appearances.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()


goals_scored_home=df.groupby("Home_Team_Name")["Home_Team_Goals"].sum()
goals_scored_away=df.groupby("Away_Team_Name")["Away_Team_Goals"].sum()

total_goals_scored=goals_scored_home.add(goals_scored_away,fill_value=0)

goals_taken_home=df.groupby("Home_Team_Name")["Away_Team_Goals"].sum()
goals_taken_away=df.groupby("Away_Team_Name")["Home_Team_Goals"].sum()

total_goals_taken=goals_taken_home.add(goals_taken_away,fill_value=0)


team_stats=pd.DataFrame({"goals scored":total_goals_scored,"goals conceded":total_goals_taken})
final_stat=team_stats.sort_values(by="goals scored",ascending=False).head(10)
top_teams =total_goals_scored.sort_values(ascending=False).head(10)

# \Corresponding goals conceded
top_conceded = total_goals_taken[top_teams.index]

# Positions of bars
x = np.arange(len(top_teams))
width = 0.4

# plt.figure(figsize=(12,6))

# # Plot bars
# plt.bar(
#     x - width/2,
#     top_teams,
#     width,
#     label="Goals Scored"
# )

# plt.bar(
#     x + width/2,
#     top_conceded,
#     width,
#     label="Goals Conceded"
# )

# # Labels and title
# plt.xticks(
#     x,
#     top_teams.index,
#     rotation=45
# )

# plt.xlabel("Nation", fontsize=12)
# plt.ylabel("Goals", fontsize=12)

# plt.title(
#     "Goals Scored vs Goals Conceded by Top 10 Nations",
#     fontsize=16
# )

# plt.grid(
#     axis='y',
#     linestyle='--',
#     alpha=0.7
# )

# plt.legend()

# plt.tight_layout()

# plt.savefig(
#     "visualizations/Goals Scored vs Goals Conceded by Top 10 Teams.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()

df["Goal_diff"]=abs(df["Home_Team_Goals"]-df['Away_Team_Goals'])
# print(df["Goal_diff"])

goal_diff_year=df.groupby("Decade")["Goal_diff"].mean()
# print(goal_diff_year)

# plt.figure(figsize=(12,6))

# plt.plot(
#     goal_diff_year.index,
#     goal_diff_year.values,
#     marker='o',
#     linewidth=2,
#     markersize=7
# )

# # Add values above each point
# for x, y in zip(goal_diff_year.index, goal_diff_year.values):
#     plt.text(
#         x,
#         y + 0.05,
#         f"{y:.2f}",
#         ha='center',
#         fontsize=9
#     )

# plt.title(
#     "Average Goal Difference per Match by Decade",
#     fontsize=16
# )

# plt.xlabel(
#     "Decade",
#     fontsize=12
# )

# plt.ylabel(
#     "Average Goal Difference",
#     fontsize=12
# )

# plt.xticks(
#     goal_diff_year.index,
#     rotation=45
# )

# plt.grid(
#     True,
#     linestyle='--',
#     alpha=0.7
# )

# plt.tight_layout()

# plt.savefig(
#     "visualizations/goal_difference_by_decade.png",
#     dpi=300,
#     bbox_inches='tight'
# )

# plt.show()



print(df["Total_goals"])