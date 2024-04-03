# Challenge Go2future
_Se armo un dataset de imágenes sintéticas a partir de un modelo 3D (archivo .glb), el cual fue cargado utilizando la herramienta Blender v4.1. En esta herramienta se realizo la modificacion del background y se aplico rotaciones. Luego se cargaron estas imágenes en roboflow para realizar las anotaciones de forma automatica y crear la base de datos._ 
## Detalles del dataset
_ Total de Imágenes: 386_
_ Dataset Split: Trainn set, 355 imágenes; valid set, 31 imágenes y test set, 0 imágenes._
_ Resize: 640 x 640_
_Augmentations: Flip: Horizontal, Vertical; 90° Rotate: Clockwise, Counter-Clockwise; Crop: 0% Minimum Zoom, 30% Maximum Zoom; Rotation: Between -15° and +15°_
_Una vez configurado el dataset, roboflow te permite descargarlo en varios formatos que son entendidos por modelos de pre-entranamiento. En este caso se descargo el dataset en formato yolov8 de ultralytics_

_Nota: Aunque se utilizaron este número de imágenes para el entrenamiento del modelo, cabe destacar que son muy pocas imágenes para que el modelo YOLO se puede entrenar eficientemente. Por lo que, necesitarian por lo menos un número minimo de 1500 imágenes aproximadamnete para el entrenamiento._  

![YOLOv9 Benchmark](Producto/Yerba_Taragui5/results.png)
