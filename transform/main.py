from transform.transform_tags import transform_tags
import os
import glob

in_dir_path = "./in_dir"
out_dir_path = "./out_dir"


def main():
    for in_path in import_path_list(in_dir_path):
        out_path = os.path.join(out_dir_path, os.path.basename(in_path))
        out_path = os.path.splitext(out_path)[0] + ".html"
        with open(in_path, 'r') as in_f:
            with open(out_path, 'wb') as out_f:
                transform_tags(in_f, out_f)


def import_path_list(in_dir):
    return glob.glob(os.path.join(in_dir, "*.jsp"))


if __name__ == '__main__':
    main()
