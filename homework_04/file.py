""" создание класса для работы с файлами """

import pathlib
import datetime

class File:
    def __init__(self, created_by='admin', storage_type='local'):
        """
        создать пустой объект, путь добавится при создании файла
        storage_type:  ('local', 'cloud'),признак на будущее, чтоб разделить логику обработки
        """
        self.full_path = None
        self.folder_path = None
        self.full_filename = None

        #мета данные
        self.created_by = created_by
        self.storage_type = storage_type
        self.created_at = None
        self.modified_at = None
        # флаг, что файл существует физически
        self._exists = False
        # тип файла буду брать из имени класса, типа videofile, audiofile
        self.type = self.__class__.__name__.lower()

    def create_file(self, full_path):
        # переделать в объект библитеки
        self.full_path = pathlib.Path(full_path)

        # отдельно сохранить путь и имя
        self.folder_path = self.full_path.parent
        self.full_filename = self.full_path.name

        # если папка не создана то создать (на один уровень в глубину)
        if not self.folder_path.exists():
            print(f' There is no folder "{self.folder_path}". Creating..')
            self.folder_path.mkdir(parents=True, exist_ok=True)
            print(f'Folder "{self.folder_path}" created')
        else:
            print(f'Folder "{self.folder_path}" already exists')

        # записать файл
        self.full_path.write_text('123')

        # и обновить мета дату
        self.created_at = datetime.datetime.now()
        self.modified_at = datetime.datetime.now()
        self._exists = True

        print(f'File created: {self.full_path}')
        return self

    def rename_file(self, new_full_path):
        # проверить существует ли файл физически
        if not self._exists or not self.full_path.exists():
            print(f'Error: no such file "{self.full_path}"')
            return self

        # опять переделать строку в объект
        new_path = pathlib.Path(new_full_path)

        # проверить не занято ли новое имя другим файлом
        if new_path.exists():
            print(f'Error: file "{new_full_path}" already exists')
            return self

        try:
            # Perform the rename
            self.full_path.rename(new_path)

            # обновить мета дату
            self.full_path = new_path
            self.folder_path = new_path.parent
            self.full_filename = new_path.name
            self.modified_at = datetime.datetime.now()

            print(f'Successfully renamed to: {new_full_path}')

        except Exception as e:
            print(f'rename_file error: {e}')

        return self

    def delete_file(self):

        if not self._exists or not self.full_path.exists():
            print(f'Error: no such file "{self.full_path}"')
            return False


        if self.full_path.is_dir():
            print(f'Error: "{self.full_path}" is a directory, not a file')
            return False

        try:

            self.full_path.unlink()

            # обновить статус, что физически не существует
            self._exists = False
            print(f'File deleted: {self.full_path}')
            return True

        except Exception as e:
            print(f'Error deleting file: {e}')
            return False

    def read_file(self):

        if not self._exists or not self.full_path.exists():
            raise FileNotFoundError(f"File not found: {self.full_path}")
        #чтение содержимого файла
        return self.full_path.read_text()

    def write_file(self, content):

        if not self._exists or not self.full_path.exists():
            raise FileNotFoundError(f"File not found: {self.full_path}")
        # запись в файл
        self.full_path.write_text(content)
        self.modified_at = datetime.datetime.now()
        return self

    def exists(self):

        return self._exists and self.full_path.exists() if self.full_path else False

    def __repr__(self):
        #все атрибуты в один список, чтобы показать на вызов принта
        attrs = []

        if self.full_path:
            attrs.append(f"full_path='{self.full_path}'")
            attrs.append(f"folder_path='{self.folder_path}'")
            attrs.append(f"full_filename='{self.full_filename}'")

        attrs.append(f"created_by='{self.created_by}'")
        attrs.append(f"storage_type='{self.storage_type}'")
        attrs.append(f"created_at='{self.created_at}'")
        attrs.append(f"modified_at='{self.modified_at}'")
        attrs.append(f"exists={self.exists()}")

        # итоговый джоин для принта
        return f"File(file type: {self.type}, {', '.join(attrs)})"


class VideoFile(File):
    """Video file class"""

class AudioFile(File):
    """Audio file class"""



# проверка что получилось. основной флоу работает, валидации конечно надо добавлять
if __name__ == '__main__':
    print('создание файла')
    file1 = VideoFile(created_by='user123', storage_type='local')
    print(f'File object: {file1}, file type: {file1.type}')

    file1.create_file('files_task/file_1.txt')
    print(f'After creation: {file1}')

    print('\nrename чек')
    file2 = AudioFile().create_file('files_task/file_2.txt').rename_file('files_task/file_renamed.txt')
    print(f'{file2}')

    print('\nчтение / запись')
    file3 = AudioFile().create_file('files_task/file_3.txt')
    file3.write_file('content check')
    content = file3.read_file()
    print(f'Content: {content}')
    file3.write_file('Updated content')

    print('\nудаление')
    if file2.delete_file():
        print('File deleted successfully')
    print(f'After deletion: {file2}')

    print('\nпроверка, если файл не существует')
    file4 = File()
    file4.rename_file('some/path.txt')
    file4.delete_file()
    print(f'Non-existent file object: {file4}')

