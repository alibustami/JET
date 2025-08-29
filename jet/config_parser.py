from enum import Enum
from typing import Union

import yaml
from pydantic import BaseModel, ConfigDict, computed_field


class ModelVersion(Enum):
    v8 = "v8"
    # v9 = "v9"
    # v10 = "v10"
    # v11 = "v11"
    # v12 = "v12"


class ModelSize(Enum):
    NANO = "n"
    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"


class ModelTask(Enum):
    DETECTION = "detection"
    SEGMENTATION = "segmentation"
    # POSE_DETECTION = "pose_detection"
    # OOB = "oob"
    # CLASSIFICATION = "classification"


MODEL_TASK_SHORT_NAME = {
    "detection": "",
    "segmentation": "seg",
}


class Config(BaseModel):
    model_config = ConfigDict(extra="forbid")

    yolo_version: ModelVersion
    model_size: ModelSize
    model_task: ModelTask
    experiment_name: str | None = None
    dataset_path: str

    @computed_field
    @property
    def ultralytics_model_same(self) -> str:
        task_value = self.model_task.value
        short_task = MODEL_TASK_SHORT_NAME.get(task_value, task_value)
        return f"yolo{self.yolo_version.value}{self.model_size.value}{'-' if short_task else ''}{short_task}.pt"


class ExperimentConfig:
    @classmethod
    def from_yaml(cls, yaml_path):
        with open(yaml_path, "r") as file:
            data = yaml.safe_load(file)

            experiment = data["experiment"]
            return Config(**experiment)

    @classmethod
    def direct(
        cls,
        yolo_version: int,
        model_size: str,
        model_task: str,
        experiment_name: str | None,
        dataset_path: str,
    ):
        return Config(
            yolo_version=yolo_version,
            model_size=model_size,
            model_task=model_task,
            experiment_name=experiment_name,
            dataset_path=dataset_path,
        )
