# Read from the file file.txt and output the tenth line to stdout.

cat file.txt | sed -n 10,10p
