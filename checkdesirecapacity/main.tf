data "aws_autoscaling_group" "existing_asg" {
  name = "terraform-asg"
# Specify the name of your existing ASG
}

output "desired_capacity" {
  value = data.aws_autoscaling_group.existing_asg.desired_capacity
}
  