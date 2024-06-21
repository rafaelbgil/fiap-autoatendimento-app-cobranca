MONGODB_SERVER ?= 192.168.0.100
MERCADOPAGO_TOKEN ?= sasa
MERCADOPAGO_EMAIL ?= rafa@ddsadsa.com
URL_DOMINIO ?= http://127.0.0.1:8091
PEDIDO_API_URL ?= http://127.0.0.1:8090
DJANGO_KEY ?= dsadsa
RABBIT_SERVER ?= 192.168.0.110

export MONGODB_SERVER
export MERCADOPAGO_TOKEN
export MERCADOPAGO_EMAIL URL_DOMINIO PEDIDO_API_URL DJANGO_KEY RABBIT_SERVER
all:
	@echo $(MONGODB_SERVER)
test:
	coverage run --source=./  ./manage.py test
	coverage html
test-xml:
	coverage run --source=./  ./manage.py test
	coverage xml
run:
	python manage.py runserver 0.0.0.0:8091



