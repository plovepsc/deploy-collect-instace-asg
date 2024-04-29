

resource  "aws_ami_from_instance" "custom-create-image" {
    name               = "terraform-asg-${formatdate("YYYY-MM-DD-HH-mm-ss", timestamp())}"
    source_instance_id = "${var.instance_id}"
    snapshot_without_reboot = true
    
  tags = {
      Name = "terraform-asg-${formatdate("YYYY-MM-DD-HH-mm-ss", timestamp())}"
  }

}
output "ami_id" {
    value = aws_ami_from_instance.custom-create-image.id
    
  
}

