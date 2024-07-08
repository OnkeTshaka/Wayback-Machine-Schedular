import requests
import schedule
import time

def save_page_now(url):
  save_url = "https://web.archive.org/save/"
  response =  requests.get(save_url + url)

  if response.status_code == 200:
    print(f"Successfully saved {url} to the Wayback Machine Archive")
  else:
    print(f"Failed to save {url}. Status code: {response.status_code}")

def job():
  #Replace with the URL you want to archive
  url="https://kworb.net/spotify/artist/3SozjO3Lat463tQICI9LcE_songs.html"
  save_page_now(url)

  schedule.every().day.at("19:10").do(job)

  print("Scheduler started.Press Ctrl+C to stop")
  try:
    while True:
      schedule.run_pending()
      time.sleep(1)
  except:
    print("Scheduler stopped")





