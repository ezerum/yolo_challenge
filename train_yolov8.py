from ultralytics import YOLO
import os


def main():
 
        model = YOLO(
            "trained/yerba_v1.pt"
        )  

        model.train(
            data=os.path.join(
                os.getcwd(),
                "dataset/Yerba_taragui",
                "data.yaml",
            ),  
            cfg="cfgs/cfg_yolov8.yaml",
            project="Producto",  
            name="Yerba_Taragui", 
        )


if __name__ == "__main__":
    main()
