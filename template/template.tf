resource "aws_launch_template" "example" {
  name = "terraform-temp"
  description   = "terraform-temp"
  block_device_mappings {
    device_name = "/dev/sda1"

    # Example EBS volume configuration
    ebs {
      volume_size = 8
      volume_type = "gp2"
    }
  }
  

  # Specify the instance type, AMI, and other instance settings
  instance_type          = "t2.micro"
  image_id               = "${var.customs_ami}"
  key_name               = "terraform"
   update_default_version = true
  #security_group_names   = ["sg-0adc401d582d5c246"]

  
  # Network interfaces configuration
  network_interfaces {
    associate_public_ip_address = true
    subnet_id                   = "subnet-0f4c1defbfc3bb126"
    security_groups             = ["sg-0adc401d582d5c246"]
  }

  # Tags for the Launch Template
  tag_specifications {
    resource_type = "instance"
    tags = {
      Name        = "terraform-temp"
      project = "shohoz"
    }
  }
}



