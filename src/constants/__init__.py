import os
from datetime import datetime
DATABASE_NAME="Proj1"
COLLECTION_NAME="Proj1-Data"
MONGODB_URL="mongodb+srv://goelshivansh61_db_user:wZTjkcDp06eL0SvQ@cluster0.sakaauo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME="MyPipeline"
ARTIFACT_DIR="artifact"

DATA_INGESTION_DIR_NAME="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR="feature_store"
DATA_INGESTION_INGESTED_DIR="ingested"
DATA_INGESTION_TRAIN_TEST_RATIO=0.25


FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


DATA_VALIDATION_DIR_NAME="data_validation"
DATA_VALIDATION_FILE_NAME="report.yaml"
SCHEMA_FILE_PATH=os.path.join("config","schema.yaml")



DATA_TRANSFORMATION_DIR_NAME="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR="transformed"
DATA_TRANSFORMATION_TRANFORMED_OBJECT_DIR="transformed_object"

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"



MODEL_TRAINER_DIR_NAME="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR="trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME="model.pkl"
MODEL_TRAINER_METRICS_FILE="metric.yaml"
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS=200
MODEL_TRAINER_MIN_SAMPLE_SPLIT=7
MODEL_TRAINER_MIN_SAMPLE_LEAF=6
MIN_SAMPLE_SPLIT_MAX_DEPTH=10
MIN_SAMPLE_SPLIT_CRITERION="entropy"
