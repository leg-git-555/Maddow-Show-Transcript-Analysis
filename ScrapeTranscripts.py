import os
import requests
from bs4 import BeautifulSoup
import time
import re
from datetime import datetime

# Folder to save transcripts
save_folder = "maddow_transcripts"
os.makedirs(save_folder, exist_ok=True)

# Read episode URLs from the text file
with open("filtered_episode_urls.txt", "r") as f:
    episode_urls = [line.strip() for line in f if line.strip()]

print(f"Found {len(episode_urls)} episode URLs.")

# Loop over each URL
for idx, url in enumerate(episode_urls, start=1):
    print(f"\n({idx}/{len(episode_urls)}) Fetching: {url}")
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ Failed to fetch page: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Grab the tvbanner text (this includes the air date)
        banner = soup.find("h1", id="tvbanner")
        if not banner:
            print("⚠️ No tvbanner found.")
            continue

        banner_text = banner.get_text(strip=True)

        # Extract date using regex (e.g. "January 8, 2021")
        date_match = re.search(r'([A-Za-z]+ \d{1,2}, \d{4})', banner_text)
        if not date_match:
            print("⚠️ Date not found in tvbanner.")
            continue

        raw_date = date_match.group(1)
        date_obj = datetime.strptime(raw_date, "%B %d, %Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")

        # Find all transcript chunks
        transcript_divs = soup.find_all("div", class_="snipin nosel")

        if not transcript_divs:
            print("⚠️ No transcript found.")
            continue

        # Combine all the transcript text
        transcript_text = "\n".join(div.get_text(strip=True) for div in transcript_divs)

        # Create a filename like 2021-01-08_Rachel_Maddow_Show.txt
        filename = os.path.join(save_folder, f"{formatted_date}_Rachel_Maddow_Show.txt")

        # Save the transcript
        with open(filename, "w", encoding="utf-8") as file:
            file.write(transcript_text)

        print(f"✅ Saved transcript to {filename}")

    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")

    # Pause a little between requests to be nice to the server
    time.sleep(1)

print("\n🎉 Done scraping transcripts!")






# OLD VERSION THAT DIDN'T NAME FILES CORRECTLY (NO DATE IN FILE NAME)
# import os
# import requests
# from bs4 import BeautifulSoup
# import time
# from urllib.parse import urlparse

# # Folder to save transcripts
# save_folder = "maddow_transcripts"
# os.makedirs(save_folder, exist_ok=True)

# # Read episode URLs from the text file
# with open("filtered_episode_urls.txt", "r") as f:
#     episode_urls = [line.strip() for line in f if line.strip()]

# print(f"Found {len(episode_urls)} episode URLs.")

# # Loop over each URL
# for idx, url in enumerate(episode_urls, start=1):
#     print(f"\n({idx}/{len(episode_urls)}) Fetching: {url}")
    
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             print(f"❌ Failed to fetch page: {response.status_code}")
#             continue

#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find all transcript chunks
#         transcript_divs = soup.find_all("div", class_="snipin nosel")

#         if not transcript_divs:
#             print("⚠️ No transcript found.")
#             continue

#         # Combine all the transcript text
#         transcript_text = "\n".join(div.get_text(strip=True) for div in transcript_divs)

#         # Extract the episode ID cleanly
#         parsed_url = urlparse(url)
#         episode_id = parsed_url.path.split("/")[-1]

#         # Try to extract date from episode ID
#         parts = episode_id.split('_')
#         if len(parts) > 1 and parts[1].isdigit() and len(parts[1]) == 8:
#             date_raw = parts[1]  # Example: '20220107'
#             date_formatted = f"{date_raw[:4]}-{date_raw[4:6]}-{date_raw[6:]}"  # '2022-01-07'
#             filename = os.path.join(save_folder, f"{date_formatted}_The_Rachel_Maddow_Show.txt")
#         else:
#             filename = os.path.join(save_folder, f"{episode_id}.txt")

#         # Save the transcript
#         with open(filename, "w", encoding="utf-8") as file:
#             file.write(transcript_text)

#         print(f"✅ Saved transcript to {filename}")

#     except Exception as e:
#         print(f"⚠️ Error fetching {url}: {e}")

#     # Pause a little between requests to be nice to the server
#     time.sleep(1)

# print("\n🎉 Done scraping transcripts!")

# fin

