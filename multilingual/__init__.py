"""
Django-multilingual-ng: multilingual model support for Django 1.2.
"""
import warnings

VERSION = (0,1,0,'b15')
__version__ = '0.1.0b15'

try:
    from multilingual import models
    from multilingual.exceptions import TranslationDoesNotExist, LanguageDoesNotExist
    from multilingual.languages import (set_default_language, get_default_language,
                                        get_language_code_list)
    from multilingual.settings import FALLBACK_LANGUAGES
    from multilingual.translation import Translation
    from multilingual.admin import MultilingualModelAdmin, MultilingualInlineAdmin
    from multilingual.manager import Manager
    ModelAdmin = MultilingualModelAdmin
except ImportError:
    pass
