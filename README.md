# Project Overview
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The object of this project is to to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

# Python Scripts

•	 create_table.py is where you'll create your fact and dimension tables for the star schema in Redshift.

•	 etl.py is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.

•	 sql_queries.py is where you'll define you SQL statements, which will be imported into the two other files above.

# Data Schema
## Fact Table
•	songplays - records in event data associated with song plays. Columns for the table:

    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

## Dimension Tables
•	users

    user_id, first_name, last_name, gender, level
    
•	songs

    song_id, title, artist_id, year, duration
    
•	artists

    artist_id, name, location, lattitude, longitude
    
•	time

    start_time, hour, day, week, month, year, weekday

# Project Steps
1. Create a redshift cluster and keep all the useful configuration and fill in the dwh.cfg file.

2. Setup Configurations in the dwh.cfg file 

3. Create tables by running the following code in the bash shell
    'python create_tables.py'

4. Load Data by running the following code in the bash shell
    'python create_tables.py'
