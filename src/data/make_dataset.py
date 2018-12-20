# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd 
import os
import configparser


config = configparser.ConfigParser()
config.read("~\config.ini")

def load_data():

    logger = logging.getLogger(__name__)
    path_config = config["PATH"]
    files_config = config["FILES"]

    input_filepath = path_config["input_filepath"]
    output_filepath = path_config["output_filepath"]

    for file in [val for val in files_config]:
        file_name = files_config[file]
        logger.info("processing file {}".format(file_name))
        file_df = pd.read_csv(os.path.join(input_filepath,file_name))
        file_df.to_csv(os.path.join(output_filepath,file_name))


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("making final data set from raw data")
    load_data()

if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(usecwd=True))


    main()
