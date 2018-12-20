# -*- coding: utf-8 -*-
import configparser
import logging
import os
from pathlib import Path

import pandas as pd
from dotenv import find_dotenv, load_dotenv


def load_data():
    """ Loads data as defined in config file, runs process_data and writes it to processed 
    """

    logger = logging.getLogger(__name__)
    path_config = config["PATH"]
    files_config = config["FILES"]

    input_filepath = path_config["input_filepath"]
    output_filepath = path_config["output_filepath"]

    for file in [val for val in files_config]:
        file_name = files_config[file]
        logger.info("processing file {}".format(file_name))
        file_df = pd.read_csv(os.path.join(input_filepath, file_name))
        process_data(file_df)
        file_df.to_csv(os.path.join(output_filepath, file_name))
    logger.info("processing done")

def process_data(df):
    """ process data 
    
    Arguments:
        df {dataframe} -- df to be processed by refference
    """

    pass

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
    config = configparser.ConfigParser()
    config.read(
        "~\\config.ini"
    )

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(usecwd=True))

    main()
