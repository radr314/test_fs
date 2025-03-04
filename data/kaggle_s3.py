import boto3
import logging
import os
s3=boto3.client('s3')

class upload_s3:
    def __init__(self):
        self.s3=boto3.client('s3')
        self.logger=logging.getLogger(__name__)
        self.dir_val=-2
        
    def upload_file(self, file_name, bucket):
        #if filter(lambda x:x.get('Name') == file_name, self.s3.list_buckets()['Buckets']):
        # logging.info('bucket already exists')
        self.recrusive_dir_upload(file_name, bucket)
            

    def recrusive_dir_upload(self,directory_name, bucket):
        for i in os.listdir(directory_name):
            if os.path.isdir(f'{directory_name}/{i}'):
                self.dir_val=self.dir_val-1
                self.recrusive_dir_upload(f'{directory_name}/{i}',bucket)
                self.dir_val=self.dir_val+1
            else:
                self.s3.upload_file(f'{directory_name}/{i}',
                                bucket,
                                '/'.join(f'{directory_name}/{i}'.split('/')[self.dir_val:]))
                


    # def kaggle_s3(self):
        