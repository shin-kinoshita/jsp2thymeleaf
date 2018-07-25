import os
import glob
import importlib

tag_def_list = []
target_path = os.path.join(os.path.dirname(__file__), "*", "__init__.py")
package_list = [__name__ + "." + os.path.split(os.path.dirname(path))[1] for path in glob.glob(target_path)]

for package in package_list:
    module = importlib.import_module(package)
    if module.tag_def_list is not None:
        tag_def_list += module.tag_def_list
