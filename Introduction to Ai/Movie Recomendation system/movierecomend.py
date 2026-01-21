import pandas as pd
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.matrix.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore, Style

init(autocorrect=True)

df = pd.read_csv("imdb_top_1000.csv")
df["text"] = df["Genre"].fillna("") + " " + df['Overview'].fillna("")

tifidf = TfidVectorizer(stop_words="english")
matrix = tifidf.fit_transform(df["text"])
similarity = cosine_similarity(matrix)

genres = sorted({g.strip()for x in df["Genre"].dropma() for g in x.split(",")})


def recomented(genre, mood, rating, limit=5):
    data = df[df["Genre"].str.contains(genre, case=False, na=False)]

    if rating:
        data = data[data["IMDB_Rating"] >= rating]

    mood_score =  TextBlob(mood).sentiment.polarity
    result = []

    for _, row  in data.sample(frac=1).iterrows():
        if pd.isna(row["Overview"]):
            continue

        polarity = TextBlob(row["Overview"]).sentiment.polarity
        if mood_score >= 0 or  polarity >= 0:
            result.append((row["Series_Title"], polarity))

        if len(results) == limit:
            break

    return result


def main():
    print(Fore.BLUE + Style.BRIGHT + "\n Movie Recomendaton system\n")

    name = input(Fore.CYAN + "Enter your name: " + Fore.WHITE).strip()

    print(Fore.YELLOW + "\nAvailable Genres: ")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.WHITE}{i}. {Fore.GREEN}{g}")
        