# Social Media Emotion Detection on Remote Working
This repository contains code/report prepared for our project on "Emotion Detection on Remote Working" for the "Text Analytics" course at University of Pisa.

## Project Goal
Our goal is to gain insight and shed light on how workers feel about remote work is essential, as their emotional well-being directly influences their job performance, overall satisfaction, and mental health. To do so, we will develop an emotion model that detects a range of emotions based on posts and discussions on social media platforms that remote workers engage in. The model will rely on the “Basic Emotions” framework developed by psychologist Paul Ekman (1984), which includes the following recognized emotions:  
Anger: Characterized by furrowed brows, clenched jaws, and a narrowed gaze. Anger often arises from frustration, threat, or injustice. 
Disgust: Manifested through wrinkled nose, raised upper lip, and lowered cheeks. Disgust is typically associated with unpleasant tastes, smells, or sights. 
Fear: Expressed through wide eyes, raised eyebrows, and a parted mouth. Fear is a response to perceived danger or threat. 
Joy: Indicated by smiling, raised cheeks, and crinkled eyes. Joy is a positive emotion associated with pleasure and satisfaction. 
Sadness: Characterized by drooping eyebrows, downturned mouth, and a tearful gaze. Sadness is often a response to loss, disappointment, or grief. 
Surprise: Expressed through raised eyebrows, wide eyes, and an open mouth. Surprise is a brief emotion triggered by unexpected events. 
 
Our research and data analysis, will seek to answer these questions: 
 
How do employees feel about remote working after the COVID-19 pandemic? 
How has the emotional response to remote work changed over time?

## Project Structure

The project is organized into the following directories:

### 1. **Data Collection**
   - **Purpose**: This folder contains contains the data files used in the project and python scripts to retrieve the data.
   - **Files & Folders**:
      - `Reddit_data.ipynb`: script that retrieves data from the subreddits /remotework, /workfromhome, /remotejobs using PRAW API.
      - `Reddit_data.csv`: data retrieved from Reddit.
      - `twitter_data.py`: script that retrieves tweets from X using keywords or hashtags like #remotework #wfm using Twikit package.
      - `twitter_data.csv`: data retrieved from X
      - `twitter_config.ini`: contains information about user authentication.
      - `cookies.json`: contains information about the already authenticated user, so as to avoid repeated calls to login method.
      - `goemotions` Folder:
          - `full dataset` subfolder: contains the three raw files of data retrieved from Go Emotions dataset.
          - `emotions.txt`: contains mapping of emotions
          -  `goemotions_train.tsv`: contains training labeled data.
