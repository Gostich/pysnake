# run pysnake
.PHONY: pysnake
pysnake:
	docker-compose -f ./docker-compose.yml build  # workaround to have correct build.target
	docker-compose -f ./docker-compose.yml run pysnake python pysnake.py

# run pysnake with dev environment
.PHONY: pysnake-dev
pysnake-dev:
	#docker-compose -f ./docker-compose.yml -f ./docker-compose.dev.yml build  # workaround to have correct build.target
	docker-compose -f ./docker-compose.yml -f ./docker-compose.dev.yml run pysnake python pysnake.py
