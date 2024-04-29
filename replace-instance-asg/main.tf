resource "aws_autoscaling_group" "example" {
  name = "terraform-asg"
  desired_capacity     = "${var.desire_capasity}"
  max_size             = 2
  min_size             = 1
  health_check_type    = "ELB"
  health_check_grace_period = 300


  launch_template {
    id = "lt-05b246b4c8e686eef"
    version = "$Latest"
  }

  vpc_zone_identifier = ["subnet-0f4c1defbfc3bb126, subnet-070a55873c1155282"]  # Specify your subnet IDs
  termination_policies = [
    "OldestInstance"
  ]
 

  tag {
    key                 = "Name"
    value               = "terraform-asg"
    propagate_at_launch = true
  }
}
