drop table Manager;
drop table Fixtures;
drop table results;
drop table Stadium;
drop table Referee;
drop table Standings;
drop table Statistics;
drop table Fantasy_points;
drop table Team;
drop table Players;

create table Team (
team_id integer primary key,
team_name varchar(32) unique not null,
abbreviation varchar(10) unique not null,
captain varchar(32) not null,
city varchar(32) not null,
jersey_color varchar(32) not null,
website varchar(128) unique not null
);

create table Players (
player_id integer primary key,
player_name varchar(32) not null,
club varchar(32) not null,
country varchar(32) not null,
position varchar(32) not null,
age integer not null
);

create table Manager (
manager_name varchar(32) not null,
manager_id integer primary key,
country varchar(32) not null,
club varchar(32) not null,
dob date not null
);

create table Stadium (
stadium_id integer primary key,
stadium_name varchar(32) not null,
city varchar(32) not null,
club varchar(32) not null,
capacity varchar(32) not null
);

create table Referee (
ref_id integer primary key,
ref_name varchar(32) not null,
DOB date not null,
country varchar(32) not null,
matches_officiated integer not null
);

create table Standings (
team_id integer primary key,
matches_won integer,
matches_lost integer,
matches_drawn integer,
points integer,
goal_difference integer,
foreign key (team_id) references Team(team_id)
);

create table Fantasy_points (
player_ID integer primary key,
fantasy_points integer,
foreign key (player_ID) references Players(player_id)
);

create table Statistics (
player_ID integer primary key,
goals_scored integer,
assist integer,
red_cards integer,
yellow_cards integer,
mins_played integer,
foreign key (player_ID) references Players(player_id)
);


create table results(
result_ID integer,
team1_id integer,
team2_id integer,
team1_score integer,
team2_score integer,
day_of_match date,
venue varchar(32),
foreign key (team1_id) references Team(team_id),
foreign key (team2_id ) references Team(team_id),
unique( team1_id, team2_id, venue),
unique( day_of_match, venue)
);

create table Fixtures(
fixture_id integer primary key,
team1_id integer,
team2_id integer,
day_of_match date,
venue varchar(32),
foreign key (team1_id) references Team(team_id),
foreign key (team2_id ) references Team(team_id),
unique( team1_id, team2_id, venue),
unique( day_of_match, venue)
);

