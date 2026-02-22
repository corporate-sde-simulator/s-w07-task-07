"""
Result Serializer — formats paginated results for API responses.

Author: Suresh Kumar (API team)
Last Modified: 2026-03-19
"""

from typing import Any, Dict, List, Optional


class ResultSerializer:
    """Serializes paginated results into standard API response format."""

    def serialize(self, pagination_result: Dict, format_type: str = 'standard') -> Dict:
        """Serialize pagination result into API response format."""
        if format_type == 'standard':
            return self._standard_format(pagination_result)
        elif format_type == 'envelope':
            return self._envelope_format(pagination_result)
        elif format_type == 'hal':
            return self._hal_format(pagination_result)
        return pagination_result

    def _standard_format(self, result: Dict) -> Dict:
        """Standard JSON API response format."""
        response = {
            'data': result.get('data', []),
            'pagination': {
                'total': result.get('total', 0),
                'page_size': result.get('page_size', 20),
            }
        }

        if 'page' in result:
            response['pagination']['page'] = result['page']
            response['pagination']['total_pages'] = result.get('total_pages', 1)

        if 'cursor' in result:
            response['pagination']['cursor'] = result.get('cursor')
            response['pagination']['next_cursor'] = result.get('next_cursor')

        response['pagination']['has_more'] = result.get('has_next', result.get('has_more', False))
        return response

    def _envelope_format(self, result: Dict) -> Dict:
        """Envelope format wrapping data and metadata."""
        return {
            'success': True,
            'data': result.get('data', []),
            'meta': {
                'total': result.get('total', 0),
                'count': len(result.get('data', [])),
            },
        }

    def _hal_format(self, result: Dict) -> Dict:
        """HAL (Hypertext Application Language) format."""
        return {
            '_embedded': {
                'items': result.get('data', []),
            },
            'page': {
                'size': result.get('page_size', 20),
                'totalElements': result.get('total', 0),
                'totalPages': result.get('total_pages', 1),
                'number': result.get('page', 1),
            },
        }
