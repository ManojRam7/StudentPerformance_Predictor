from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def run_pipeline(self) -> float:
        ingestion = DataIngestion()
        train_data_path, test_data_path = ingestion.initiate_data_ingestion()

        transformation = DataTransformation()
        train_arr, test_arr, _ = transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        trainer = ModelTrainer()
        score = trainer.initiate_model_trainer(train_arr, test_arr)
        return score


if __name__ == "__main__":
    pipeline = TrainPipeline()
    print(f"Model training completed. R2 score: {pipeline.run_pipeline():.4f}")
