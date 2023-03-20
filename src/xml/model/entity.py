from src.exceptions import EntityError


class Entity(object):
    """Bases config properties:
    file_name - Export xml file name
    template_name - Template file name,
    body_path - Path to head entity element,
    entity_path - Path to head entity element,
    dictionary - Constant dictionary values,
    mapping - Description item names and mapping paths to them,
    dictionary_mapping - Description constant values and mapping paths to them
    """
    def __init__(self, config):
        """Set configuration
        """
        try:
            self.file_name = config.FILE_NAME
            self.template_name = config.TEMPLATE_NAME
            self.body_path = config.BODY_PATH
            self.element_path = config.ELEMENT_PATH
            self.dictionary = config.DICTIONARY
            self.dictionary_mapping = config.DICTIONARY_MAPPING
            self.mapping = config.MAPPING
        except Exception as err:
            raise EntityError(f'EntityError: {err}')

    def is_valid(self, data):
        for key in data.keys():
            if key not in self.mapping.keys():
                return False
        return True
