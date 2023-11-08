import json
from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            for key in data:
                self.students[key] = []
                for subj in data[key]:
                    self.students[key].append(
                        (subj, data[key][subj]))
            print(self.students)
        return self.students
