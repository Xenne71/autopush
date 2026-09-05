import subprocess
from datetime import datetime

# 1. Ask the user for a commit message
user_input = input(
    "Describe your changes (press Enter for default): "
).strip()

# 2. Check if the user typed anything; if not, use a default fallback
if user_input:
    commit_message = user_input
else:
    # A timestamped default like: "Auto-commit: 2026-09-05 17:25"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_message = f"Auto-commit: {timestamp}"

print(f"Using commit message: \"{commit_message}\"\n")

# 3. Define the Git commands
commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", commit_message],
    ["git", "push"],
]

# 4. Execute the sequence
try:
    for cmd in commands:
        print(f"Running: {' '.join(cmd)}...")
        subprocess.run(cmd, check=True, capture_output=True, text=True)

    print("\nSuccess! All changes staged, committed, and pushed!")

except subprocess.CalledProcessError as err:
    print(f"\nFailed while running: {' '.join(err.cmd)}")
    print("Git output:")
    print(err.stderr or err.stdout)