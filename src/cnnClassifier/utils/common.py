import os  # Provides a way to interact with the operating system, like reading or writing files.
from box.exceptions import BoxValueError  # Handles exceptions specific to the Box library, often used for dealing with configurations.
import yaml  # Used for parsing and writing YAML, a human-readable data serialization standard.
from cnnClassifier import logger  # Imports a custom logger from the cnnClassifier package for logging messages.
import json  # Provides functions to parse JSON strings and convert Python objects to JSON.
import joblib  # Used for serializing Python objects, often for saving and loading machine learning models.
from ensure import ensure_annotations  # A decorator for enforcing type annotations at runtime.
from box import ConfigBox  # A subclass of Python dictionaries with dot notation access to dictionary attributes, used for configurations.
from pathlib import Path  # Provides an object-oriented interface for working with filesystem paths.
from typing import Any  # Used for type hinting, allowing any type of variable.
import base64  # Provides functions for encoding and decoding data using Base64, often for handling binary data in text format.



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
# Purpose:
# This function reads a YAML file and converts its contents into a ConfigBox, which allows easy access to data with dot notation.
# Usage:
# YAML Files: YAML files are used for configuration because they are easy to read and write.


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# Purpose:
# This function creates directories specified in a list.
# Usage:
# Directory Creation: Ensures necessary directories exist for organizing project files.

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

# Purpose:
# This function saves data as a JSON file.
# Usage:
# Data Storage: JSON files are used for storing structured data.


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

# Purpose:
# This function loads data from a JSON file and returns it as a ConfigBox.
# Usage:
# Data Loading: Reads data back into the program from a JSON file.


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

# Purpose:
# This function saves data in a binary format.
# Usage:
# Model Persistence: Commonly used for saving machine learning models.

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

# Purpose:
# This function loads data from a binary file.
# Usage:
# Model Loading: Retrieves saved machine learning models.

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

# Purpose:
# This function returns the size of a file in kilobytes.
# Usage:
# File Management: Useful for monitoring file sizes.


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

# Purpose:
# This function decodes a base64-encoded string and saves it as an image file.
# Usage:
# Image Processing: Converts encoded image data back to image files.

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
# Purpose:
# This function reads an image file and encodes it into a base64 string.
# Usage:
# Image Transmission: Converts images to a format suitable for embedding in text formats like JSON or HTML.


# Summary
# @ensure_annotations: This decorator ensures that type annotations are enforced at runtime.
# read_yaml: Reads a YAML configuration file.
# create_directories: Creates a list of directories.
# save_json: Saves data as a JSON file.
# load_json: Loads data from a JSON file.
# save_bin: Saves data in a binary format.
# load_bin: Loads data from a binary file.
# get_size: Gets the size of a file in KB.
# decodeImage: Decodes a base64 string to an image file.
# encodeImageIntoBase64: Encodes an image file to a base64 string.