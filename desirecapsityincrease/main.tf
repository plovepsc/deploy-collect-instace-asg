# main.tf

# Define a null_resource to execute local commands
resource "null_resource" "remove_file" {
  
  # Use a local-exec provisioner to run a command
  provisioner "local-exec" {
    # Command to remove the file
    command = "rm -f /home/ubuntu/saddam/deploy-bus/desirecapsityincrease/terraform.tfstate"
  }
  
  # Trigger the provisioner when Terraform apply is executed
  triggers = {
    always_run = "${timestamp()}"
  }
}
# Data source to read the content of the input file
data "local_file" "input_file" {
  filename = "/home/ubuntu/saddam/deploy-bus/checkdesirecapacity/input_file.txt"
}

# Provisioner to execute a local script after resource creation
resource "null_resource" "process_file" {
  # Use triggers to re-run this provisioner only when input_file.txt changes
  triggers = {
    input_file_checksum = data.local_file.input_file.content
  }

  # Execute a local script to process the input file
  provisioner "local-exec" {
    command = "python3 ${path.module}/multiply.py ${data.local_file.input_file.content}"
  }
}
