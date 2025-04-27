import requests
from bs4 import BeautifulSoup

# URL of the episode you want to scrape
url = "https://archive.org/details/MSNBCW_20241112_090000_The_Rachel_Maddow_Show"  # Example URL

# Send a GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all divs with class 'snipin nosel'
transcript_divs = soup.find_all('div', class_='snipin nosel')

# Check if we found any transcript divs
if transcript_divs:
    transcript_text = ""
    for div in transcript_divs:
        transcript_text += div.get_text(separator="\n")  # Add text and separate with line breaks
    
    # Save the transcript to a text file
    with open('maddow_transcript.txt', 'w', encoding='utf-8') as f:
        f.write(transcript_text)
    
    print("Transcript saved to 'maddow_transcript.txt'")
else:
    print("No transcript found on this page.")


