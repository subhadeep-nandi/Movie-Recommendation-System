# 🎬 Movie Recommendation System

A machine learning based web application that recommends movies similar to a selected movie based on movie metadata.

The recommendation system is built using **Content-Based Filtering**, **CountVectorizer**, and **Cosine Similarity**, and deployed using **Streamlit**.

---

## 📌 Project Overview

Movie recommendation systems help users discover movies based on the characteristics of movies they already like.

This project uses the following movie information to generate recommendations:

* Movie Overview
* Genres
* Keywords
* Top 3 Cast Members
* Director

These features are combined into a single text-based feature called `tags`.

The movie tags are then converted into numerical vectors using **CountVectorizer**.

Finally, **Cosine Similarity** is used to calculate the similarity between movies.

The system recommends the **Top 5 movies** that are most similar to the selected movie.

---

## 🖥️ Application Preview

The Movie Recommendation System provides an interactive Streamlit interface where users can select a movie and receive similar movie recommendations.

The application also provides:

* Movie posters
* Movie ratings
* Release year
* Movie genres
* Movie overview
* Movie trailers
* Minimum rating filter
* Release year filter
* Genre filter

---

## 🎯 Objective

The objective of this project is to develop an end-to-end machine learning application that:

1. Loads and preprocesses the movie datasets.
2. Combines movie and credits datasets.
3. Extracts useful movie metadata.
4. Performs feature engineering.
5. Creates a combined `tags` feature.
6. Applies text preprocessing and stemming.
7. Converts movie tags into numerical vectors using CountVectorizer.
8. Calculates movie similarity using Cosine Similarity.
9. Recommends the Top 5 similar movies.
10. Integrates the TMDB API for movie information.
11. Provides a user-friendly web interface using Streamlit.

---

## 🤖 Machine Learning Model

The project uses a:

**Content-Based Filtering Recommendation System**

The recommendation system recommends movies based on the similarity between their metadata.

### Features Used

The following features are used to create the movie representation:

