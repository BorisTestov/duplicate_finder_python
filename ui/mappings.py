from dataclasses import dataclass

from search_types import SearchTypes


@dataclass
class Mappings:
    type_mappings = {
        'hash': SearchTypes.BY_HASH,
        'name': SearchTypes.BY_NAME
    }

    size_mappings = {
        'b': 2 ** 0,
        'KB': 2 ** 10,
        'MB': 2 ** 20,
        'GB': 2 ** 30
    }
