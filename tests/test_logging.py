import os
from logger_config.logger_config import setup_logger

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_path = os.path.join(BASE_DIR, "logs", "game.log")
print("Log path:", log_path)

# Use a unique logger name to avoid re-use conflicts
logger_name = "test_game_logger"
game_logger = setup_logger(logger_name, log_path, to_console=True)

print("Handlers:", game_logger.handlers)

# Log a test message
test_message = "LOGGING GUCCI"
game_logger.info(test_message)

# Flush all handlers
for handler in game_logger.handlers:
    handler.flush()

# Read last line of the file
try:
    with open(log_path, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        last_line = lines[-1] if lines else ""
except FileNotFoundError:
    print("Log file not found.")
    last_line = ""
except Exception as e:
    print(f"Exception while reading the log file: {e}")
    last_line = ""

assert test_message in last_line, f"Test log message not found. Last line: {last_line}"
print("Logger test passed.")
