# Breaking Bad Data Code Submission

## Table of Contents

- [Breaking Bad Data Code Submission](#breaking-bad-data-code-submission)
  - [Table of Contents](#table-of-contents)
  - [Goal of this Project](#goal-of-this-project)
    - [Task](#task)
    - [Objectives](#objectives)
    - [Project Structure](#project-structure)
  - [Authors](#authors)
  - [Acknowledgements](#acknowledgements)
      

## Goal of this Project

In an era where artificial intelligence (AI) is rapidly evolving, public perception is significantly influenced by how AI is portrayed by the media. This year’s RAISE 2024 data science competition delves into the intricate relationship between public opinion of AI and media narratives. The challenge is to determine whether news media plays any role in fostering a sense of fear or apprehension towards AI and to identify dominant themes, sentiments, and topics that AI news headlines convey. 

### Task
Participants will be provided with a dataset containing news headlines related to AI. Their task is to analyze these headlines to uncover the narratives surrounding AI in the media. The challenge involves using analytical text analytics and natural language processing (NLP) techniques to extract meaningful insights from these headlines. The goal is to generate innovative data-supported insights that deepen our understanding of media dynamics, promoting a more informed and empowered public discourse on AI.

### Objectives
- Analyze news headlines to identify prevalent themes, sentiments, and topics related to AI.
- Determine if news media contributes to a sense of fear or apprehension towards AI.
- Use NLP techniques to extract meaningful insights and patterns from the headlines.
- Provide data-supported recommendations for promoting a more informed public discourse on AI.

### Project Structure

- `./data`: Contains all necessary data files, including both provided datasets and generated CSV files after preprocessing.
- `./corpus`: Directory for installing NLTK built-in corpus.

### High-Level Description

#### Required Data Files in `./data` Directory
- `labeled_headlines_10k.csv`
- `Dataset_10k.csv`

#### File Functions

1. **Cleaning/Preprocessing Files**
    - `cleaning_csv.ipynb`: Notebook for cleaning and preprocessing CSV data.
    - `preprocessing.ipynb`: Notebook for general data preprocessing steps.

2. **Exploratory Data Analysis (EDA)**
    - `EDA_P1.ipynb`: First part of EDA focusing on initial data exploration and simple visualizations.
    - `EDA_Pt2.ipynb`: Second part of EDA with further exploration and visualizations.

3. **Sentiment Analysis Techniques**
    - `Vader.ipynb`: Notebook implementing sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool.
    - `ZeroShotEmotions.ipynb`: Utilizes zero-shot classification to analyze emotions in the dataset.
    - `zeroShotmodel.ipynb`: Implements a custom zero-shot classification model for sentiment analysis.
    - `lda.ipynb`: Notebook for Latent Dirichlet Allocation (LDA) topic modeling.

4. **Additional Analytics and Visualizations**
    - `emotion_distributions.ipynb`: Analyzes emotion distributions within the dataset.
    - `visualizations.ipynb`: Provides additional visualizations and analytics.

#### Authors
- 

#### Acknowledgements
Special thanks to the RAISE-24 Datathon organizers for providing the opportunity to work on this exciting project!

For any inquiries or suggestions, please contact asr658@nyu.edu.

Happy Analyzing! 🚀
