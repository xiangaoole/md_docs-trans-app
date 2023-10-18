import translators as ts
from md_translate import const
from md_translate.exceptions import UnknownServiceError


def get_translator_by_service_name(service_name: str):
    if service_name not in const.TRANSLATOR_BY_SERVICE_NAME:
        raise UnknownServiceError(service_name)
    def translator_class (line, from_language, to_language):
        return ts.translate_text(line, service_name.lower(), from_language, to_language)
    return translator_class
