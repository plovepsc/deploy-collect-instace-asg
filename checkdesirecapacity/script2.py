
import subprocess
import time
def run_terraform_command(command_args):
    try:
        # Execute the terraform command with provided arguments
        result1 = subprocess.run(["terraform"] + command_args, capture_output=True, text=True)
        
        # Check the result
        if result1.returncode == 0:
            print("Terraform command executed successfully.")
            print(result1.stdout)
        else:
            print("Terraform command failed.")
            print(result1.stderr)
    
    except FileNotFoundError:
        print("Terraform binary not found. Make sure Terraform is installed and in PATH.")

# Example usage: Run 'terraform apply'
command_arguments = ["apply", "-auto-approve"]
run_terraform_command(command_arguments)

# Run terraform output command and capture the result
result = subprocess.run(["terraform", "output", "desired_capacity"], capture_output=True, text=True)

# Extract the output value from the result
output_value = result.stdout.strip()

# Write the output value to a text file
with open("input_file.txt", "w") as file:
        file.write(output_value)

        print(f"Output value '{output_value}' captured to outputfile")
        
        
        


        
# devision capacity

def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for {delay_seconds} seconds...")
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
command_to_run = "cd /home/ubuntu/saddam/deploy-bus/desirecapsitydecrease && python3 runcommand1.py"  # Replace this with your desired command
delay_seconds = 5  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)



# final desire capacity run

def run_command_with_delay(command, delay_seconds):
    print(f"Waiting for {delay_seconds} seconds...")
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
command_to_run = "cd /home/ubuntu/saddam/deploy-bus/replace-instance-asg && python3 runcommand.py"  # Replace this with your desired command
delay_seconds = 5  # 2 minutes (2 minutes = 120 seconds)

run_command_with_delay(command_to_run, delay_seconds)

