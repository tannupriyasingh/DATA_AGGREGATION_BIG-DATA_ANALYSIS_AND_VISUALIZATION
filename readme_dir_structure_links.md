# README for CSE587 Lab 2#

The following directory contains all the required files for Lab 2

Please read before performing any actions.

## What is this project?

- It is the Lab 2 Project where we gathered data from various sources using Tweepy, NYT API, Commoncrawl in Python.
- We used AWS EMR HDFS to setup our cluster and uploaded all our data to AWS S3 bucket using the AWS CLI or boto3 package.

## System Requirements

- Please make sure to have Python 3 installed and AWS CLI with the required credentials.
- In addition, please install the needed packages to run the code.

# Links
Commoncrawl —> https://public.tableau.com/profile/rakshit.viswanatham#!/vizhome/CommoncrawlDataVisualization/AllSheets

NYT —> https://public.tableau.com/profile/rakshit.viswanatham#!/vizhome/NYTDataVisualization/AllSheets

Twitter —> https://public.tableau.com/profile/rakshit.viswanatham#!/vizhome/TwitterDataVisualization/AllSheets

Video -> https://buffalo.app.box.com/file/444133194704

# Directory Structure
Report.pdf
Video.mp4
Part 1
    Code
        cc_scraper.py - Scraper to get Commoncrawl data.
        nyt_scraper.py - Scraper to get NYT data.
        twitter_scraper.py - Scraper to get Twitter data.
    Data
        Commoncrawl
            Clean Data - Processed Data.
            Raw Data - Raw data that was gathered, with articles per file in the title.
        NYT
            Clean Data - Processed Data.
            Raw Data - Gathered data per keyword.
        Test Data
            Clean Data - Processed Data.
            Raw Data - File given for testing Word Count.
        Twitter
            Clean Data - Processed Data.
            Raw Data - Tweets gathered per keyword with count in each file.
Part 2
    wordcount-mr - MR for Word Count
    pre_processing.ipynb - Pre-processing for an type of data and just ours.
    stopwords_clean.txt - All the needed stopwords.
    test_data_output.txt - Test data for the demo file.
    test_data_wordcloud.jpg - Image of the word cloud for it.
    test_data_wordcloud.twbx - Tableau Workbook
Part 3
    Commoncrawl
        Code - Cleaning and co-occurence MR.
        Images - Images and the Tableau workbook with the output.
        Output - Output of the AWS EMR for Word Count and co-occurence.
    NYT
        Code - Cleaning and co-occurence MR.
        Images - Images and the Tableau workbook with the output.
        Output - Output of the AWS EMR for Word Count and co-occurence.
    Test Data
        Code - Cleaning and co-occurence MR.
        Images - Images and the Tableau workbook with the output.
        Output - Output of the AWS EMR for Word Count and co-occurence.
    Twitter
        Code - Cleaning and co-occurence MR.
        Images - Images and the Tableau workbook with the output.
        Output - Output of the AWS EMR for Word Count and co-occurence.
