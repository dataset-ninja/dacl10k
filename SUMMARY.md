**dacl10k: Benchmark for Semantic Bridge Damage Segmentation** is a dataset for a semantic segmentation task. It is used in the construction industry. 

The dataset consists of 9920 images with 62327 labeled objects belonging to 19 different classes including *rust*, *spalling*, *weathering*, and other: *crack*, *efflorescence*, *protective equipment*, *cavity*, *hollowareas*, *drainage*, *wetspot*, *graffiti*, *joint tape*, *exposed rebars*, *restformwork*, *bearing*, *expansion joint*, *alligator crack*, *rockpocket*, and *washouts/concrete corrosion*.

Images in the dacl10k dataset have pixel-level semantic segmentation annotations. There are 2081 (21% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *train* (6935 images), *test* (2010 images), and *val* (975 images). Every object class can be labeled with ***damage class*** tag: ***weathering***, ***rust***,***cavity***,***efflorescence***,***alligator crack***,***spalling***,***graffiti***,***restformwork***,***wetspot***,***exposed rebars***, ***hollowareas***, ***crack***, ***rockpocket*** classes, or ***object class*** tag: ***bearing***, ***expansion joint***, ***drainage***, ***protective equipment***, ***joint tape***, ***washouts/concrete corrosion*** classes. Every image in test dataset has one of following tags: ***test dev*** or ***test challenge***. The dataset was released in 2023 by the University of the Bundeswehr Munich, Germany.

Here are the visualized examples for the classes:

[Dataset classes](https://github.com/dataset-ninja/dacl10k/raw/main/visualizations/classes_preview.webm)
