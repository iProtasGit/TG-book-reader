import logging
import os

logger = logging.getLogger(__name__)

def find_last_sep(text: str) -> str:
    if text[-1] in ['?', ',', '.', ':', ';']:
        if text[-2] in ['?', ',', '.', ':', ';']:
            return find_last_sep(text[:-2])
        
        return text
    return find_last_sep(text[:-1])


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page_text = text[start:size+start]
    page_text = find_last_sep(page_text)
    
    page_size = len(page_text)

    return page_text, page_size


# Функция, формирующая словарь книги
def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

   

    return book