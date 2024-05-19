test:
	coverage run --source=./  ./manage.py test
	coverage html

run:
	python manage.py runserver 0.0.0.0:8091


