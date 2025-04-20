set -o errexit

pip install -r employe/requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate 