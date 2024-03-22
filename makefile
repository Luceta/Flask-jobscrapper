# Makefile

# 스크립트 폴더
SCRIPT_DIR := ./

# 스크립트 파일 이름
SCRIPT_NAME := run-dev.sh

# 스크립트 실행 명령
run:
	@$(SCRIPT_DIR)/$(SCRIPT_NAME)

# 실행 권한 설정
permissions:
	@chmod +x $(SCRIPT_DIR)/$(SCRIPT_NAME)

.PHONY: run permissions
