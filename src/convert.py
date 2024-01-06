import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name, get_file_name_with_ext
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    train_images_path = "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_devphase/images/train"
    val_images_path = "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_devphase/images/validation"
    test_dev_images_path = "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_devphase/images/testdev"
    challenge_test_data_path = (
        "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_testchallenge/images/testchallenge"
    )

    train_anns_path = "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_devphase/annotations/train"
    val_anns_path = "/home/alex/DATASETS/TODO/dacl10k/dacl10k_v2_devphase/annotations/validation"

    batch_size = 30

    ds_name_to_split = {
        "train": (train_images_path, train_anns_path),
        "val": (val_images_path, val_anns_path),
        "test": (None, None),
    }

    def create_ann(image_path):
        labels = []

        if ds_name == "test":
            image_np = sly.imaging.image.read(image_path)[:, :, 0]
            img_height = image_np.shape[0]
            img_wight = image_np.shape[1]
            subfolder_value = image_path.split("/")[-2]
            subfolder_meta = subfolder_value_to_tag[subfolder_value]
            subfolder = sly.Tag(subfolder_meta)
            return sly.Annotation(
                img_size=(img_height, img_wight), labels=labels, img_tags=[subfolder]
            )

        ann_path = os.path.join(anns_path, get_file_name(image_path) + ".json")
        ann_data = load_json_file(ann_path)
        img_height = ann_data["imageHeight"]
        img_wight = ann_data["imageWidth"]

        ann_labels = ann_data["shapes"]
        for curr_ann_label in ann_labels:
            class_name = curr_ann_label["label"]
            if class_name in object_classes:
                class_type = sly.Tag(object_meta)
            elif class_name in general_classes:
                class_type = sly.Tag(general_meta)
            else:
                class_type = sly.Tag(concrete_meta)
            obj_class = names_to_obj_classes[class_name]
            coords = curr_ann_label["points"]
            exterior = [[coord[1], coord[0]] for coord in coords]
            polygon = sly.Polygon(exterior)
            label_poly = sly.Label(polygon, obj_class, tags=[class_type])
            labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)

    testdev_meta = sly.TagMeta("test dev", sly.TagValueType.NONE)
    testchallenge_meta = sly.TagMeta("test challenge", sly.TagValueType.NONE)
    subfolder_value_to_tag = {"testdev": testdev_meta, "testchallenge": testchallenge_meta}
    general_meta = sly.TagMeta("general defect", sly.TagValueType.NONE)
    concrete_meta = sly.TagMeta("concrete defect", sly.TagValueType.NONE)
    object_meta = sly.TagMeta("object part", sly.TagValueType.NONE)

    names_to_obj_classes = {
        "Weathering": sly.ObjClass("weathering", sly.Polygon),
        "PEquipment": sly.ObjClass("protective equipment", sly.Polygon),
        "Rust": sly.ObjClass("rust", sly.Polygon),
        "Cavity": sly.ObjClass("cavity", sly.Polygon),
        "Drainage": sly.ObjClass("drainage", sly.Polygon),
        "Efflorescence": sly.ObjClass("efflorescence", sly.Polygon),
        "ACrack": sly.ObjClass("alligator crack", sly.Polygon),
        "JTape": sly.ObjClass("joint tape", sly.Polygon),
        "Spalling": sly.ObjClass("spalling", sly.Polygon),
        "Graffiti": sly.ObjClass("graffiti", sly.Polygon),
        "Restformwork": sly.ObjClass("restformwork", sly.Polygon),
        "Wetspot": sly.ObjClass("wetspot", sly.Polygon),
        "ExposedRebars": sly.ObjClass("exposed rebars", sly.Polygon),
        "Bearing": sly.ObjClass("bearing", sly.Polygon),
        "EJoint": sly.ObjClass("expansion joint", sly.Polygon),
        "Hollowareas": sly.ObjClass("hollowareas", sly.Polygon),
        "Crack": sly.ObjClass("crack", sly.Polygon),
        "WConccor": sly.ObjClass("washouts/concrete corrosion", sly.Polygon),
        "Rockpocket": sly.ObjClass("rockpocket", sly.Polygon),
    }

    object_classes = ["Bearing", "EJoint", "Drainage", "PEquipment", "JTape", "WConccor"]
    general_classes = ["Rust", "Weathering", "Wetspot", "Graffiti"]

    meta = sly.ProjectMeta(
        tag_metas=[testdev_meta, testchallenge_meta, general_meta, concrete_meta, object_meta],
        obj_classes=list(names_to_obj_classes.values()),
    )

    api.project.update_meta(project.id, meta.to_json())

    for ds_name, data_pathes in ds_name_to_split.items():
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_path, anns_path = data_pathes

        if ds_name != "test":
            images_names = os.listdir(images_path)

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(images_path, image_name) for image_name in img_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
                api.annotation.upload_anns(img_ids, anns_batch)

                progress.iters_done_report(len(img_names_batch))

        else:
            challenge_test_pathes = [
                os.path.join(challenge_test_data_path, im_name)
                for im_name in os.listdir(challenge_test_data_path)
            ]
            test_dev_pathes = [
                os.path.join(test_dev_images_path, im_name)
                for im_name in os.listdir(test_dev_images_path)
            ]
            test_pathes = challenge_test_pathes + test_dev_pathes
            progress = sly.Progress("Create dataset {}".format(ds_name), len(test_pathes))

            for img_pathes_batch in sly.batched(test_pathes, batch_size=batch_size):
                img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(img_names_batch))

    return project
