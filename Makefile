# run pysnake
.PHONY: pysnake
pysnake:
	docker-compose -f ./docker-compose.yml run pysnake python pysnake.py

# run pynake with dev environment
.PHONY: pysnake-dev
pysnake-dev:
	docker-compose -f ./docker-compose.yml -f ./docker-compose.dev.yml run pysnake python pysnake.py
