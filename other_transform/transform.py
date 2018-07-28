from defs import other_transform_def


def transform(in_file, out_file):
    contents = in_file.read()
    for logic_def in other_transform_def.get_logic_def_list():
        contents = logic_def.operation(contents)
    out_file.write(contents)
