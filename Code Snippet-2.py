import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import webbrowser

# The script supports python 3 and above 
# References from AWS Boto3 documentation - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
# It requires pip (repositories) to install boto3 to install boto3 libraries
# s3v4 - signature version supported by AWS
# Creating headers for API request call
# Access KEY ID and Secret Access Key is used for the apisuer created using IAM services
# Define AWS region and timeperiod for the URL validity
# To resue the script, replace the access key ID, secret acccess key and default region as configured in AWS cloud
AWS_ACCESS_KEY_ID = 'XXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXX'
AWS_DEFAULT_REGION = 'us-east-1'

def create_presigned_url(bucket_name, bucket_key, expiration, signature_version):

    s3_client = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             config=Config(signature_version=signature_version),
                             region_name=AWS_DEFAULT_REGION
                             )
    
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': bucket_key},
                                                    ExpiresIn=expiration)
 # Print the generate signed URL      
        print(response)
        #Open webbrowser to open the URL
        webbrowser.open(response)
   
    except:
        return none
 # Generates pre-signed URL with the bucket name, object name, URL validity, singature version      
generated_signed_url = create_presigned_url('XXX bucket name', 'XXX filename', 3600, 's3v4')        
