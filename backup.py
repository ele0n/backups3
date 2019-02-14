#!/usr/bin/python3

"""
:Author Daniel Klamtd
:Licence MIT
"""


import argparse
import os
import sys
import string
from hashlib import sha256

import credentials
import boto3 as aws

def hash(path):
        engine = sha256()
        engine.update(path.encode('UTF8'))
        return engine.hexdigest()

def get_files(path):
        a = []
        for i in os.walk(path):
                for j in i[2]:
                        a.append('/' + str(i[0]) + '/' + str(j))
        return a

def main():
        parser = argparse.ArgumentParser(prog="Backup S3")
        parser.add_argument('path', type=str, 
                help='file path')
        parser.add_argument('-d', action='store_true',
                help='Download mode, default Upload mode')

        args = parser.parse_args()

        session = aws.setup_default_session(
                aws_access_key_id = credentials.AWS_ACCESS_KEY_ID,
                aws_secret_access_key = credentials.AWS_SECRET_ACCESS_KEY,
                aws_session_token = credentials.AWS_SESSION_TOKEN
        )

        s3 = aws.resource('s3')
        bucket = s3.Bucket(credentials.BACK3SUP_BUCKET)

        if args.d:
                exists = False
                for i in bucket.objects.all():
                        if i.key.startswith(str(hash(args.path))):
                                exists = True
                                to = os.path.normpath('/'.join(os.path.abspath(args.path).split('/')[0:-1]) + i.key[64:])
                                try:
                                        if not os.path.exists(os.path.dirname(to)):
                                                os.makedirs(os.path.dirname(to))
                                        backup.download_file(i.key, to)

                                except Exception as e:
                                        print(e)

                if not exists:
                        print("No such file in the CLOUD")
                                

        else:
                for f in get_files(args.path):
                        try:
                                bucket.upload_file(os.path.normpath('/'.join(os.path.abspath(args.path).split('/')[0:-1]) + f), str(hash(args.path)) + os.path.normpath(f))
                        except Exception as e:
                                print(e)



if __name__=="__main__":
        main()