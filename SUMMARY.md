**dacl10k: Benchmark for Semantic Bridge Damage Segmentation** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the construction industry. 

The dataset consists of 9920 images with 62327 labeled objects belonging to 19 different classes including *rust*, *spalling*, *weathering*, and other: *crack*, *efflorescence*, *protective equipment*, *cavity*, *hollowareas*, *drainage*, *wetspot*, *graffiti*, *joint tape*, *exposed rebars*, *restformwork*, *bearing*, *expansion joint*, *alligator crack*, *rockpocket*, and *washouts/concrete corrosion*.

Images in the dacl10k dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 2081 (21% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *train* (6935 images), *test* (2010 images), and *val* (975 images). Additionally, each label in images has ***concrete defect***, ***general defect***, or ***object part*** tag. Also every image in ***test*** dataset has one of following tags: ***test dev*** or ***test challenge***. Explore it in supervisely labeling tool. The dataset was released in 2023 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">University of the Bundeswehr Munich, Germany</span>.

Here are the visualized examples for the classes:

[Dataset classes](https://github.com/dataset-ninja/dacl10k/raw/main/visualizations/classes_preview.webm)
