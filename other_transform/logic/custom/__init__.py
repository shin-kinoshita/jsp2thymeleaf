import os
import glob
import importlib

logic_list = []
target_path = os.path.join(os.path.dirname(__file__), "*", "__init__.py")
package_list = [__name__ + "." + os.path.split(os.path.dirname(path))[1] for path in glob.glob(target_path)]

for package in package_list:
    module = importlib.import_module(package)
    if module.logic_list is not None:
        logic_list += module.logic_list
