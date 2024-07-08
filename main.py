import requests

def save_songs_now(url):
  save_url = "https://web.archive.org/save/"
  response =  requests.get(save_url + url)

  if response.status_code == 200:
    print(f"Successfully saved {url} to the Wayback Machine Archive")
  else:
    print(f"Failed to save {url}. Status code: {response.status_code}")

def save_albums_now(url_albums):
  save_url = "https://web.archive.org/save/"
  response =  requests.get(save_url + url_albums)

  if response.status_code == 200:
    print(f"Successfully saved {url_albums} to the Wayback Machine Archive")
  else:
    print(f"Failed to save {url_albums}. Status code: {response.status_code}")

def save_chart_now(url_chart):
  save_url = "https://web.archive.org/save/"
  response =  requests.get(save_url + url_chart)

  if response.status_code == 200:
    print(f"Successfully saved {url_chart} to the Wayback Machine Archive")
  else:
    print(f"Failed to save {url_chart}. Status code: {response.status_code}")


if __name__ == "__main__":
  #Replace with the URL you want to archive
  url= "https://kworb.net/spotify/artist/3SozjO3Lat463tQICI9LcE_songs.html"
  url_albums ="https://kworb.net/spotify/artist/3SozjO3Lat463tQICI9LcE_albums.html"
  url_chart="https://kworb.net/itunes/artist/tyla.html"

  save_songs_now(url)
  save_albums_now(url_albums)
  save_chart_now(url_chart)
