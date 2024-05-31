import requests

def save_page_now(url):
  save_url = "https://web.archive.org/save/"
  response =  requests.get(save_url + url)

  if response.status_code == 200:
    print(f"Successfully saved {url} to the Wayback Machine Archive")
  else:
    print(f"Failed to save {url}. Status code: {response.status_code}")

if __name__ == "__main__":
  #Replace with the URL you want to archive
  url= ""
  save_page_now(url)
