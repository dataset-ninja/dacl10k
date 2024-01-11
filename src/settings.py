from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################s
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "dacl10k"
PROJECT_NAME_FULL: str = "dacl10k: Benchmark for Semantic Bridge Damage Segmentation"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_4_0(
    source_url="https://github.com/phiyodr/dacl10k-toolkit?tab=readme-ov-file#arrow_right-data"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Construction()]
CATEGORY: Category = Category.Construction()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2023-11-21"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://dacl.ai/workshop.html"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 12455283
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/dacl10k"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "The Development dataset": "https://dacl10k.s3.eu-central-1.amazonaws.com/dacl10k-challenge/dacl10k_v2_devphase.zip",
    "The Tesfinal dataset": "https://dacl10k.s3.eu-central-1.amazonaws.com/dacl10k-challenge/dacl10k_v2_testchallenge.zip",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "crack": [255, 192, 203],
    "alligator crack": [178, 223, 138],
    "efflorescence": [0, 0, 255],
    "rockpocket": [253, 191, 111],
    "washouts/concrete corrosion": [0, 0, 139],
    "hollowareas": [246, 124, 104],
    "spalling": [123, 211, 247],
    "restformwork": [212, 175, 162],
    "wetspot": [0, 139, 139],
    "rust": [255, 0, 0],
    "graffiti": [255, 140, 0],
    "weathering": [0, 128, 0],
    "exposed rebars": [207, 52, 118],
    "bearing": [139, 69, 19],
    "expansion joint": [169, 169, 169],
    "drainage": [139, 0, 0],
    "protective equipment": [128, 128, 0],
    "joint tape": [128, 0, 128],
    "cavity": [0, 255, 128],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = {
    "Research Paper": "https://arxiv.org/abs/2309.00460",
    "Dacl Challenge Data": "https://eval.ai/web/challenges/challenge-page/2130/overview",
}
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Johannes Flotzinger", "Philipp J. Rosch", "Thomas Braml"]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "johannes.flotzinger@unibw.de",
    "philipp.roesch@unibw.de",
    "thomas.braml@unibw.de",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "University of the Bundeswehr Munich, Germany"
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = ["https://www.unibw.de/home-en"]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Additionally, each label in images has ***concrete defect***, ***general defect***, or ***object part*** tag. Also every image in ***test*** dataset has one of following tags: ***test dev*** or ***test challenge***. Explore it in supervisely labeling tool"
}
TAGS: Optional[List[str]] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
