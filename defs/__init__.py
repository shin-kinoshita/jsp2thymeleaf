import os
import glob
import importlib

from .bs_transform_def import BsTransformDef
from .other_transform_def import OtherTransformDef

bs_extra_logic_def_list = list()
bs_extra_operation_def_list = list()
bs_tag_def_list = list()
other_logic_def_list = list()

target_path = os.path.join(os.path.dirname(__file__), "*", "__init__.py")
def_package_list = [__name__ + "." + os.path.split(os.path.dirname(path))[1] for path in glob.glob(target_path)]

for package in def_package_list:
    module = importlib.import_module(package)
    bs_extra_logic_def_list += module.bs_extra_logic_def_list
    bs_extra_operation_def_list += module.bs_extra_operation_def_list
    bs_tag_def_list += module.bs_tag_def_list
    other_logic_def_list += module.other_logic_def_list

for operation_def in bs_extra_operation_def_list:
    operation_def.set_logic_list(bs_extra_logic_def_list)

bs_transform_def = BsTransformDef(
    tag_def_list=bs_tag_def_list,
    extra_operation_def_list=bs_extra_operation_def_list
)
other_transform_def = OtherTransformDef(
    logic_def_list=other_logic_def_list
)

