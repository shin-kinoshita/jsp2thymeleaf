
class CommentTemplate:
    @staticmethod
    def header_template(message):
        return "#### jsp2thymeleaf comment: {0}".format(message)

    @staticmethod
    def footer_template(message):
        return "#" * len(CommentTemplate.header_template(message))

    @staticmethod
    def hint_template(message):
        return "<hint> {0}".format(message)

    @staticmethod
    def transformation_impossible_template(message):
        return "<transformation impossible> {0}".format(message)

    @staticmethod
    def transformation_unreliable_template(message):
        return "<transformation unreliable> {0}".format(message)

    @staticmethod
    def base_tag_template(message):
        return "<base tag> {0}".format(message)

    @staticmethod
    def base_string_template(message):
        return "<base string> {0}".format(message)
