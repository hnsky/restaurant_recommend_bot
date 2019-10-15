import os
import string

from termcolor import colored

def get_template_dir_path():
    """Return the path of the template's directory

    Returns:
          str: The template dir path.
    """

    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')

    return template_dir_path

class NoTemplateError(Exception):
    """No Template Error"""

def find_template(template_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(template_dir_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    Returns:
        string.Template: Return templates with characters in templates.
    """

    template = find_template(template_file_path)
    with open(template, 'r') as template_file:
        contents = template_file.read()
        contents = contents.rstrip('\n')
        contents = '{spliter}\n{contents}\n{spliter}\n'.format(
            contens = contents, spliter = "=" * 60
        )
        contents = colored(contents, color)
        return string.Template(contents)
