setup:
	@docker-compose up -d --build

run:
	@uvicorn api.main:app --reload

tear_down:
	@docker-compose down

test:
	@pytest