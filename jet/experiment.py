from pathlib import Path

from logdir import LogDir
from ultralytics import YOLO

from jet.config_parser import ExperimentConfig


class Experiment:
    def __init__(self, config_file_path: Path):
        self.config_file_path = config_file_path
        configs = ExperimentConfig.from_yaml(self.config_file_path)
        self.ultralytics_model_same = configs.ultralytics_model_same
        print(self.ultralytics_model_same)
        self.dataset_path = configs.dataset_path
        self.experiment_name = (
            configs.experiment_name
            if configs.experiment_name
            else self.ultralytics_model_same.split(".")[0]
        )
        # self.logdir = LogDir(name=self.experiment_name, rootdir=Path("./experiments"))
        self.models_dir = Path("./models")

    def run(self):
        self.model = YOLO(Path(self.models_dir) / self.ultralytics_model_same)
        self.model.export(format="onnx")
        self.model.export(format="engine")


if __name__ == "__main__":
    exp = Experiment(Path("config.yaml"))
    exp.run()
