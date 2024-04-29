
import subprocess
import time


def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for few seconds...")
    time.sleep(delay_seconds)
    print("Executing the command now.")
    
    try:
        # Execute the command using subprocess
        result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:")
        print(result1.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print("Error output:")
        print(e.output)

# Example usage:
command_to_run = "cd /home/ubuntu/saddam/deploy-bus/collect_instance_id && python3 script.py"  # Replace this with your desired command
delay_seconds = 3  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)




def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for few seconds...")
    time.sleep(delay_seconds)
    print("Executing the command now.")
    
    try:
        # Execute the command using subprocess
        result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:")
        print(result1.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print("Error output:")
        print(e.output)

# Example usage:
command_to_run = "cd /home/ubuntu/saddam/deploy-bus/create-ami && python3 script.py"  # Replace this with your desired command
delay_seconds = 3  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)


def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for few seconds...")
    time.sleep(delay_seconds)
    print("Executing the command now.")
    
    try:
        # Execute the command using subprocess
        result1 = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command executed successfully.")
        print("Output:")
        print(result1.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
        print("Error output:")
        print(e.output)

# Example usage:
command_to_run = "cd /home/ubuntu/saddam/deploy-bus/template && terraform apply  -auto-approve"  # Replace this with your desired command
delay_seconds = 3  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)

def run_command(command):
    # Execute the command using subprocess
    subprocess.run(command, shell=True)

# List of commands to execute sequentially
commands = [
    "cd /home/ubuntu/saddam/deploy-bus/checkdesirecapacity && python3 script1.py",
    "cd /home/ubuntu/saddam/deploy-bus/checkdesirecapacity && python3 script2.py"
]

# Loop through the list of commands and execute them sequentially
for command in commands:
    print(f"Executing command: {command}")
    run_command(command)

    # Introduce a delay (sleep) after each command except the last one
    if command != commands[-1]:
        delay_seconds = 60  # Adjust the delay duration as needed (5 seconds in this example)
        print(f"Sleeping for {delay_seconds} seconds before the next command...")
        time.sleep(delay_seconds)

print("All commands have been executed.")
