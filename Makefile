build:
	docker build -t netreport:latest .

run:
	docker run -p 3000:3000 netreport:latest