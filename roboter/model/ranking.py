"""Generates ranking model to write to CSV

TODO Rewrite to DB instead of CSV
"""
import collections
import csv
import os
import pathlib

RANKING_COLOMN_NAME = 'NAME'
RANKING_COLOMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'

class CsvModel(object):
    """Base csv Model."""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()


class RankingModel(CsvModel):
    """Definition of class that generates ranking model to wirte to CSV"""
    def __init__(self, csv_file=None, *args, **kargs):
         if not csv_file:
             csv_file = self.get_csv_file_path()
         super().__init__(csv_file, *args, **kwargs)
         self.column = [RANKING_COLOMN_NAME, RANKING_COLOMN_COUNT]
         self.data = collections.defaultdict(int)
         self.load.data()

    def get_csv_file_path(self):
        """Set csv file path.

        Use csv path if set in settings, otherwise use default
        """
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path

    def load_data(self):
        """Load csv data.

        Returns:
            dict: Returns ranking data of dict type.
        """
        with open(self.csv_file, 'r') as csv_file:
            reader - csv.DictReader(csv_file)