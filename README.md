<!-- This Repository will help Avanindra to learn more about DVC from practical as well as theoritical aspects.

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

Step9: git push -->

# DVC Interview + Practical Learning Summary

This repository helps Avanindra learn DVC from both:

* Practical implementation perspective
* Interview preparation perspective

This document covers:

1. What DVC is
2. Why Git alone is not enough
3. Internal DVC files/folders
4. Without pipeline workflow
5. Pipeline workflow
6. `dvc.yaml`
7. `dvc.lock`
8. `.dvc` files vs `dvc.lock`
9. How DVC detects changes
10. Common DVC commands
11. Reproducibility workflow
12. DVC experiment tracking limitations
13. DVC vs MLflow
14. AWS S3 integration
15. CI/CD practical tips

---

# 1) What is DVC?

DVC (Data Version Control) is Git for machine learning artifacts.

It helps version:

* datasets
* models
* intermediate outputs
* ML pipelines

Git is good for:

* code
* configs
* documentation

Git is not good for:

* huge datasets
* trained models
* binary files

DVC solves this by:

* storing metadata in Git
* storing actual heavy files in cache/remote storage

---

# 2) Why Git alone is not enough

Suppose dataset is 10GB.

If we push every version to Git:

* repo becomes huge
* cloning becomes slow
* Git performance degrades

DVC solves this by separating:

Code → Git
Data → DVC remote/cache

---

# 3) DVC Internal Files/Folders

After:

```bash
dvc init
```

DVC creates:

```text
.dvc/
```

Inside:

---

## `.dvc/config`

Stores remote configuration.

Example:

* S3 bucket
* DagsHub remote

---

## `.dvc/cache`

Most important folder.

Stores actual contents of files.

Not just metadata.

Example:

```text
.dvc/cache/files/
.dvc/cache/runs/
```

---

### `files/`

Stores actual dataset/model content using hash-based storage.

Example:

```text
.dvc/cache/files/md5/
```

---

### `runs/`

Stores experiment/pipeline execution cache.

Used during:

* `dvc repro`
* `dvc exp run`

---

## `.dvc/tmp`

Temporary folder.

Stores:

* lock files
* state files
* temporary execution metadata

Safe to regenerate.

---

# 4) Without Pipeline Workflow

When tracking standalone datasets:

```bash
dvc add data.csv
```

Creates:

```text
data.csv.dvc
```

This file stores metadata:

* file hash
* file path
* cache reference

Actual file content goes to:

```text
.dvc/cache
```

Then:

```bash
dvc push
```

Uploads cache to remote.

Then:

```bash
git add data.csv.dvc
git commit
git push
```

---

## Summary

Standalone file → `.dvc file`

---

# 5) Pipeline Workflow

Suppose pipeline:

```text
raw → preprocess → train → evaluate
```

Outputs are defined in:

```text
dvc.yaml
```

Example:

* processed dataset
* trained model
* metrics

These outputs are automatically tracked.

We DO NOT manually run:

```bash
dvc add model.pkl
```

for pipeline outputs.

Because:

```text
outs:
```

handles this automatically.

---

# 6) `dvc.yaml`

This is pipeline blueprint.

Stores:

* stages
* commands
* dependencies
* outputs
* params
* metrics

Example:

```text
preprocess → train → evaluate
```

Created using:

```bash
dvc stage add
```

---

# 7) `dvc.lock`

This is centralized metadata file for pipeline runs.

Stores:

* dependency hashes
* output hashes
* parameter values

Created/updated during:

```bash
dvc repro
```

This acts like pipeline snapshot.

---

# 8) `.dvc` file vs `dvc.lock`

This is a very common interview question.

---

## `.dvc file`

Used for standalone tracked files.

Example:

```text
data.csv → data.csv.dvc
```

---

## `dvc.lock`

Used for pipeline outputs.

Tracks metadata of all stages centrally.

---

## Easy memory trick

Standalone artifact → `.dvc`

Pipeline artifact → `dvc.lock`

---

# 9) How DVC Detects Changes

Very common interview question.

When we run:

```bash
dvc repro
```

DVC:

1. Reads `dvc.yaml`
2. Reads `dvc.lock`
3. Recomputes hashes of:

* dependencies
* outputs
* params

4. Compares hashes

If hash changes:

Stage reruns.

Only downstream affected stages rerun.

---

# 10) Most Important DVC Commands

## Initialize

```bash
dvc init
```

---

## Track standalone data

```bash
dvc add
```

---

## Create pipeline stage

```bash
dvc stage add
```

---

## Run pipeline

```bash
dvc repro
```

Most important command.

---

## Push artifacts

```bash
dvc push
```

---

## Pull artifacts

```bash
dvc pull
```

---

## Restore files

```bash
dvc checkout
```

---

## Track experiments

```bash
dvc exp run
```

---

## Compare experiments

```bash
dvc exp show
```

---

## Visualize DAG

```bash
dvc dag
```

---

## Sync manual changes

```bash
dvc commit
```

---

# 11) Correct Workflow Order

Very common interview question.

Correct order:

```bash
dvc repro
dvc push
git add .
git commit
git push
```

Why?

Because teammates should be able to pull artifacts after Git pull.

---

# 12) Reproducibility Workflow

Example:

Team worked for 6 months.

Best dataset was created months ago.

How to restore?

Step 1:

```bash
git checkout old_commit
```

Restores:

* old code
* old metadata

Step 2:

```bash
dvc pull
```

Downloads exact historical artifacts.

Step 3:

```bash
dvc repro
```

Recreates exact pipeline outputs.

---

# 13) DVC Experiment Tracking Limitations

DVC supports:

```bash
dvc exp run
dvc exp show
```

But limitations:

* CLI heavy
* weaker visualization
* no strong model registry
* weaker deployment integration
* difficult at large scale

---

# 14) Why We Use MLflow Along With DVC

DVC is better for:

* dataset versioning
* pipeline reproducibility
* dataset lineage

MLflow is better for:

* experiment tracking
* visualization
* model registry
* deployment lifecycle

Real-world architecture:

```text
DVC → data versioning
MLflow → experiment tracking
FastAPI → serving
AWS/DagsHub → infrastructure
```

---

# 15) AWS S3 Integration

Step 1:
Create S3 bucket

---

Step 2:
Create IAM user

---

Step 3:
Create custom IAM policy

Allow:

* ListBucket
* PutObject
* GetObject

Script: 

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

Link of the Article (Outdated) : https://ritza.co/articles/dvc-s3-set-up-s3-as-dvc-remote/

---

Step 4:

```bash
pip install dvc[s3]
```

---

Step 5:

```bash
pip install awscli
```

Use `uv` if dependency conflicts happen.

---

Step 6:

```bash
aws configure
```

---

Step 7:

```bash
dvc remote add -d remotestore s3://bucket-name
```

---

Step 8:

```bash
dvc push
```

---

Step 9:

```bash
git push
```

---

# 16) CI/CD Practical Tips

Very important for interviews.

Typical CI flow:

```text
Developer pushes code
      ↓
GitHub Actions triggers
      ↓
dvc pull
      ↓
dvc repro
      ↓
pytest
      ↓
dvc push
```

---

Always remember:

Git stores metadata.

DVC stores actual artifacts.

---

# Final Interview Summary

DVC guarantees reproducibility by:

* versioning datasets
* tracking pipeline outputs
* storing metadata in Git
* storing artifacts in remote storage

This allows teams to restore exact datasets/models even months later.
