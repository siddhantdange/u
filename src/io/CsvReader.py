
import csv
import itertools

class CsvReader:
    def __init__(self, fpath):
        self.fpath = fpath
        self.cur_row = 0
        self.file = open(self.fpath)
        self.reader = csv.reader(self.file, delimiter=',')
        self.columns = next(self.reader)
        self.column_idx = {}

        for idx in range(len(self.columns)):
            self.column_idx[self.columns[idx]] = idx

    def get_current_row(self):
        return self.reader.line_num

    def get_columns(self):
        return self.reader.fieldnames

    def get_num_rows(self):
        total = -1 # discard header

        with open(self.fpath) as f:
            for line in f:
                total += 1
        return total

    def get_next_row(self):
        return next(self.reader)

    def get_row_at_index(self, index):
        line = None
        with open(self.fpath) as f:
            temp_reader = csv.reader(f, delimiter=',')
            next(temp_reader) # header
            for _ in range(index + 1):
                line = next(temp_reader)
        return line

    def get_value_for_row_col(self, row, col):
        if col not in self.columns:
            return None

        return row[self.column_idx[col]]

    def reset_reader(self):
        self.file.close()
        self.file = open(self.fpath)
        self.reader = csv.reader(self.file, delimiter=',')
