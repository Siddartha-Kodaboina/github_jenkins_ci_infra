# Base Makefile for CI operations

.PHONY: init clean

init:
	@echo "Initializing workspace for $(APP_NAME)"
	python3 scripts/workspace/init_workspace.py --app-repo $(APP_REPO) --app-name $(APP_NAME)

clean:
	@echo "Cleaning workspace"
	python3 scripts/workspace/clean_workspace.py