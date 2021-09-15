start:
	docker-compose up -d --build nginx

stop:
	docker-compose down

test:
	docker-compose up --build unit_test


