import os
import json
import shutil
import librosa
import audioread
import pathlib
import soundfile as sf

from dir_operations import check_is_dir


def convert_gtzan(dir_path: str, output_dataset_path: str):
    check_is_dir(dir_path)

    metadata = {
        "dataset": "gtzan",
        "data_kind": "music",
    }

    samples = {}
    classes = []
    file_counter = 0

    genres_dir = f"{dir_path}/Data/genres_original"

    for genre in os.listdir(genres_dir):
        classes.append(genre)
        for file_name in os.listdir(f"{genres_dir}/{genre}"):
            file_path = f"{genres_dir}/{genre}/{file_name}"
            try:
                sample_rate = librosa.core.get_samplerate(file_path)
                with audioread.audio_open(file_path) as f:
                    duration = f.duration
                new_name = f"{file_counter}{pathlib.Path(file_name).suffix}"
                samples.update(
                    {
                        new_name: {
                            "name": new_name,
                            "original_name": file_name,
                            "sample_rate": sample_rate,
                            "duration": duration,
                            "class": genre
                        }
                    })
                shutil.copy2(file_path, f"{output_dataset_path}/{new_name}")
                file_counter += 1

            except (sf.LibsndfileError, audioread.exceptions.NoBackendError):
                print(f"File {file_name} was skipped")

    metadata.update({"classes": classes,
                     "samples": samples
                     })

    with open(f"{output_dataset_path}/metadata.json", "w") as metada_file:
        json.dump(metadata, metada_file, indent=4)


def convert_fma(dir_path: str, output_dataset_path: str):
    pass


def convert_demand(dir_path: str, output_dataset_path: str):
    check_is_dir(dir_path)

    metadata = {
        "dataset": "demand",
        "data_kind": "noise",
    }

    samples = {}
    classes = []
    file_counter = 0

    viable_dirs = filter(lambda x: pathlib.Path(x).stem.endswith("48k"), os.listdir(dir_path))

    for noise_class in viable_dirs:
        inner_dir = noise_class.replace("_48k", "")
        classes.append(inner_dir)
        for file_name in os.listdir(f"{dir_path}/{noise_class}/{inner_dir}"):
            file_path = f"{dir_path}/{noise_class}/{inner_dir}/{file_name}"
            try:
                sample_rate = librosa.core.get_samplerate(file_path)
                with audioread.audio_open(file_path) as f:
                    duration = f.duration
                new_name = f"{file_counter}{pathlib.Path(file_name).suffix}"
                samples.update(
                    {
                        new_name: {
                            "original_name": file_name,
                            "sample_rate": sample_rate,
                            "duration": duration,
                            "class": inner_dir
                        }
                    })
                shutil.copy2(file_path, f"{output_dataset_path}/{new_name}")
                file_counter += 1

            except (sf.LibsndfileError, audioread.exceptions.NoBackendError):
                print(f"File {file_name} was skipped")

    metadata.update({"classes": classes,
                     "samples": samples
                     })

    with open(f"{output_dataset_path}/metadata.json", "w") as metada_file:
        json.dump(metadata, metada_file, indent=4)


def convert_urban_sound(dir_path: str, output_dataset_path: str):
    pass


def convert_vctk(dir_path: str, output_dataset_path: str):
    pass


def convert_commonvoice_pl(dir_path: str, output_dataset_path: str):
    pass


def convert_custom():
    pass


if __name__ == "__main__":
    pass
