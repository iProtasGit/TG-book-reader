import logging

logger = logging.getLogger(__name__)

def find_last_sep(text: str) -> str:
    if text[-1] in ['?', ',', '.', ',', ';', '!']:
        if text[-2] in ['?', ',', '.', ';', '!']:
            return find_last_sep(text[:-2])
        return text
    return find_last_sep(text[:-1])


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page_text = text[start:size+start]
    page_text = find_last_sep(page_text)
    
    page_size = len(page_text)

    return page_text, page_size


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}
    
    with open(path, 'r', encoding='utf-8') as file:
        book_content = file.read()

    page_count = 1
    start = 0
    end = len(book_content) / page_size + 1
    
    while(end > page_count):
        page, size = _get_part_text(book_content, start, page_size)
        
        page = page.lstrip()
        book[page_count] = page
        
        page_count += 1
        start += size
    return book