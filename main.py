from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} stareted <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<< \n\nX==============X")
except Exception as e:
    logger.exception(e)
    raise e