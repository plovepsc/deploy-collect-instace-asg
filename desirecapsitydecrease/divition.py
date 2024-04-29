import sys

def multiply_value(value, multiplier):
    return int(value) / int(multiplier)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 multiply.py <input_value>")
        sys.exit(1)

    input_value = sys.argv[1]
    multiplier = 2  # Specify the multiplier here (e.g., 2)

    result = multiply_value(input_value, multiplier)

    # Write the result to the output file
    with open("/home/ubuntu/saddam/deploy-bus/replace-instance-asg/terraform.tfvars", "w") as file:
        file.write("desire_capasity = "+  str(result))
