BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    symb = ('.', ',', '!', '?', ':', ';')
    if len(text) < start + page_size:
        return text[start:], len(text) - start
    while text[start + page_size] in symb:
        page_size -= 1
    while text[start + page_size] not in symb:
        page_size -= 1
    page_size += 1
    return text[start:start + page_size], page_size


def prepare_book(path: str) -> None:
    with open(path) as f:
        booktxt = f.read()
    text_start = 0
    page_num = 1
    while text_start != len(booktxt):
        book_text, text_end = _get_part_text(booktxt, text_start, PAGE_SIZE)
        text_start += text_end
        book[page_num] = book_text.strip()
        page_num += 1


prepare_book(BOOK_PATH)
