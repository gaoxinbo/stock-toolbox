#!/usr/bin/env python

import boto3
import datetime
import os

bucket="gaoxinbo-db-backup"
prefix="stock"

cmd="mysqldump -uroot -p840326 stock > /tmp/backup.sql"

if __name__ == '__main__':
  s3 = boto3.resource('s3')
  today = datetime.date.today().strftime("%Y%m%d")

    

  os.system(cmd)

  
  path=os.path.join(prefix, today, "backup.sql")
  s3.Object(bucket, path).put(Body=open('/tmp/backup.sql', 'rb'))