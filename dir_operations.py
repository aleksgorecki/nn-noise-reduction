import pathlib
import zipfile
import tarfile
import os


def extract_archive(archive_path: str, extracted_path: str):
    if zipfile.is_zipfile(archive_path):
        archive = zipfile.ZipFile(archive_path)
        archive.extractall(extracted_path)
    elif tarfile.is_tarfile(archive_path):
        archive = tarfile.TarFile(archive_path)
        archive.extractall(extracted_path)
    else:
        raise RuntimeError("File doesn't exist, is a directory or is not a zipfile or a tarfile")


def extract_archives(archives_dir: str, extracted_path: str):
    for file in os.listdir(archives_dir):
        try:
            extract_archive(f"{archives_dir}/{file}", f"{extracted_path}/{pathlib.Path(file).stem}")
        except RuntimeError:
            print(f"File {file} skipped - not a viable archive")


def dir_to_zip():
    pass


def zip_to_tar():
    pass


def check_is_dir(dir_path: str):
    if not os.path.isdir(dir_path):
        raise RuntimeError("Dataset path is not a directory or it doesn't exist")
    pass
