from transform.transform import transform
import os
import glob

IN_DIR_PATH = "./in_dir/"
OUT_DIR_PATH = "./out_dir/"


def main():
    for in_path in import_path_list(IN_DIR_PATH):
        out_path = generate_out_path(in_path)
        resolve_directories(os.path.dirname(out_path))
        with open(in_path, 'r') as in_f:
            with open(out_path, 'wb') as out_f:
                transform(in_f, out_f)


def import_path_list(in_dir):
    return glob.glob(os.path.join(in_dir, "**/*.jsp"), recursive=True)


def generate_out_path(in_path):
    return os.path.splitext(in_path.replace(IN_DIR_PATH, OUT_DIR_PATH, 1))[0] + ".html"


def resolve_directories(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    main()
