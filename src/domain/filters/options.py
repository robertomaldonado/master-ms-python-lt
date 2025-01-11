from typing import Optional


class Options:
    limit: Optional[int]
    page: Optional[int]

    def __init__(self, limit: Optional[int] = 10, page: Optional[int] = 0):
        self.limit = limit
        self.page = page

    def __repr__(self):
        return f'<Options limit={self.limit} page={self.page}>'

    def apply(self, query):
        if self.limit:
            query = query.limit(self.limit)

        return query