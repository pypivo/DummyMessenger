
build:
	docker compose -f docker_compose/two_app.yaml up --build

migrations:
	cd ./backend && alembic upgrade head

send:
	python3 ./client/send.py
