from pprint import pprint

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


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}
    
    with open(path, 'r', encoding='utf-8') as file:
        book_content = file.read()
    
    print(book)

    start = 0
    page_count = 0
    end = len(book_content) / page_size    
    
    while(page_count < 16):
        page, start = _get_part_text(book_content, start, page_size)
        
        page.lstrip('-\xa0').rstrip('\n')
        book[page_count] = page
        
        end -= 1
        page_count += 1
        print(page_count)

    return book

pprint(prepare_book('book/book.txt'))