setup:
	@docker-compose up -d

run:
	@uvicorn api.main:app --reload

tear_down:
	@docker-compose down

test:
	@pytest