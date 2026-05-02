This Repository will help Avanindra to learn more about DVC from practical as well as theoritical aspects.

# Without Pipeline : 

In general usage (without pipelines), when we run dvc add, DVC creates a .dvc file (e.g., data.csv.dvc) which is tracked by Git. This file stores metadata such as the hash of the data and its location in the DVC cache.

data.csv → data.csv.dvc

# With Pipeline :

However, when working with pipelines (dvc.yaml), DVC automatically tracks outputs defined in each stage using the outs field. In this case, we do not need to manually run dvc add for those outputs.

Instead of creating individual .dvc files for each output, DVC stores the metadata of all pipeline stages in a centralized file called dvc.lock. This file contains hashes of dependencies, outputs, and parameters for each stage, ensuring reproducibility.

Therefore:

.dvc files → used for standalone data tracking
dvc.lock → used for pipeline tracking
dvc.yaml → dvc.lock (centralized metadata)
Both serve similar purposes but are used in different contexts.

# AWS Steps:

Steps Required to Set up an AWS S3 Bucket at Remote location for dvc usecase:

Step1: Create S3 Bucket

Step2: Create IAM user -> with allow dvc policy.
Note: Allow dvc policy is just the name of the custom policy that we created.

Script: 

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::twitter-sentiment-dvc-store"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::twitter-sentiment-dvc-store/*"
        }
    ]
}
Just change the bucket address based on usecases.

Step3: pip install dvc[s3]

Step4: pip install awscli
-> Dependency COnflict Often Happens Here because of botocore. Hence use uv to resolve dependency conflicts

Step5: aws configure
-> Access key and secret key will be asked in this step. PLease store it somewhere.

Step6: dvc remote add -d <"name of dvc remote stores"> remotestore <"adress of the bucket"> s3://<"bucket_name">

Step7: git commit

Step8: dvc push

Step9: git push
