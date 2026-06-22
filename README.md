# 🏆 FIFA World Cup Analytics Dashboard

An interactive dashboard for analyzing FIFA World Cup tournaments from 1930–2014 using Python, Pandas, Plotly, and Streamlit.

## 🚀 Live Demo

https://fifa-world-cup-dashboard-zund7kbm8vubyfwwmspvhe.streamlit.app

## 📌 Features

* 📈 Tournament Trends
* ⚽ Team Explorer
* 📊 Interactive Plotly Charts
* 🏆 Team Performance Analysis
* 🎯 Year and Team Filters
* 🍩 Match Outcome Donut Chart
* 📋 Expandable Match History Tables

# 🔍 Key Findings

## Tournament Goal Trends

* The 1998 FIFA World Cup recorded the highest number of goals among the tournaments included in the cleaned dataset.
* The five highest-scoring tournaments were **1998, 2014, 2002, 2006, and 1982**.
* Modern World Cups generally produce more goals, partly due to the increase in the number of participating teams and matches.

---

## Highest-Scoring Matches

* The match between **Austria and Switzerland in 1954** produced the highest number of goals in World Cup history, with a total of **12 goals**.
* Historical tournaments occasionally featured extremely high-scoring encounters, highlighting differences in playing styles across eras.

---

## Attendance Patterns

* The **1950 World Cup match between Uruguay and Brazil** attracted the largest crowd in the dataset, with an attendance of **173,850 spectators**.
* The **2014 FIFA World Cup** recorded the highest overall tournament attendance, exceeding **4.3 million spectators**.
* These results demonstrate the growing global popularity and commercial success of the World Cup.

---

## Goal Scoring Across Tournament Stages

* Group-stage matches account for the largest share of games and goals scored.
* As the tournament progresses, teams tend to adopt more cautious and tactical approaches.
* Knockout rounds and finals generally produce fewer goals due to the increased importance of avoiding mistakes.
* The findings suggest that defensive discipline becomes increasingly important in the later stages of the competition.

---

## Historical Team Performance

* **Brazil emerged as the highest-scoring nation** in the dataset, followed by several traditional football powers.
* Countries with long histories of World Cup success consistently maintain strong attacking records across generations.
* Brazil, Germany, and Italy stand out as some of the most prolific teams in World Cup history.

---

## Attacking and Defensive Records

* Strong attacking teams do not necessarily possess equally strong defensive records.
* Different nations have achieved success through different styles of play.
* Some teams relied primarily on attacking dominance, while others combined offensive strength with defensive solidity.

---

## World Cup Appearances

* **Brazil is the only nation to have participated in every World Cup between 1930 and 2014**, recording 20 appearances.
* Italy and Argentina followed with 18 and 16 appearances respectively.
* Traditional football powers such as Brazil, Italy, Argentina, Germany, England, France, and Spain have demonstrated remarkable consistency across multiple generations.

---

## Competitiveness Across Decades

* The average goal difference per match has steadily declined over time.
* Early tournaments were characterized by larger score margins and more one-sided contests.
* Since the 1960s, World Cup matches have become increasingly competitive.
* The trend indicates that the quality gap between nations has narrowed, resulting in more balanced and closely contested matches in modern tournaments.

---

## Data Cleaning and Standardization

* Duplicate matches were identified and removed using the unique MatchID field to ensure accurate tournament statistics.
* Historical stage names were standardized into common categories such as **Group Stage, Round of 16, Quarter-finals, Semi-finals, Third Place, and Final**.
* This standardization enabled meaningful comparisons across different World Cup eras and improved the reliability of stage-level analyses.


## 🛠️ Technologies Used

* Python
* Pandas
* Plotly
* Streamlit
* Matplotlib

## 📊 Insights

* Goals scored across tournaments over time
* Attendance trends
* Highest scoring teams
* Top nations by appearances
* Goal difference by decade
* Stage-wise goal analysis
* Highest scoring matches

## 🚀 How to Run

```bash
pip install -r requirements.txt

streamlit run app.py
```

## 📂 Project Structure

```text
FIFA-World-Cup-Dashboard/
│
├── app.py
├── main.py
├── world_cup_matches.csv
├── requirements.txt
├── README.md
├── visualizations/
└── screenshots/
```
## 📸 Dashboard Preview

## Home Tab
![Home Dashboard](<screenshots/Home.png>)

## World cup Overview
![World cup Overview](<screenshots/World cup Overview.png>)

## Team Explorer
![Team Explorer](<screenshots/Team explorer.png>)

## Tournament Trends
![Tournament trends](<screenshots/Tournament trends.png>)

## Teams Analysis
![Teams Analysis](<screenshots/Teams analysis.png>)

## Matches Analysis
![Matches Analysis](<screenshots/Matches analysis.png>)

## Advanced Insights
![Advanced Insights](<screenshots/Advanced insights.png>)

## 🚀 Built with

Python • Pandas • Plotly • Streamlit
