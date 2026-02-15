#!/bin/bash

# 1. defining the directories
INPUT_DIR="input"
OUTPUT_DIR="output"

# 2. looping through every file in the input folder
for file in "$INPUT_DIR"/*; do
	# getting the filename without the path and extension
	filename=$(basename "$file")
	filename_no_extension="${filename%.*}"

	echo "Processing: $filename"
	echo "$filename_no_extension"
	# 3. the ffmpeg command
	# -c:v (video codec)
	# -c:a (audio codec)
	ffmpeg -hwaccel cuda -i "$file" \
		-c:v dnxhd -profile:v dnxhr_lb \
		-pix_fmt yuv422p \
		-c:a pcm_s16le \
		"$OUTPUT_DIR/${filename_no_extension}.mov" -y

done

echo "---------------------------------"
echo "all videos have been converted to $OUTPUT_DIR"
