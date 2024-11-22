set -o errexit

pip insall -r requirements.txt

python manae.py collectstatic --no-input
python manage.py migrate