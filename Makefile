setup:
	@docker-compose up

run:
	@uvicorn api.main:app --reload

tear_down:
	@docker-compose down

test:
	@pytest