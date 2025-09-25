import requests
import json
favorites = []
API_KEY = "1f453bf1"

def get_movie_name():
    name = input("Enter movie name: ")
    return name

def search_movie():
    movie_name = get_movie_name()
    url = f"http://www.omdbapi.com/?s={movie_name}&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("RAW json data:")
        print(data)

        if "Search" in data and len(data["Search"]) > 0:
            for movie in data["Search"]:
                print("------")
                print(f"Title : {movie.get('Title', 'N/A')}")
                print(f"Year  : {movie.get('Year', 'N/A')}")
                print(f"Type  : {movie.get('Type', 'N/A')}")
                print(f"IMDB ID: {movie.get('imdbID', 'N/A')}")
            choice = input("Enter the IMDB ID of the movie to add to favorites (or press Enter to skip): ")
            
            if choice:
                found = False
                for movie in data["Search"]:
                    if movie.get("imdbID") == choice:
                        favorites.append(movie)
                        found = True
                        print(f"{movie.get('Title')}added to favorites.")
                        break
                if not found:
                        print("IMDB ID not found in search results.")
        else:
            print("Movie not found.")
    else:
        print("Error in request.")

search_movie()        

def save_fav():
    with open("favorites.json", "w") as f:
        json.dump(favorites, f)

def show_favorite():
    if not favorites:
        print("there is no movie in favorite list")
    for movie in favorites:
        print("______")
        print("Title:", movie["Title"])
        print("Year:", movie["Year"])

def remove_favorite():
    
    if not favorites:
        print("there is no movie in favorite list")
        return
    
    for index, movie in enumerate(favorites, start=1):
        print(f"{index}. {movie['Title']} ({movie['Year']})")
    
    choice =input("enter your number ofthe movie you want to remove: ")
    index = int(choice) - 1

    if 0 <= index < len(favorites):
        removed = favorites.pop(index)
        print(f"the {removed['Title']} removed")
    
        with open("favorites.json", "w") as f:
            json.dump(favorites, f, indent=2) 
    else:
        print("invalid number") 

def load_and_show_favorites():
    try:
        with open("favorites.json", "r") as f:
            saved_list = json.load(f)    
            if not saved_list:
                print("there is nothing here")
                return
            favorites.clear()
            favorites.extend(saved_list)
            print("Favorites loaded successfully.")
    except FileNotFoundError:
        print("favorites.json file not found.")
        return
    for index, movie in enumerate(saved_list, 1):
        print(f"{index}. {movie['Title']} ({movie['Year']})")

def main_menu():
    while True:
        print ("\n ________MENU_________")
        print("1. Search and add movie")
        print("2. Show favorite list")
        print("3. Remove a movie")
        print("4. Save favorites to file")
        print("5. Load favorites from file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            search_movie()
        elif choice == "2":
            show_favorite()
        elif choice == "3":
            remove_favorite()
        elif choice == "4":
            save_fav()
        elif choice == "5":
            load_and_show_favorites()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")        


main_menu()