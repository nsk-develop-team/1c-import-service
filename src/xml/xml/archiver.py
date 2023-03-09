import logging
import os
import zipfile

from ...exceptions import SplitZipFileError, XmlToZipError

logger = logging.getLogger('main')


def xml_to_zip():
    """Archives the XML to a ZIP file."""
    try:
        parent_dir_path = os.path.dirname(os.path.dirname(__file__))
        path_to_xmlfile = parent_dir_path + '/data/datafile.xml'
        path_to_zipfile = parent_dir_path + '/data/datafile.zip'
        with zipfile.ZipFile(path_to_zipfile, 'w') as zip_file:
            zip_file.write(path_to_xmlfile, arcname='datafile.xml')
        os.remove(path_to_xmlfile)
        logger.info('xml_to_zip - OK')

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        raise XmlToZipError
    except Exception as err:
        logger.exception(f'Exception: {err}')
        raise XmlToZipError


def split_zip_file():
    """Split a ZIP file into chunks of a given size."""
    try:
        parent_dir_path = os.path.dirname(os.path.dirname(__file__))
        path_to_datafile = parent_dir_path + '/data/datafile.zip'
        part_size = 2097152  # 2 MB = 2097152 byte
        zip_name, ext = os.path.splitext(path_to_datafile)
        with zipfile.ZipFile(path_to_datafile, 'r') as zip_file:
            num_parts = (
                zip_file.getinfo(file).file_size
                for file in zip_file.namelist()
            )
            for num, file in enumerate(zip_file.namelist()):
                num_part = 0
                with open(f'{zip_name}.{num + 1:03d}{ext}', 'wb') as part:
                    with zip_file.open(file, 'r') as source:
                        while True:
                            part_data = source.read(part_size)
                            if not part_data:
                                break
                            part.write(part_data)
                            num_part += len(part_data)
                num_parts -= num_part
                if num_parts <= 0:

                    break

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        raise SplitZipFileError
    except Exception as err:
        logger.exception(f'Exception: {err}')
        raise SplitZipFileError
