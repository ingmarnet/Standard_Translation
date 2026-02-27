import csv
import sys

# Increase CSV field size limit in case there are huge fields
csv.field_size_limit(sys.maxsize)

translated_file = 'app/code/Standard/Translation/i18n/es_AR.csv'
untranslated_file = 'app/code/Standard/Translation/i18n/es_AR_nissei_com.csv'
output_file = 'app/code/Standard/Translation/i18n/es_AR_missing.csv'

try:
    translated_keys = set()
    with open(translated_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                translated_keys.add(row[0])
    print(f"Loaded {len(translated_keys)} keys from {translated_file}")

    missing_rows = []
    with open(untranslated_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] not in translated_keys:
                missing_rows.append(row)
    print(f"Found {len(missing_rows)} missing translations")

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(missing_rows)

    print(f"Saved to {output_file}")
except Exception as e:
    print(f"Error: {e}")
