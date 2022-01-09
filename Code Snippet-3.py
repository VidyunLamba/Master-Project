# The script supports python 3 and above 
# References from AWS Boto3 documentation - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
# It requires pip (repositories) to install boto3 to install boto3 libraries
# s3v4 - signature version supported by AWS

import datetime
import webbrowser
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner


def rsa_signer(message):
# Line 17 opens the private key file generated (replace the file name with other file name to resue the script
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())
#Key ID and URL generated in the CloudFront distribution
key_id = 'K1LQYGDSFR7UGV'
url = 'https://d3i0jfvyqwt1c5.cloudfront.net/vid.txt'
# mention the expiry date for the singed CloudFront URL
expire_date = datetime.datetime(2021, 12, 12)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Generate a signed URL that will be valid until the specific expiry date

signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
# Print the generate signed URL    
print(signed_url)
#Open webbrowser to open the URL
webbrowser.open(signed_url)