```text
Movie Overview
       +
Genres
       +
Keywords
       +
Top 3 Cast Members
       +
Director
       ↓
Combined Tags
Text Preprocessing

The movie metadata is processed using:

Lowercase conversion
Tokenization
Stop-word removal
Porter Stemming

The project uses:

PorterStemmer()

from NLTK for stemming.

Feature Vectorization

The processed movie tags are converted into numerical vectors using:

CountVectorizer(
    max_features=5000,
    stop_words='english'
)
Similarity Calculation

The similarity between movies is calculated using:

cosine_similarity(vectors)

A higher cosine similarity value indicates greater similarity between the corresponding movie metadata vectors.

🔄 Machine Learning Pipeline
TMDB Movies Dataset
        +
TMDB Credits Dataset
        ↓
Merge Datasets
        ↓
Select Required Features
        ↓
Handle Missing Values
        ↓
Extract Genres
        ↓
Extract Keywords
        ↓
Extract Top 3 Cast
        ↓
Extract Director
        ↓
Create Combined Tags
        ↓
Convert Text to Lowercase
        ↓
Porter Stemming
        ↓
CountVectorizer
        ↓
Movie Vectors
        ↓
Cosine Similarity
        ↓
Similarity Matrix
        ↓
Top 5 Similar Movies
        ↓
Streamlit Web Application

📊 Recommendation Process

When a user selects a movie, the application follows these steps:

Finds the selected movie in the dataset.
Retrieves its similarity scores.
Sorts movies according to similarity.
Removes the selected movie from the recommendations.
Selects the Top 5 similar movies.
Retrieves additional movie information using the TMDB API.
Displays the recommendations in the Streamlit application.
Recommendation Workflow
Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Scores
      ↓
Sort Similarity Scores
      ↓
Select Top 5 Similar Movies
      ↓
Fetch Movie Details
      ↓
Display Recommendations

🗂️ Dataset

The project uses the TMDB 5000 Movies Dataset.

The datasets used are:

tmdb_5000_movies.csv
tmdb_5000_credits.csv
Movie Dataset

The movie dataset contains information related to:

Movie ID
Movie title
Movie overview
Genres
Keywords
Other movie metadata
Credits Dataset

The credits dataset contains:

Cast information
Crew information
Director information

The two datasets are merged using the movie title to create the final dataset used for recommendation.

📋 Dataset Features
Feature	Description
movie_id	Unique movie identifier
title	Movie title
overview	Movie description
genres	Movie genre information
keywords	Keywords associated with the movie
cast	Movie cast information
crew	Movie crew information
tags	Combined movie metadata used for recommendation
🛠️ Technologies Used
Python
NumPy
Pandas
Scikit-learn
NLTK
Streamlit
Requests
TMDB API
Jupyter Notebook
Git & GitHub
Machine Learning Libraries
CountVectorizer for text vectorization
cosine_similarity for calculating movie similarity
PorterStemmer for text stemming

📁 Project Structure
Movie-Recommendation-System/
│
├── app_file.py
├── Movie_Recommender_System.ipynb
│
├── movie_dict.pkl
├── movies.pkl
│
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── requirements.txt
├── README.md
└── .gitignore
File Description
File	Description
app_file.py	Streamlit web application for movie recommendations
Movie_Recommender_System.ipynb	Complete machine learning and data preprocessing workflow
movie_dict.pkl	Processed movie data used by the application
movies.pkl	Processed movie dataset
tmdb_5000_movies.csv	Movie metadata dataset
tmdb_5000_credits.csv	Movie cast and crew dataset
requirements.txt	Python dependencies required to run the project
.gitignore	Files and folders excluded from Git

Note: similarity.pkl is generated by the notebook but is not included in the GitHub repository because its file size exceeds GitHub's standard 100 MB file limit.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/subhadeep-nandi/Movie-Recommendation-System.git
2. Navigate to the Project Directory
cd Movie-Recommendation-System
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

For Windows PowerShell:

.\venv\Scripts\Activate.ps1

If PowerShell prevents script execution, you can activate the environment using Command Prompt:

venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
🔑 TMDB API Configuration

This project uses the TMDB API to retrieve dynamic movie information such as:

Movie posters
Movie ratings
Release year
Genres
Movie overview
Movie trailers

Create the following file:

.streamlit/secrets.toml

Add your TMDB API key:

TMDB_API_KEY = "YOUR_API_KEY"

⚠️ Important: Never upload your API key or secrets.toml file to GitHub.

The secrets.toml file is excluded using .gitignore.

▶️ Run the Application

Start the Streamlit application using:

streamlit run app_file.py

The application will open in your browser.

Usually, the application will be available at:

http://localhost:8501
🎬 How the Application Works

The user selects a movie from the Streamlit interface.

The system then:

User Selects Movie
       ↓
Find Movie Index
       ↓
Retrieve Similarity Scores
       ↓
Sort Movies by Similarity
       ↓
Select Top 5 Similar Movies
       ↓
Fetch Movie Details from TMDB API
       ↓
Display Movie Recommendations
🔍 Application Features
🎥 Movie Recommendations

The application recommends the Top 5 movies similar to the selected movie.

⭐ Rating Filter

Users can specify a minimum movie rating to filter recommendations.

📅 Year Filter

Users can specify a release-year range to filter recommendations.

🎭 Genre Filter

Users can select a preferred genre to filter the recommended movies.

🖼️ Movie Posters

Movie posters are dynamically retrieved using the TMDB API.

🎥 Movie Trailers

The application retrieves available YouTube trailers through TMDB movie information.

📖 Movie Overview

The application displays a short overview of each recommended movie.

⚡ API Optimization

TMDB API requests use caching and retry handling to improve reliability and reduce unnecessary API requests.

💾 Pickle Files

The machine learning pipeline generates pickle files used by the Streamlit application.

movies.pkl

Stores the processed movie dataset.

movie_dict.pkl

Stores the processed movie information in dictionary format.

similarity.pkl

Stores the cosine similarity matrix used to generate movie recommendations.

Note: similarity.pkl is not included in the GitHub repository because the file size exceeds GitHub's standard 100 MB limit.

To run the application after cloning the repository, generate similarity.pkl by running the notebook.

🧠 Generate similarity.pkl

Open Jupyter Notebook:

jupyter notebook

Open:

Movie_Recommender_System.ipynb

Run the notebook cells from the beginning.

The notebook performs:

Data Loading
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Text Preprocessing
      ↓
Porter Stemming
      ↓
CountVectorizer
      ↓
Cosine Similarity
      ↓
Save Pickle Files

The generated files include:

movie_dict.pkl
movies.pkl
similarity.pkl
📌 Project Workflow

The complete project workflow is:

Raw Movie Data
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Feature Engineering
      ↓
Create Movie Tags
      ↓
Text Preprocessing
      ↓
Porter Stemming
      ↓
CountVectorizer
      ↓
Cosine Similarity
      ↓
Recommendation Engine
      ↓
TMDB API Integration
      ↓
Streamlit Application
🚀 Future Improvements

Some possible improvements for future versions include:

Improve recommendation filtering by applying filters before selecting the final Top 5 movies.
Handle duplicate movie titles more robustly.
Optimize TMDB API requests.
Improve API error handling.
Add recommendation evaluation metrics.
Add collaborative filtering.
Build a hybrid recommendation system.
Add personalized recommendations.
Improve the Streamlit user interface.
Add interactive visualizations.
Deploy the application online.
⚠️ Limitations

The current system has some limitations:

The recommendation system is based on movie metadata.
It does not use individual user-rating history.
Recommendation quality depends on the available movie metadata.
Dynamic movie information requires TMDB API access.
similarity.pkl is not stored in the GitHub repository because of its large file size.
The similarity matrix needs to be generated from the notebook when setting up the project from scratch.
📌 Project Highlights
Developed an end-to-end Content-Based Movie Recommendation System.
Performed feature engineering using movie overview, genres, keywords, cast, and director.
Applied Porter Stemming for text preprocessing.
Used CountVectorizer for text feature extraction.
Used Cosine Similarity to calculate movie similarity.
Generated a similarity matrix for movie recommendations.
Recommended the Top 5 similar movies.
Built an interactive Streamlit web application.
Integrated the TMDB API for dynamic movie information.
Implemented API caching and retry handling.
Used Git and GitHub for project version control.
📚 Skills Demonstrated
Python
Python programming
Functions
Lists and dictionaries
File handling
Exception handling
API requests
Data Science
Data loading
Data cleaning
Data preprocessing
Feature engineering
Working with structured datasets
Machine Learning
Recommendation systems
Content-based filtering
Text vectorization
Cosine similarity
Natural Language Processing
Text preprocessing
Tokenization
Stop-word removal
Stemming
Deployment
Streamlit
API integration
Web application development
Development Tools
Jupyter Notebook
Git
GitHub
Virtual environments
📜 Disclaimer

This project uses the TMDB API for retrieving movie-related information.

This project is developed for educational, learning, and portfolio purposes.

The project is not endorsed or certified by TMDB.

👨‍💻 Author

Subhadeep Nandi

M.Sc. Mathematics and Computing
IIT (ISM) Dhanbad

🔗 Connect with me

LinkedIn:
https://www.linkedin.com/in/subhadeep-nandi-8140672a7

GitHub:
https://github.com/subhadeep-nandi

⭐ Acknowledgement

This project was developed as a machine learning project for learning, practical implementation, and portfolio development.

The project helped in gaining practical experience with:

Machine Learning
Natural Language Processing
Recommendation Systems
Data Preprocessing
Feature Engineering
Streamlit
API Integration
Git and GitHub

If you find this project useful, consider giving the repository a ⭐ on GitHub.s