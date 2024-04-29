
import subprocess
import os
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
result = subprocess.run(["terraform", "output", "ami_id"], capture_output=True, text=True)

# Extract the output value from the result
output_value = result.stdout.strip()

# Write the output value to a text file
with open("/home/ubuntu/saddam/deploy-bus/template/terraform.tfvars", "w") as file:
        file.write("customs_ami = "+ str(output_value))

        print(f"Output value '{output_value}' captured to outputfile")
        


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file '{file_path}': {e}")

# Specify the path of the file you want to delete
file_to_delete = "/home/ubuntu/saddam/deploy-bus/create-ami/terraform.tfstate"

# Call the delete_file function with the specified file path
delete_file(file_to_delete)

