# DATA_AGGREGATION_BIG-DATA_ANALYSIS_AND_VISUALIZATION# README for CSE587 Lab 2#


## What is this project?

-  Data was gathered from various sources using Tweepy, NYT API, Commoncrawl in Python.
- AWS EMR HDFS was used to setup the cluster and  all our data was then uploaded to AWS S3 bucket using the AWS CLI or boto3 package.

## System Requirements

- Please make sure to have Python 3 installed and AWS CLI with the required credentials.
- In addition, please install the needed packages to run the code.



# Directory Structure

Report.pdf


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
