#!/bin/bash
# Path to the text file listing the python files
FILE_LIST="generate-docs-for.txt"

# Read the file line by line
while IFS= read -r file || [[ -n "$file" ]]; do
    # Check if file exists to avoid errors
    if [[ -f "$file" ]]; then
        echo "Generating docs for: $file"
        pycco "$file"
    else
        echo "File not found: $file"
    fi
done < "$FILE_LIST"

# Trnasfer docs to central root

SOURCE_DIR="./docs"
DESTINATION_DIR="../../docs/python/graphs"

# Remove existing docs
rm -rf "$DESTINATION_DIR"

# Move the source folder into the destination directory
mv "$SOURCE_DIR" "$DESTINATION_DIR/"

echo "Folder moved from $SOURCE_DIR to $DESTINATION_DIR"
