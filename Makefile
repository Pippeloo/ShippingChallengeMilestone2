# Start the docker-compose stack for production
# Usage: make start
start:
	docker-compose -f docker-compose.yml up -d

# Start the docker-compose stack for development
# Usage: make start-dev
start-dev:
	docker-compose -f docker-compose.dev.yml up -d

# Stop the docker-compose stack
# Usage: make stop
stop:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.dev.yml down

# Restart the docker-compose stack
# Usage: make restart
restart: stop start

# Restart the docker-compose stack for development
# Usage: make restart-dev
restart-dev: stop start-dev

# Build the docker-compose stack
# Usage: make build
build:
	docker-compose -f docker-compose.yml build

# Build the docker-compose stack for development
# Usage: make build-dev
build-dev:
	docker-compose -f docker-compose.dev.yml build
