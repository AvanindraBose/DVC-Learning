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

AWS Steps:
