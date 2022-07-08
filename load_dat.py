import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('nyse.taq.prod.rawfiles')

def load(path):
    for obj in bucket.objects.filter(Prefix=path):
        print(obj.key)
       
    return None