import os
import sys
import yaml

from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import (Any, List)

from TextSummarization.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str): yaml file path input

    Raises:
        ValueError: if file is empty
        e: other exceptions

    Return:
        configBox: ConfigBox type contents in the yaml file
    """

    try:
        with open(path_to_yaml, 'w') as yaml_obj:
            content = yaml.safe_load(yaml_obj)
            return ConfigBox(content)

    except Exception as e:
        logger.error(f"error while reading yaml file {path_to_yaml} \n {e}")




@ensure_annotations
def create_directories(path_to_directories:List, verbose:True):
    """
    Creates directories mentioned in the list

    Args:
    path_to_directories: List: list of path of directories    
    """

    try:
        for dir in path_to_directories:
            os.makedirs(dir, exist_ok=True)
            if verbose:
                logger.info(f"created directory {dir}")


    except Exception as e:
        logger.error(f"error while creating directories {e}")



@ensure_annotations
def get_size(path:Path) -> str:
    """
    get Size in KB

    Args:
        path (Path): path of the file object

    Returns:
        str: size of the file object in KB
    """

    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    
    except Exception as e:
        logger.error(f"error while getting the size of file {path} \n {e}")