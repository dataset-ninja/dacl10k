## Motivation

Civil engineering structures such as power plants, sewers, and bridges form essential components of the public infrastructure. It is mandatory to keep these structures in a safe and operational state. In order to ensure this, they are frequently inspected where the current recognition and documentation of defects and building components is mostly carried out manually. A failure of individual structures results in enormous costs. For example, the economic costs caused by the closure of a bridge due to congestion is many times the cost of the bridge itself and its maintenance. The **dacl10k: Benchmark for Semantic Bridge Damage Segmentation** is the first large-scale dataset for semantic bridge damage segmentation, comprising annotated images from real-world inspections. During its creation, the authors primary objective was to develop a dataset that enables the training of models which later support the inspector during damage recognition and documentation to a maximum. It includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges.

## Dataset Structure

├── annotations
│ ├── train (n=6.935)
│ └── validation (n=975)
└── images
├── train (n=6.935)
├── validation (n=975)
├── testdev (n=1.012)
└── testchallenge (n=998)

## Dataset description

Dataset distinguishes _13 bridge defects_ classes and _6 bridge components_ classes (_damage class_ and _object class_ tags respectively), that play a key role in the building assessment. Every image in test dataset has one of following tags: _test dev_ or _test challenge_. Dataset comprises coarse pixel-level annotations. The authors border each defect and object on a given image with one polygon (shape), assign its label and include polygons of the same class that overlap with each other in one shape because it is not important to differentiate between instances of a given class. Instead, their size and localization on a class-basis is important.
