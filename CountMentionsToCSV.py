import os
import csv

# Folder containing transcript text files
transcript_folder = "maddow_transcripts"
output_csv = "mention_counts.csv"

# Prepare list to hold results
results = []

# Totals
total_trump = 0
total_biden = 0

# Loop through each text file
for filename in sorted(os.listdir(transcript_folder)):
    if filename.endswith(".txt"):
        filepath = os.path.join(transcript_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            trump_count = text.lower().count("trump")
            biden_count = text.lower().count("biden")
            results.append([filename, trump_count, biden_count])
            total_trump += trump_count
            total_biden += biden_count

# Write to CSV
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "trump_count", "biden_count"])
    writer.writerows(results)

    # Blank line, then labeled totals
    writer.writerow([])
    writer.writerow([f"Trump: {total_trump}", f"Biden: {total_biden}"])

print(f"✅ Done! Results written to {output_csv}")





# import os
# import csv
# import re

# # Folder with your transcript files
# transcripts_folder = "maddow_transcripts"

# # Output CSV file
# output_csv = "mention_counts.csv"

# # Prepare CSV file
# with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["filename", "date", "trump_count", "biden_count"])

#     # Loop through all transcript files
#     for filename in os.listdir(transcripts_folder):
#         if filename.endswith(".txt"):
#             filepath = os.path.join(transcripts_folder, filename)

#             try:
#                 with open(filepath, "r", encoding="utf-8") as file:
#                     text = file.read()

#                     # Count mentions (case-insensitive)
#                     trump_count = len(re.findall(r"\btrump\b", text, re.IGNORECASE))
#                     biden_count = len(re.findall(r"\bbiden\b", text, re.IGNORECASE))

#                     # Try to extract date from filename if possible
#                     date_match = re.search(r"\d{4}-\d{2}-\d{2}", filename)
#                     date_str = date_match.group(0) if date_match else ""

#                     # Write row to CSV
#                     writer.writerow([filename, date_str, trump_count, biden_count])

#             except Exception as e:
#                 print(f"⚠️ Error processing {filename}: {e}")

# print("✅ All transcript counts written to mention_counts.csv")
