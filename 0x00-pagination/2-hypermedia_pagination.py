#!/usr/bin/env python3
''' Simple pagination.
'''

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Return a tuple of size two containing a start index
    and an end index
    '''
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieves a page of data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start < len(data):
            return data[start:end]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        '''
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if end < len(self.__dataset) else None

        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_pafe': page - 1 if start > 0 else None,
                'total_pages': total_pages,
                }
