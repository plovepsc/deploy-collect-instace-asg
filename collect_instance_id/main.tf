


data "aws_instance" "running_instance_by_tag" {
  filter {
    name   = "tag:Name"
    values = ["terraform-asg"]  # Replace with the desired tag value
  }
}

output "running_instance_id" {
  value = data.aws_instance.running_instance_by_tag.id
}



