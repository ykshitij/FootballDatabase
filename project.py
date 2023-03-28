import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

"# Football League Database"


@st.cache
def get_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}


@st.cache
def query_db(sql: str):
    # print(f"Running query_db(): {sql}")

    db_info = get_config()

    # Connect to an existing database
    conn = psycopg2.connect(**db_info)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute(sql)

    # Obtain data
    data = cur.fetchall()

    column_names = [desc[0] for desc in cur.description]

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    df = pd.DataFrame(data=data, columns=column_names)

    return df


try:
    table_name = st.sidebar.checkbox("Players")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Players's data"

    sql_table = f"SELECT * FROM Players;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")

try:
    table_name = st.sidebar.checkbox("Teams")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Teams data"

    sql_table = f"SELECT * FROM Team;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    table_name = st.sidebar.checkbox("Stadium")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Stadium's data"

    sql_table = f"SELECT * FROM Stadium;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    table_name = st.sidebar.checkbox("Managers")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Managers data"

    sql_table = f"SELECT * FROM Managers;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")



try:
    table_name = st.sidebar.checkbox("Referee")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Referee's data"

    sql_table = f"SELECT * FROM Referee;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")



try:
    table_name = st.sidebar.checkbox("Standings")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Standings data"

    sql_table = f"SELECT * FROM Standings;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")



try:
    table_name = st.sidebar.checkbox("Fixtures")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Fixtures"

    sql_table = f"SELECT * FROM Fixtures;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    table_name = st.sidebar.checkbox("Results")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Results"

    sql_table = f"SELECT * FROM Results;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    table_name = st.sidebar.checkbox("Statistics")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Statistics"

    sql_table = f"SELECT * FROM Statistics;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    table_name = st.sidebar.checkbox("Fantasy Points")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if table_name:
    f"Showing Fantasy Points"

    sql_table = f"SELECT * FROM fantasy_points;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


country_names = "SELECT distinct country FROM Players;"
try:
    country_table_names = query_db(country_names)["country"].tolist()
    country_name = st.sidebar.selectbox("Select Country to get club wise distribution", country_table_names)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if country_name:
    f"Showing {country_name} players in each club"

    sql_table = f"SELECT club, count(*) as Player_Count FROM Players where country = '{country_name}' group by club order by count(*) desc;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


ages = "SELECT distinct age FROM Players;"
try:
    ages_table = query_db(ages)["age"].tolist()
    age = st.sidebar.slider('Select age', 16, 38, 25)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if age:
    f"Showing goals scored by players of age {age} at respective clubs"

    sql_table = f"select Players.club, sum(Statistics.goals_scored) as Goals from Players JOIN Statistics ON Players.player_id=Statistics.player_ID where Players.age='{age}' group by Players.club having sum(Statistics.goals_scored)>0 order by sum(Statistics.goals_scored) desc;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_table_names = query_db(team_names)["team_name"].tolist()
    team_name = st.sidebar.selectbox("Select Team to get statistics", team_table_names)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing {team_name}'s Statistics"

    sql_table = f"Select P.player_name,F.fantasy_points, S.goals_scored, S.assist, S.yellow_cards, S.red_cards From Fantasy_points F, Statistics S,Players P,Team T Where P.Club = T.team_name And F.player_ID = P.player_ID And S.player_ID = P.player_ID And T.team_name =  '{team_name}';"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_table_names = query_db(team_names)["team_name"].tolist()
    team_name = st.sidebar.checkbox("Select to get Captain and Manager info")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing captain and manager names for different football club"

    sql_table = f"select Team.team_name, Team.captain, Manager.manager_name from Team JOIN Manager ON Team.team_name=Manager.club;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_table_names = query_db(team_names)["team_name"].tolist()
    team_name = st.sidebar.checkbox("Select to see fairplay stats")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing Clubs Discipline stats"

    sql_table = f"Select T.team_name, sum(S.yellow_cards) as Yellow_Cards, sum(S.red_cards) as Red_Cards From Statistics S,Players P,Team T Where S.player_ID = P.player_ID And P.Club = T.team_name Group by T.team_name;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


try:
    team_name = st.sidebar.checkbox("Select to see Matches Officiated by Referee's on a country level")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing Matches Officiated by Referee's on a country level"

    sql_table = f"SELECT Referee.Country, sum(Referee.matches_officiated) as Matches_Officiated FROM Referee GROUP BY Referee.Country;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_name = st.sidebar.checkbox("Select to get ticket booking information")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing Stadium and Website Information to book tickets"

    sql_table = f"select Team.team_name, Team.city, Stadium.Capacity, Team.website FROM Team JOIN Stadium ON Team.team_name = Stadium.club;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_table_names = query_db(team_names)["team_name"].tolist()
    team_name = st.sidebar.selectbox("Select Team to Home and Away Goals scored", team_table_names)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing {team_name}'s Home and Away Goals Scored"

    sql_table = f"SELECT T1.team_name, sum(R.team1_score) as HomeGoals, sum(R.team2_score) as AwayGoals FROM Results R, Team T1 WHERE R.team1_id = T1.team_id and T1.team_name = '{team_name}' Group by T1.team_name;"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")


team_names = "SELECT team_name FROM Team;"
try:
    team_table_names = query_db(team_names)["team_name"].tolist()
    team_name = st.sidebar.selectbox("Select Team to see next Season's fixtures", team_table_names)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")

if team_name:
    f"Showing {team_name}'s ALL Home and Away games next season"

    sql_table = f" SELECT Team.team_name, Fixtures.day_of_match FROM Team JOIN Fixtures ON Team.team_id = Fixtures.team1_id WHERE Team.team_name = '{team_name}' UNION SELECT Team.team_name, Fixtures.day_of_match FROM Team JOIN Fixtures ON Team.team_id = Fixtures.team2_id WHERE Team.team_name = '{team_name}';"
    try:
        df = query_db(sql_table)
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again.")
