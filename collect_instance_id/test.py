import boto3
from botocore.exceptions import ClientError
import subprocess
import datetime
import os

def send_email(sender_email, recipient_emails, subject, body, body_html=None):
    # Create a new SES client
    ses_client = boto3.client('ses', region_name='us-east-1')

    # Construct the message
    message = {
        'Subject': {'Data': subject},
        'Body': {
            'Text': {'Data': body},
        }
    }

    # Construct the destination with multiple recipients
    destination = {
        'ToAddresses': recipient_emails,
    }

    # Try to send the email
    try:
        # Provide the contents of the email
        response = ses_client.send_email(
            Source=sender_email,
            Destination=destination,
            Message=message
        )
        print("Email sent! Message ID:", response['MessageId'])

    except ClientError as e:
        print("Error sending email:", e.response['Error']['Message'])
        
        
def execute_terraform_apply():
    try:
        # Execute Terraform apply command and capture output
        result = subprocess.run(['python3', 'finalscript.py'], capture_output=True, text=True, check=True)
        return result.stdout, None  # Return stdout if command succeeds
    except subprocess.CalledProcessError as e:
        return None, e.stderr  # Return stderr if command fails with non-zero exit code
    except Exception as e:
        return None, f"An unexpected error occurred: {str(e)}"

def log_to_file(log_content):
    log_filename = f"terraform_apply_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    with open(log_filename, 'w') as log_file:
        log_file.write(log_content)
    print(f"Log file created: {log_filename}")
    
def main():
    sender_email = ''
    recipient_emails = ['']
    try:
        # Execute Terraform apply command and capture output
        stdout, stderr = execute_terraform_apply()

        if stderr:
            # Command failed, send email notification
            subject = 'Terraform Apply Failed'
            body = f"The Terraform apply command failed:\n\n{stderr}"
            #send_email(subject, body, sender_email, recipients)
            send_email(sender_email, recipient_emails, subject, body)
        else:
            # Command succeeded, send success email notification
            subject = 'Terraform Apply Succeeded'
            body = 'The Terraform apply command executed successfully.'
    
            send_email(sender_email, recipient_emails, subject, body)

        # Log the result (stdout or stderr) into a log file
        log_content = f"Command Output:\n\n{stdout if stdout else stderr}"
        log_to_file(log_content)

    except Exception as e:
        # Log unexpected errors
        log_content = f"An unexpected error occurred: {str(e)}"
        log_to_file(log_content)

if __name__ == "__main__":
    main()

    # # Example usage
    # sender_email = 'from'
    # recipient_emails = ['revicver']
    # subject = 'Test Email via AWS SES'
    # body_text = 'This is a test email sent via AWS SES.'
    # body_html = '<p>This is a test email sent via <strong>AWS SES</strong>.</p>'

    # send_email(sender_email, recipient_emails, subject, body_text, body_html)


