import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    #возвращает среднюю оценку по каталогу, округленную до одного знака
    total = 0

    for movie in movies:
        total += movie["rating"]
    
    avg_r = total / len(movies)

    return round(avg_r, 1)


def catalog_age_stats(movies, current_year=2026):
    #возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее)
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    old = max(ages)
    new = min(ages)

    avg_age = sum(ages) / len(ages)

    return old, new, math.ceil(avg_age)


def duration_in_hours(minutes):
    #переводит минуты в формат "ч м"
    hours = minutes // 60
    minutes_rem = minutes % 60

    return f"{hours}ч {minutes_rem}м"


def rating_tier(rating):
    #возвращает по оценке категорию
    rating = rating if rating >= 0 else 0

    if rating >= 9:
        category = "шедевр"
    elif rating >= 7:
        category = "хорошо"
    elif rating >= 5:
        category = "средне"
    else:
        category = "слабо"

    return category


def decade_label(year):
    #возвращает категорию по году
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"


def print_non_comedy_movies(movies):
    #выводит названия всех не комедий
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    #возвращает первый по порядку в списке фильм с рейтингом выше 9.0
    index = 0

    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    #считает количество фильмов длиннее threshold минут
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


def normalize_title(title: str) -> str:
    #приводит строку к формату Title Case
    words = title.split()
    result = []

    for word in words:
        result.append(word[0].upper() + word[1:])

    return " ".join(result)


def make_slug(title):
    #превращает нормализованное название в «слаг»

    title = title.lower()
    title = title.replace(" ", "-")

    return title


def format_report_line(movie: dict) -> str:
    #возвращает единую строку с описанием фильма

    title = normalize_title(movie["title"])
    genres = sorted(movie["genres"])
    genres = ", ".join(genres)
    length = duration_in_hours(movie["duration_min"])

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {length}, жанры: {genres}'
    )


def titles_sorted_by_rating(movies):
    # возвращает список названий фильмов, отсортированных по убыванию рейтинга
    top_movies_title = []

    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    for movie in sorted_movies:
        top_movies_title.append(movie["title"])

    return top_movies_title


def top_n_by_rating(movies, n=3):
    #возвращает топ по рейтингу
    top_movies_rating = []

    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)    

    for movie in sorted_movies[:n]:
        top_movies_rating.append((movie["title"], movie["rating"]))

    return top_movies_rating


def count_by_genre(movies):
    #возвращает словарь {жанр: количество фильмов}

    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def actor_filmography(movies):
    #возвращает словарь {актер: [список названий фильмов]}
    filmography = {}

    for movie in movies:
        title = movie["title"]
        actors = movie["actors"]

        for actor in actors:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(title)

    return filmography


def above_average_ratings(movies):
    #возвращает словарь {title: rating} только для фильмов с рейтингом выше среднего
    average = average_rating(movies)

    above_average_ratings = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

    return above_average_ratings

def all_genres(movies):
    #множество всех уникальных жанров каталога
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    #множество актеров, снимавшихся в обоих фильмах
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    #жанры в movies_a, но не встречающиеся в movies_b
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    #отдает фильмы с рейтингом не ниже min_rating
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above_seven(movies):
    #суммарная длительность всех фильмов с рейтингом выше 7
    total_time = 0

    for movie in movies:
        if movie["rating"] > 7:
            total_time = total_time + movie["duration_min"]
            
    return total_time


def build_report(movies):
    average = average_rating(movies)
    age_stats = catalog_age_stats(movies)

    top_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    top_movies = top_movies[:3]

    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    genres = sorted(all_genres(movies))

    print("ОТЧЁТ ПО КАТАЛОГУ") #в задании ОТЧеТ, выглядит как опечатка 
    print(f"Средний рейтинг: {average}")
    print(f"Средний возраст фильмов: {age_stats[2]} лет", end="\n\n")
    
    print("Топ-3 фильма:")
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()

    print(f"Все жанры каталога: {', '.join(genres)}")

if __name__ == "__main__":
    build_report(movies)