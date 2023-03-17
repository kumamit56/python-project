import boto3 

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

c = 0
for bucket in s3.buckets.all():
    print(bucket.name)
    c = c+1
    
s3.Bucket("triponcall.com").download_file("Self introduction.txt","Self introduction.txt")
