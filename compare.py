import csv

translated_file = 'app/code/Standard/Translation/i18n/es_AR.csv'
untranslated_file = 'app/code/Standard/Translation/i18n/es_AR_nissei_com.csv'
output_file = 'app/code/Standard/Translation/i18n/es_AR_missing.csv'

# Set to store keys that are already translated
translated_keys = set()

# Read the translated file
with open(translated_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:  # ensure row is not empty
            translated_keys.add(row[0])

# List to store missing translation rows
missing_rows = []

# Read the untranslated file
with open(untranslated_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # If the row is not empty and its key is not in the translated keys set
        if row and row[0] not in translated_keys:
            missing_rows.append(row)

# Write the missing rows to the new file
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(missing_rows)

print(f"Extracted {len(missing_rows)} missing translations to {output_file}")
