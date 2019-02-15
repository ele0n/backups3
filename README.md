# backups3
A backup Tool for S3
## Design Idea
This tool can upload und download files from and to a s3 bucket.
And test if there is already an backup or it should generate a new one
## Init
You should add an S3Bucket that should be used for the backup
then you should get the api keys and write them into the credentials.py
If you want versioning you should enable that in the s3
If you want an periodic execution i would recoment to do this by adding the execution ot this python script to a cron job.
## Run
To run it execute backup.py
The option -h gives you help on the input parameters
The option -d changes from upload to download mode
There is also the path parameter giving the path of the folder / file that should be backed up.
