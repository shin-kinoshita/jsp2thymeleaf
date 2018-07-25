import logging
import os
import glob
import shutil

from other_transform.transform import transform as other_transform
from bs_transform.transform import transform as bs_transform

IN_DIR_PATH = "./in_dir/"
OUT_DIR_PATH = "./out_dir/"


def main():
    init_logging()

    for in_path in import_path_list(IN_DIR_PATH):
        out_path = generate_out_path(in_path)
        tmp_path = generate_tmp_path(out_path)
        resolve_directories(os.path.dirname(out_path))
        logging.info("transforming {0} -> {1}".format(in_path, out_path))

        with open(in_path, 'r') as in_f:
            with open(tmp_path, 'w') as out_f:
                other_transform(in_f, out_f)
        shutil.move(tmp_path, out_path)

        with open(out_path, 'r') as in_f:
            with open(tmp_path, 'wb') as out_f:
                bs_transform(in_f, out_f)
        shutil.move(tmp_path, out_path)


def init_logging():
    logging.basicConfig(level=logging.INFO)


def import_path_list(in_dir):
    return glob.glob(os.path.join(in_dir, "**/*.jsp"), recursive=True)


def generate_out_path(in_path):
    return os.path.splitext(in_path.replace(IN_DIR_PATH, OUT_DIR_PATH, 1))[0] + ".html"


def generate_tmp_path(in_path):
    return os.path.splitext(in_path)[0] + "_tmp" + os.path.splitext(in_path)[1]


def resolve_directories(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    main()
