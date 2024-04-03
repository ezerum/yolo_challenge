# Challenge Go2future
_Se armo un dataset de imágenes sintéticas a partir de un modelo 3D (archivo .glb), el cual fue cargado utilizando la herramienta Blender v4.1. En esta herramienta se realizo la modificacion del background y se aplico rotaciones. Luego se cargaron estas imágenes en roboflow para realizar las anotaciones de forma automatica y crear la base de datos._ 
## Detalles del dataset
_ Total de Imágenes: 386_
_ Dataset Split: Trainn set, 355 imágenes; valid set, 31 imágenes y test set, 0 imágenes._
_ Resize: 640 x 640_
_Augmentations: Flip: Horizontal, Vertical; 90° Rotate: Clockwise, Counter-Clockwise; Crop: 0% Minimum Zoom, 30% Maximum Zoom; Rotation: Between -15° and +15°_

![YOLOv9 Benchmark](Producto/Yerba_Taragui5/results.png)

Especificar cuál sería, a tu criterio, la cantidad de imágenes adecuada para un correcto entrenamiento.

Te compartimos el modelo 3D del producto yerba taragui 500g.

Tendrás que anotar estas imágenes sintéticas con fondo random armando por ejemplo un dataset en formato que entienda Yolo. Podés probar con la nueva versión de Yolo (v9) o usar la v8.**
![YOLOv9 Benchmark](Producto/Yerba_Taragui5/results.png)
