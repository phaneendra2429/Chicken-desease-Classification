from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} stareted <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<< \n\nX==============X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} stareted <<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<< \n\nX==============X")
except Exception as e:
    logger.exception(e)
    raise e
