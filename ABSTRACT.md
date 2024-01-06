## Motivation

The **dacl10k: Benchmark for Semantic Bridge Damage Segmentation** is the first large-scale dataset for semantic bridge damage segmentation, comprising annotated images from real-world inspections. Civil engineering structures such as power plants, sewers, and bridges form essential components of the public infrastructure. It is mandatory to keep these structures in a safe and operational state. In order to ensure this, they are frequently inspected where the current recognition and documentation of defects and building components is mostly carried out manually. A failure of individual structures results in enormous costs. For example, the economic costs caused by the closure of a bridge due to congestion is many times the cost of the bridge itself and its maintenance. During its creation, the authors primary objective was to develop a dataset that enables the training of models which later support the inspector during damage recognition and documentation to a maximum. It includes images collected during concrete bridge inspections acquired from databases at authorities and engineering offices, thus, it represents real-world scenarios. Concrete bridges represent the most common building type, besides steel, steel composite, and wooden bridges.

## Dataset acquisition

Approximately one half of the images originate from databases of engineering offices, while the other half was provided by local authorities from Germany. The images were taken between 2000 and 2020. Both data sources supplied highly heterogeneous images regarding camera type, pose, lighting condition, and resolution.

The authors take the problem of semantic segmentation of bridge defects out of the niche by introducing dacl10k, the biggest real-world inspection dataset for multi-label semantic segmentation making it possible to perform damage classification, measurement and localization on a pixel-level. Thereby, they enable recognizing 13 frequently occurring defects on reinforced concrete bridges (e.g., Crack, Spalling, Efflorescence) and 6 important building parts (e.g., exposed reinforcement bar Exposed Rebar, Bearing, Expansion Joint, Protective Equipment). All these classes play an important role for determining the building’s structural integrity, traffic safety and durability. Dacl10k includes 9,920 images from more than 100 different bridges, specifically designed for practical use, as it comprises all visually unique damage types defined by bridge inspection standards.

<img src="https://github.com/dataset-ninja/dacl10k/assets/120389559/a2cffa6d-8a66-499c-8303-cad8f3ad6770" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example annotations from dacl10k. Top row: original image. Middle row: polygonal annotations. Bottom row: stacked masks. The following classes are abbreviated: Alligator Crack (ACrack), Washouts/Concrete corrosion (WConccor), Expansion Joint (EJoint), Protective Equipment (PEquipment) and Joint Tape (JTape). From left to right, the images display the individual classes: 1. Weathering, Spalling, Exposed Rebars, Rust; 2. Weathering, Crack; 3. Alligator Crack, Restformwork, Efflorescence; 4. Weathering, Crack, Spalling, Rockpocket; 5. Crack, Rust, Expansion Joint, Spalling; 6. Weathering, Rockpocket, Spalling, Efflorescence, Crack, Rust, Restformwork, Joint Tape; 7. Weathering, Protective Eq.</span>

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
