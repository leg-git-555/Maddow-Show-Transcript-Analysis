# # Adjusted FetchFilteredEpisodeURLs.py
# import requests
# from bs4 import BeautifulSoup

# # URL you provided
# base_url = "https://archive.org/details/tv?q=rachel+maddow+show&and[]=publicdate:[2021-01-06+TO+2024-11-06]&and[]=program:%22The+Rachel+Maddow+Show%22&sort=publicdate&page="

# def fetch_episode_urls():
#     all_episode_urls = []

#     # Increase the range of pages being fetched
#     # For now, we'll fetch the first 10 pages, adjust as necessary
#     for page_number in range(1, 15):  # fetching 10 pages
#         print(f"Fetching page {page_number}...")
#         url = base_url + str(page_number)
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"Failed to fetch page {page_number}")
#             continue
        
#         soup = BeautifulSoup(response.text, 'html.parser')
#         # Each episode link has a CSS class "stealth"
#         links = soup.select('div.item-ttl a')
        
#         for link in links:
#             href = link.get('href')
#             if href:
#                 full_url = "https://archive.org" + href
#                 all_episode_urls.append(full_url)

#     return all_episode_urls

# # Run the function
# episode_urls = fetch_episode_urls()

# # Print results
# print(f"✅ Found {len(episode_urls)} episode URLs.")
# for url in episode_urls:
#     print(url)

# # Optionally save to a text file
# with open("filtered_episode_urls.txt", "w") as f:
#     for url in episode_urls:
#         f.write(url + "\n")

import requests
from bs4 import BeautifulSoup

# URL you provided
base_url = "https://archive.org/details/tv?q=rachel+maddow+show&and[]=publicdate:[2021-01-06+TO+2024-11-06]&and[]=program:%22The+Rachel+Maddow+Show%22&sort=publicdate&page="

def fetch_episode_urls():
    all_episode_urls = []
    page_number = 1  # Start from the first page
    
    while True:
        print(f"Fetching page {page_number}...")
        url = base_url + str(page_number)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {page_number}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Each episode link has a CSS class "stealth"
        links = soup.select('div.item-ttl a')
        
        if not links:  # No links means we've hit the last page
            print("No more episodes found, ending pagination.")
            break
        
        for link in links:
            href = link.get('href')
            if href:
                full_url = "https://archive.org" + href
                all_episode_urls.append(full_url)

        # Check if next page exists
        page_number += 1

    return all_episode_urls

# Run the function
episode_urls = fetch_episode_urls()

# Print results
print(f"✅ Found {len(episode_urls)} episode URLs.")
for url in episode_urls:
    print(url)

# Optionally save to a text file
with open("filtered_episode_urls.txt", "w") as f:
    for url in episode_urls:
        f.write(url + "\n")


