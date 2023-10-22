.PHONY: dev.up dev.createsuperuser dev.shell.celery

dev.up:
	docker compose -f local.yml up

dev.migrate:
	docker compose -f local.yml run --rm django python manage.py migrate

dev.createsuperuse:
	docker compose -f local.yml run --rm django python manage.py createsuperuser

dev.shell.celery:
	docker-compose -f local.yml exec celeryworker bash

dev.shell.django:
	docker-compose -f local.yml  run --rm django bash
