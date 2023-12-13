#!/bin/bash

# Specify the directory where your .zip files are located
dataset_directory="./datasets"

# Check if the directory exists
if [ ! -d "$dataset_directory" ]; then
    echo "Error: Dataset directory not found."
    exit 1
fi

# Change to the dataset directory
cd "$dataset_directory" || exit 1

# Iterate through each .zip file and extract its contents
for file in *.zip; do
    # Check if the file is a .zip file
    if [ -f "$file" ]; then
        # Extract the contents to the current directory
        unzip -q "$file"
        echo "Successfully extracted $file"
    else
        echo "Ignoring non-zip file: $file"
    fi
done
