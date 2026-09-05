import subprocess

# A temporary commit message for testing the chain
commit_message = "initial commit from python script"

commands = [
    ["git", "add", "."],
    ["git", "commit", "-m", commit_message],
    ["git", "push"],
]

try:
    for cmd in commands:
        print(f"running: {' '.join(cmd)}...")
        # check=True halts execution immediately if any command returns an error
        subprocess.run(cmd, check=True, capture_output=True, text=True)

    print("\nSuccess! All changes staged, committed, and pushed!")

except subprocess.CalledProcessError as err:
    print(f"\nFailed while running: {' '.join(err.cmd)}")
    print("Git output:")
    # Print the error details captured from Git
    print(err.stderr or err.stdout)