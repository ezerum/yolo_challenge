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
            ),  # Merged_Dataset/Augmented_Dataset - "Gestion_de_filas_4_camaras_v1i_yolov8",
            cfg="cfgs/cfg_y8s.yaml",
            project="Producto",  # Gestion_fila_Yolov8m_4_cam - Gestion_fila_Yolov8n_4_cam -CF_Pilar_tracking_Yolov8m_11_cam
            name="Yerba_Taragui",  # Yolov8m_ - Yolov8n_
        )


if __name__ == "__main__":
    main()
