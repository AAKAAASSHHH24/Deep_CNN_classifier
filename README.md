# DEEP Classifier package

## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

![img](https://raw.githubusercontent.com/AAKAAASSHHH24/Deep_CNN_classifier/master/docs/Data%20Ingestion%402x%20(1).png)

OUTER STRUCTURE

dvc.yaml is used for orchestration i.e. to connect several pipelines. It can act as a substitute for main.py used in ML project.

params.yaml keeps all the parameters related to the project like batch size, epochs etc.

config.yaml keeps the project structure


STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab
MLFLOW_TRACKING_URI=https://dagshub.com/AAKAAASSHHH24/Deep_CNN_classifier.mlflow \
MLFLOW_TRACKING_USERNAME=AAKAAASSHHH24 \
MLFLOW_TRACKING_PASSWORD=eace9117203f613afad0874c7cf8db27d285d1b3 \
python script.py

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model

DOCKER RUN COMMAND:
docker build -t prediction .