import streamlit as st
import pandas as pd
import pickle
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       MAIN BACKGROUND
       ============================== */

    .stApp {
        background:
            radial-gradient(
                circle at top center,
                rgba(150, 0, 0, 0.22),
                transparent 38%
            ),
            linear-gradient(
                135deg,
                #050505 0%,
                #0b0b0b 55%,
                #140000 100%
            );

        color: #f5f5f5;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ==============================
       TITLE
       ============================== */

    h1 {
        font-family: "Trebuchet MS", sans-serif;
        font-size: 42px !important;
        font-weight: 800;
        letter-spacing: 0.5px;

        color: white;

        background:
            linear-gradient(
                90deg,
                #ffffff 0%,
                #ff3b3b 45%,
                #b30000 100%
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        text-shadow:
            0 0 18px rgba(180, 0, 0, 0.25);
    }


    /* ==============================
       SUBTITLE
       ============================== */

    .project-subtitle {

        font-family: "Trebuchet MS", sans-serif;

        color: #a8a8a8;

        font-size: 16px;

        margin-top: -8px;

        margin-bottom: 25px;
    }


    /* ==============================
       SECTION HEADINGS
       ============================== */

    .section-title {

        font-family: "Trebuchet MS", sans-serif;

        font-size: 25px;

        font-weight: 700;

        color: #ffffff;

        border-left:
            4px solid #c40000;

        padding-left: 12px;

        margin-top: 28px;

        margin-bottom: 16px;
    }


    /* ==============================
       SIDEBAR
       ============================== */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #090909 0%,
                #120000 100%
            );

        border-right:
            1px solid #3a0a0a;
    }


    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {

        font-family:
            "Trebuchet MS",
            sans-serif;

        color: #ffffff !important;
    }


    /* ==============================
       INPUT BOX
       ============================== */

    div[data-baseweb="input"] {

        background-color: #111111;

        border:
            1px solid #353535;

        border-radius: 7px;
    }


    div[data-baseweb="input"]:focus-within {

        border:
            1px solid #b30000;
    }


    /* ==============================
       SELECT BOX
       ============================== */

    div[data-baseweb="select"] > div {

        background-color: #111111;

        border:
            1px solid #353535;

        border-radius: 7px;
    }


    /* ==============================
       RECOMMEND BUTTON
       ============================== */

    .stButton > button {

        background:
            linear-gradient(
                135deg,
                #8b0000 0%,
                #d00000 50%,
                #650000 100%
            );

        color: #ffffff;

        border:
            1px solid #e00000;

        border-radius: 8px;

        font-family:
            "Trebuchet MS",
            sans-serif;

        font-size: 16px;

        font-weight: 700;

        padding: 11px 20px;

        box-shadow:
            0 5px 18px
            rgba(150, 0, 0, 0.30);

        transition:
            all 0.2s ease;
    }


    .stButton > button:hover {

        background:
            linear-gradient(
                135deg,
                #b00000,
                #f00000,
                #7a0000
            );

        border-color: #ff3333;

        box-shadow:
            0 7px 25px
            rgba(210, 0, 0, 0.45);

        transform:
            translateY(-1px);
    }


    /* ==============================
       TRAILER BUTTON
       ============================== */

    .stLinkButton > a {

        background:
            linear-gradient(
                135deg,
                #1a1a1a,
                #2b0000
            );

        color: #ff5c5c !important;

        border:
            1px solid #641010;

        border-radius: 7px;

        font-family:
            "Trebuchet MS",
            sans-serif;

        font-weight: 600;

        transition:
            all 0.2s ease;
    }


    .stLinkButton > a:hover {

        background:
            linear-gradient(
                135deg,
                #350000,
                #650000
            );

        color: #ffffff !important;

        border-color: #c40000;
    }


    /* ==============================
       MOVIE CARD
       ============================== */

    .movie-card {

        background:
            linear-gradient(
                145deg,
                #151515,
                #0d0d0d
            );

        border:
            1px solid #292929;

        border-radius: 10px;

        padding: 12px;

        margin-bottom: 15px;

        box-shadow:
            0 8px 25px
            rgba(0, 0, 0, 0.45);

        transition:
            all 0.2s ease;
    }


    .movie-card:hover {

        border-color: #8b0000;

        box-shadow:
            0 10px 30px
            rgba(130, 0, 0, 0.25);

        transform:
            translateY(-3px);
    }


    /* ==============================
       MOVIE TITLE
       ============================== */

    .movie-title {

        font-family:
            "Trebuchet MS",
            sans-serif;

        font-size: 18px;

        font-weight: 700;

        color: #ffffff;

        margin-top: 10px;

        margin-bottom: 8px;
    }


    /* ==============================
       MOVIE INFORMATION
       ============================== */

    .movie-info {

        font-family:
            "Trebuchet MS",
            sans-serif;

        font-size: 14px;

        color: #a9a9a9;

        line-height: 1.6;
    }


    /* ==============================
       SIMILARITY
       ============================== */

    .similarity {

        color: #ff4d4d;

        font-weight: 700;
    }


    /* ==============================
       EXPANDER
       ============================== */

    div[data-testid="stExpander"] {

        background-color: #111111;

        border:
            1px solid #292929;

        border-radius: 8px;
    }


    /* ==============================
       DIVIDER
       ============================== */

    hr {

        border: none;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                #6d0000,
                #c00000,
                #6d0000,
                transparent
            );

        margin: 30px 0;
    }


    /* ==============================
       FOOTER
       ============================== */

    .footer {

        text-align: center;

        color: #666666;

        font-family:
            "Trebuchet MS",
            sans-serif;

        font-size: 13px;

        padding-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# TMDB SESSION WITH RETRY
# =========================================================

session = requests.Session()

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[
        429,
        500,
        502,
        503,
        504
    ],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(
    max_retries=retry_strategy
)

session.mount(
    "https://",
    adapter
)

session.mount(
    "http://",
    adapter
)


# =========================================================
# LOAD MOVIE DATA
# =========================================================

with open(
    "movie_dict.pkl",
    "rb"
) as file:

    movie_dict = pickle.load(file)

movies = pd.DataFrame(movie_dict)


# =========================================================
# LOAD SIMILARITY MATRIX
# =========================================================

with open(
    "similarity.pkl",
    "rb"
) as file:

    similarity = pickle.load(file)


# =========================================================
# FETCH TRAILER
# =========================================================

@st.cache_data(ttl=3600)
def fetch_trailer(movie_id, api_key):

    try:

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{movie_id}/videos"
        )

        response = session.get(
            url,
            params={
                "api_key": api_key,
                "language": "en-US"
            },
            timeout=10
        )

        response.raise_for_status()

        videos = response.json().get(
            "results",
            []
        )

        # First look for an official YouTube trailer
        for video in videos:

            if (
                video.get("site") == "YouTube"
                and video.get("type") == "Trailer"
                and video.get("official") is True
                and video.get("key")
            ):

                return (
                    "https://www.youtube.com/watch?v="
                    + video["key"]
                )

        # Fallback to any YouTube trailer
        for video in videos:

            if (
                video.get("site") == "YouTube"
                and video.get("type") == "Trailer"
                and video.get("key")
            ):

                return (
                    "https://www.youtube.com/watch?v="
                    + video["key"]
                )

        return None

    except Exception as e:

        print(
            f"Trailer request failed: {e}"
        )

        return None


# =========================================================
# FETCH MOVIE DETAILS
# =========================================================

@st.cache_data(ttl=3600)
def fetch_movie_details(movie_id):

    try:

        api_key = st.secrets["TMDB_API_KEY"]

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{movie_id}"
        )

        response = session.get(
            url,
            params={
                "api_key": api_key
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Poster
        poster_path = data.get(
            "poster_path"
        )

        if poster_path:

            poster = (
                "https://image.tmdb.org/t/p/w500"
                + poster_path
            )

        else:

            poster = None

        # Rating
        rating = data.get(
            "vote_average",
            0
        )

        # Release date
        release_date = data.get(
            "release_date",
            ""
        )

        if release_date:

            year = int(
                release_date[:4]
            )

        else:

            year = 0

        # Genres
        genres = data.get(
            "genres",
            []
        )

        genre_names = [
            genre["name"]
            for genre in genres
        ]

        genre_text = ", ".join(
            genre_names
        )

        if not genre_text:

            genre_text = "Unknown"

        # Overview
        overview = data.get(
            "overview",
            "No overview available."
        )

        # Trailer
        trailer = fetch_trailer(
            movie_id,
            api_key
        )

        return {
            "poster": poster,
            "rating": rating,
            "year": year,
            "genres": genre_text,
            "overview": overview,
            "trailer": trailer
        }

    except Exception as e:

        print(
            f"TMDB request failed: {e}"
        )

        return {
            "poster": None,
            "rating": 0,
            "year": 0,
            "genres": "Unknown",
            "overview":
                "Movie information unavailable.",
            "trailer": None
        }


# =========================================================
# RECOMMENDATION FUNCTION
# =========================================================

def recommend(movie_name):

    # Find selected movie index
    movie_index = movies[
        movies["title"] == movie_name
    ].index[0]

    # Get similarity scores
    distances = similarity[movie_index]

    # Sort according to similarity
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:

        movie_id = movies.iloc[
            i[0]
        ].movie_id

        movie_title = movies.iloc[
            i[0]
        ].title

        details = fetch_movie_details(
            movie_id
        )

        details["title"] = movie_title

        details["similarity"] = round(
            i[1] * 100,
            2
        )

        recommendations.append(
            details
        )

    return recommendations


# =========================================================
# GET GENRES
# =========================================================

@st.cache_data(ttl=3600)
def get_genres():

    genre_set = set()

    sample_movies = movies.head(100)

    for _, row in sample_movies.iterrows():

        details = fetch_movie_details(
            row["movie_id"]
        )

        if details["genres"] != "Unknown":

            genres = details[
                "genres"
            ].split(", ")

            for genre in genres:

                genre_set.add(
                    genre
                )

    return sorted(
        list(genre_set)
    )


# =========================================================
# GET TOP RATED MOVIES
# =========================================================

@st.cache_data(ttl=3600)
def get_top_rated_movies():

    movie_data = []

    sample_movies = movies.head(50)

    for _, row in sample_movies.iterrows():

        details = fetch_movie_details(
            row["movie_id"]
        )

        details["title"] = row["title"]

        movie_data.append(
            details
        )

    movie_data = sorted(
        movie_data,
        key=lambda x: x["rating"],
        reverse=True
    )

    return movie_data[:5]


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "# Project Filters"
)

st.sidebar.write(
    "Use the filters to narrow down the movies."
)

st.sidebar.divider()


# Search
search_text = st.sidebar.text_input(
    "Search movie",
    placeholder="Enter movie name"
)


# Rating
minimum_rating = st.sidebar.slider(
    "Minimum rating",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.5
)


# Year
year_filter = st.sidebar.slider(
    "Release year",
    min_value=1900,
    max_value=2026,
    value=(1900, 2026)
)


# Genre
try:

    available_genres = get_genres()

    selected_genre = st.sidebar.selectbox(
        "Genre",
        ["All Genres"] + available_genres
    )

except Exception:

    selected_genre = "All Genres"


# =========================================================
# MAIN HEADER
# =========================================================

st.title(
    "Movie Recommendation System"
)

st.markdown(
    '<div class="project-subtitle">'
    'A content-based movie recommendation system '
    'using similarity analysis and the TMDB API.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# MOVIE SEARCH
# =========================================================

st.markdown(
    '<div class="section-title">'
    'Select a Movie'
    '</div>',
    unsafe_allow_html=True
)


if search_text:

    filtered_movies = movies[
        movies["title"].str.contains(
            search_text,
            case=False,
            na=False
        )
    ]

else:

    filtered_movies = movies


if len(filtered_movies) > 0:

    selected_movie_name = st.selectbox(
        "Movie",
        filtered_movies["title"].values
    )

else:

    st.warning(
        "No movie found. Try a different search."
    )

    selected_movie_name = None


# =========================================================
# RECOMMEND BUTTON
# =========================================================

if st.button(
    "Recommend",
    use_container_width=True
):

    if selected_movie_name:

        with st.spinner(
            "Finding recommendations..."
        ):

            recommendations = recommend(
                selected_movie_name
            )


        # -------------------------------------------------
        # APPLY FILTERS
        # -------------------------------------------------

        filtered_recommendations = []

        for movie in recommendations:

            # Rating filter
            if movie["rating"] < minimum_rating:

                continue

            # Year filter
            if movie["year"] != 0:

                if not (
                    year_filter[0]
                    <= movie["year"]
                    <= year_filter[1]
                ):

                    continue

            # Genre filter
            if selected_genre != "All Genres":

                if selected_genre not in movie["genres"]:

                    continue

            filtered_recommendations.append(
                movie
            )


        # -------------------------------------------------
        # DISPLAY RECOMMENDATIONS
        # -------------------------------------------------

        if filtered_recommendations:

            st.markdown(
                '<div class="section-title">'
                'Recommended Movies'
                '</div>',
                unsafe_allow_html=True
            )

            columns = st.columns(
                len(filtered_recommendations)
            )

            for col, movie in zip(
                columns,
                filtered_recommendations
            ):

                with col:

                    # Poster
                    if movie["poster"]:

                        st.image(
                            movie["poster"],
                            use_container_width=True
                        )

                    else:

                        st.info(
                            "Poster unavailable"
                        )


                    # Movie title
                    st.markdown(
                        f'<div class="movie-title">'
                        f'{movie["title"]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                    # Rating
                    st.markdown(
                        f'<div class="movie-info">'
                        f'Rating: '
                        f'<b>{movie["rating"]:.1f}/10</b>'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                    # Year
                    if movie["year"]:

                        st.markdown(
                            f'<div class="movie-info">'
                            f'Release year: '
                            f'{movie["year"]}'
                            f'</div>',
                            unsafe_allow_html=True
                        )


                    # Genre
                    st.markdown(
                        f'<div class="movie-info">'
                        f'Genre: '
                        f'{movie["genres"]}'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                    # Similarity
                    st.markdown(
                        f'<div class="movie-info">'
                        f'<span class="similarity">'
                        f'Similarity: '
                        f'{movie["similarity"]:.1f}%'
                        f'</span>'
                        f'</div>',
                        unsafe_allow_html=True
                    )


                    # Trailer
                    if movie["trailer"]:

                        st.link_button(
                            "Watch Trailer",
                            movie["trailer"],
                            use_container_width=True
                        )

                    else:

                        st.caption(
                            "Trailer unavailable"
                        )


                    # Overview
                    with st.expander(
                        "Movie Overview"
                    ):

                        st.write(
                            movie["overview"]
                        )


        else:

            st.warning(
                "No recommendations match "
                "the selected filters."
            )


# =========================================================
# TOP RATED MOVIES
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">'
    'Top Rated Movies'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Highest-rated movies available in the dataset."
)


with st.spinner(
    "Loading movie information..."
):

    top_movies = get_top_rated_movies()


top_columns = st.columns(5)


for col, movie in zip(
    top_columns,
    top_movies
):

    with col:

        if movie["poster"]:

            st.image(
                movie["poster"],
                use_container_width=True
            )

        else:

            st.info(
                "Poster unavailable"
            )


        st.markdown(
            f'<div class="movie-title">'
            f'{movie["title"]}'
            f'</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            f'<div class="movie-info">'
            f'Rating: '
            f'<b>{movie["rating"]:.1f}/10</b>'
            f'</div>',
            unsafe_allow_html=True
        )


        if movie["year"]:

            st.markdown(
                f'<div class="movie-info">'
                f'Release year: '
                f'{movie["year"]}'
                f'</div>',
                unsafe_allow_html=True
            )


        if movie["trailer"]:

            st.link_button(
                "Watch Trailer",
                movie["trailer"],
                use_container_width=True
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        Movie Recommendation System |
        Content-Based Filtering |
        Python | Pandas | Streamlit | TMDB API
    </div>
    """,
    unsafe_allow_html=True
)