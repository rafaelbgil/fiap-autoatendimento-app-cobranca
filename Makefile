test:
	coverage run --source=./  ./manage.py test
	coverage html
test-xml:
	coverage run --source=./  ./manage.py test
	coverage xml
run:
	python manage.py runserver 0.0.0.0:8091


