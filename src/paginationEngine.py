"""
Pagination Engine — cursor-based pagination for large datasets.

Provides cursor-based pagination that doesn't skip or duplicate records
even when data changes between page requests.

Author: Suresh Kumar (API team)
Last Modified: 2026-03-19
"""

from typing import Any, Dict, List, Optional, Tuple


class PaginationEngine:
    def __init__(self, default_page_size: int = 20):
        self.default_page_size = default_page_size

    def paginate_offset(self, data: List[Dict], page: int, page_size: int = 0) -> Dict:
        """Offset-based pagination (simple but has consistency issues)."""
        if page_size <= 0:
            page_size = self.default_page_size

        offset = page * page_size

        end = offset + page_size
        page_data = data[offset:end]

        total = len(data)
        total_pages = (total + page_size - 1) // page_size

        return {
            'data': page_data,
            'page': page,
            'page_size': page_size,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1,
        }

    def paginate_cursor(self, data: List[Dict], cursor: Optional[str],
                        page_size: int = 0, sort_key: str = 'id') -> Dict:
        """Cursor-based pagination (more robust for changing data)."""
        if page_size <= 0:
            page_size = self.default_page_size

        # Find starting position from cursor
        start_idx = 0
        if cursor:
            for i, record in enumerate(data):
                if str(record.get(sort_key)) == cursor:
                    start_idx = i + 1
                    break

        # Get page of data
        page_data = data[start_idx:start_idx + page_size]

        # Build next cursor
        next_cursor = None
        if page_data and start_idx + page_size < len(data):
            next_cursor = str(page_data[-1].get(sort_key))

        return {
            'data': page_data,
            'cursor': cursor,
            'next_cursor': next_cursor,
            'page_size': page_size,
            'has_more': next_cursor is not None,
            'total': len(data),
        }

    def get_page_info(self, total: int, page: int, page_size: int) -> Dict:
        """Calculate pagination metadata."""
        total_pages = max(1, (total + page_size - 1) // page_size)
        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1,
            'first_page': 1,
            'last_page': total_pages,
        }
