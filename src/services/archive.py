import logging
import os
import zipfile

from ..exceptions import SplitZipFileError, XmlToZipError

logger = logging.getLogger('web')


def xml_to_zip(xml_document_path):
    """Archives the XML to a ZIP file."""
    try:
        file_name = os.path.basename(xml_document_path)
        zip_document_path = xml_document_path.replace('.xml', '.zip')
        with zipfile.ZipFile(zip_document_path, 'w') as zf:
            zf.write(xml_document_path, arcname=file_name)

        logger.info('xml_to_zip - OK')
        return zip_document_path

    except FileNotFoundError as err:
        raise XmlToZipError(f'FileNotFoundError: {err}')
    except Exception as err:
        raise XmlToZipError(f'Exception: {err}')


# TODO: replace constant and return file path
# def split_zip_file(size):
#     """Split a ZIP file into chunks of a given size."""
#     try:
#         with zipfile.ZipFile(DATAFILE_ZIP_PATH, 'r') as zf:
#             size_files = zf.getinfo(DATAFILE_NAME + '.xml').file_size
#
#             num_part = 1
#             with zf.open(DATAFILE_NAME + '.xml', 'r') as source:
#                 while size_files > 0:
#                     part_path = DATAFILE_XML_PATH
#                     with open(part_path, 'wb') as part:
#                         part_data = source.read(size)
#                         part.write(part_data)
#                     with zipfile.ZipFile(
#                         f'{DATAFILE_PATH}.zip.{num_part:03d}', 'w'
#                     ) as part_zf:
#                         part_zf.write(
#                             part_path, arcname=f'{DATAFILE_NAME}.xml'
#                         )
#                     num_part += 1
#                     size_files -= len(part_data)
#
#         logger.info('split_zip_file - OK')
#
#     except FileNotFoundError as err:
#         raise SplitZipFileError(f'FileNotFoundError: {err}')
#     except Exception as err:
#         raise SplitZipFileError(f'Exception: {err}')