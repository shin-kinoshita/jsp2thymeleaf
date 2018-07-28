class BsTransformDef:
    def __init__(self, tag_def_list, extra_operation_def_list):
        self.tag_def_list = tag_def_list
        self.extra_operation_def_list = extra_operation_def_list

    def get_extra_logic_def_list(self):
        return self.extra_logic_def_list

    def get_extra_operation_def_list(self):
        return self.extra_operation_def_list

    def get_tag_def_list(self):
        return self.tag_def_list
