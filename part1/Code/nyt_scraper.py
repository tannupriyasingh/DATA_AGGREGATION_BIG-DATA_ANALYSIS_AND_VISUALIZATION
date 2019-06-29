# -*- coding: utf-8 -*-

# Import all the required packages
from yanytapi import SearchAPI
import json
import requests
from bs4 import BeautifulSoup

# This function takes care of reading each URL from the list of articles and then go through BeautifulSoup and
# get the entire text that is contained in the <p> tags for the article
def gather_data(nyt_articles):
    global total
    articles_list = []
    total_articles: int = 0
    for article in nyt_articles:
        if article.document_type == 'article':
            total_articles += 1
            # We get the full article in form of HTML
            r = requests.get(article.web_url)
            # We put it through BeautifulSoup and parse the HTML
            soup = BeautifulSoup(r.text, 'html.parser')
            # Find all the <p> tags as that will contain the article's body
            data = soup.find_all('p')
            full_text = ''
            # For each <p> tag, we check if it doesn't contain the generic words and
            # does not start with "By" as we do not need the author's information then
            # save the required fields from the arrticle and the full body into a json object
            for p_tag in data:
                if (p_tag.text != 'Advertisement') and (p_tag.text != 'Supported by') and (p_tag.text != 'Follow The New York Times Opinion section on Facebook, Twitter (@NYTopinion) and Instagram.'):
                    if not p_tag.text.startswith('By'):
                        full_text = full_text + " " + p_tag.text

            clean_article: object = {
                'type': 'nyt',
                'headline': article.headline['main'],
                'full_text': full_text,
                'id': article._id,
                'date': article.pub_date
            }

            # The JSON object is then saved and added to a list of articles body.
            print(clean_article)
            articles_list.append(clean_article)
            print(total_articles, total)
    total = total + total_articles
    return articles_list

# This function read the full object with all the articles and
# writes it to a file and saves it.
def write_to_file(name, articles_list1):
    file_name = "nyt_json_" + name.lower().replace(" ", "_") + ".txt"
    with open(file_name, "w") as open_file:
        json.dump(articles_list1, open_file, ensure_ascii=False)

# total number of articles collected in the sub-topic search
total = 0
# API Key used to gather all the data
nyt_api = SearchAPI('8VF5m7ti4XSy9V74fxlvpf870KTIvAgF')
#All the keywrods used to gather the articles divided in sub-topics
topic_words1 = [
    #Immigration:
    'Souther Border', 'Border Wall', 'Kirstjen Nielsen', 'Green Card', 'dhs', 'daca',  'homeland security'
]
topic_words2 = [
    'Cortez', 'Green New Deal', 'Climate Change', 'E.P.A', 'Single Payer', 'Obamacare', 'Medicaid', 'Medicare', 'Planned Parenthood', 'Affordable Care Act', '2020 democrat', '2020 elections', "Beto O'Rourke", 'Bernie Sanders', 'Elizabeth Warren', 'joe biden', 'Kamala Harris', 'no Collusion', 'barr', 'russia inquiry', 'Mueller report', 'robert mueller', 'N.R.A', 'Gun Law', 'Gun Violence', 'Mass Shootings'
]

# For each sub-topic, a topic is selected and then
# It is run through the search if the headline contains
# that article.
for topic in topic_words1:
    print(topic)
    # setting the topic as the headline
    fq = {"headline": topic}
    # This will do the API search for NYT and gather list of articles
    # that would have the topic as the headline
    articles = nyt_api.search(topic, begin_date="20190101", fq=fq)
    # We get the article data and gather the required fields from the articles
    final_list = gather_data(articles)
    # Then write the data to a new file.
    write_to_file(topic, final_list)
