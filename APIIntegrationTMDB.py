import urllib.parse
import requests

url1 = "https://api.themoviedb.org/3/search/movie?api_key=dbaf48597cf03626e4349585c7d1fca5&language=en-US&query="
url2 = "&page=1&include_adult=false"

while True:

    movie = input("Movie: ")
    if movie == "quit" or movie == "q":
        break

    url = url1 + movie + url2

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["total_results"]

    if json_status > 0:
        print("API Status (number of results): " + str(json_status) + " = A successful call.\n")
        for mov in json_data["results"]:
            print("=============================================")
            print("Movie title: " + str(json_data[mov]["title"]))
            print("Overview: " + str(json_data[mov]["overview"]))
            print("Release date: " + str(json_data[mov]["release_date"]))
            print("Vote average: " + str(json_data[mov]["vote_average"]))
            print("=============================================")