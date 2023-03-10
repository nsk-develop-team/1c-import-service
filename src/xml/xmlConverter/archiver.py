import logging
import os
import zipfile

from .constants import (DATAFILE_NAME, DATAFILE_PATH, DATAFILE_XML_PATH,
                        DATAFILE_ZIP_PATH)

logger = logging.getLogger('web')


def xml_to_zip():
    """Archives the XML to a ZIP file."""
    try:
        with zipfile.ZipFile(DATAFILE_ZIP_PATH, 'w') as zf:
            zf.write(DATAFILE_XML_PATH, arcname=DATAFILE_NAME+'.xml')

        logger.info('xml_to_zip - OK')
        os.remove(DATAFILE_XML_PATH)

        return True

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return False
    except Exception as err:
        logger.exception(f'Exception: {err}')
        return False


def split_zip_file(size):
    """Split a ZIP file into chunks of a given size."""
    try:
        with zipfile.ZipFile(DATAFILE_ZIP_PATH, 'r') as zf:
            size_files = zf.getinfo(DATAFILE_NAME + '.xml').file_size

            num_part = 1
            with zf.open(DATAFILE_NAME + '.xml', 'r') as source:
                while size_files > 0:
                    part_path = DATAFILE_XML_PATH
                    with open(part_path, 'wb') as part:
                        part_data = source.read(size)
                        part.write(part_data)
                    with zipfile.ZipFile(
                        f'{DATAFILE_PATH}.zip.{num_part:03d}', 'w'
                    ) as part_zf:
                        part_zf.write(
                            part_path, arcname=f'{DATAFILE_NAME}.xml'
                        )
                    os.remove(part_path)
                    num_part += 1
                    size_files -= len(part_data)

        logger.info('split_zip_file - OK')
        os.remove(DATAFILE_ZIP_PATH)

        return True

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return False
    except Exception as err:
        logger.exception(f'Exception: {err}')
        return False
