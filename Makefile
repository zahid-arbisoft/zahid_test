.PHONY: dev.up dev.createsuperuser

dev.up:
	docker compose -f local.yml up

dev.migrate:
	docker compose -f local.yml run --rm django python manage.py migrate

dev.createsuperuse:
	docker compose -f local.yml run --rm django python manage.py createsuperuser
