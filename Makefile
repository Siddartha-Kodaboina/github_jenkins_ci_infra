# Base Makefile for CI operations

.PHONY: init clean

# Default target
all: help

# Help target
help:
	@echo "Available targets:"
	@echo "  init    - Initialize workspace with application repository"
	@echo "  clean   - Clean the workspace"

# Initialize workspace
init:
	@echo "Initializing workspace for $(APP_NAME)"
	@echo "App repository: $(APP_REPO)"
	python3 scripts/workspace/init_workspace.py --app-repo $(APP_REPO) --app-name $(APP_NAME)

# Clean workspace
clean:
	@echo "Cleaning workspace"
	python3 scripts/workspace/clean_workspace.py