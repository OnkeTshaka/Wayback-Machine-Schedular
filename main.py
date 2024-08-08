
import requests

def save_to_wayback(url):
    save_url = "https://web.archive.org/save/"
    
    while True:
        response = requests.get(save_url + url)
        
        if response.status_code == 200:
            print(f"Successfully saved {url} to the Wayback Machine Archive")
            break
        else:
            print(f"Failed to save {url}. Status code: {response.status_code}. Retrying...")

if __name__ == "__main__":
    # Replace with the URLs you want to archive
    urls = [
        "https://kworb.net/spotify/artist/3SozjO3Lat463tQICI9LcE_songs.html",
        "https://kworb.net/spotify/artist/3SozjO3Lat463tQICI9LcE_albums.html",
        "https://kworb.net/itunes/artist/tyla.html"
    ]

    for url in urls:
        save_to_wayback(url)


'''This code will continuously attempt to save the URL to the Wayback Machine until it receives a status code of 200, indicating a successful save.'''