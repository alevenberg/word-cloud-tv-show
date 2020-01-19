# Usage: ./run.sh tv-show-name

if [ $# -eq 0 ]; then
    echo "No arguments provided, usage: ./run.sh tv-show-name"
    exit 1
fi

mkdir -p $1
python3 scraper.py $1 
python3 clean_data.py $1
python3 word_cloud.py $1