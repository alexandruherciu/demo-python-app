# Cointainerised Application for calculating factorial of a given non-negative integer
This containerised Python application uses Flask. It is a simple example for AWS ECS Demo.

## Infrastructure

AWS CDK (Python) used for Infrastructure as Code (Seperate repository)

* AWS ECR
* AWS ECS

IaC repository: https://github.com/omerkarabacak/multi-stack-aws-cdk-python-iac-project

## CICD

Github Actions used for auto building docker image and deploying it to AWS ECS