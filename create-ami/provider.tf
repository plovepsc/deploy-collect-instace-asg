# terraform {
#   required_version = "~> 1.5.2"
#   required_providers {
#     aws = {
#         source = "hashicorp/aws"
#         version = "~> 3.0"
#     }
#     null = {
#       source = "hashicorp/null"
#       version = "~> 3.0.0"
#     }
#   }
# }

provider "aws" {
  access_key = "${var.AWS_ACCESS_KEY}"
  secret_key = "${var.AWS_SECRET_KEY}"
  region     = "${var.AWS_REGION}"
}

