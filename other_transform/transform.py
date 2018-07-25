from .logic import logic_list


def transform(in_file, out_file):
    contents = in_file.read()
    for logic in logic_list:
        contents = logic.operation(contents)
    out_file.write(contents)
