from cursor_pagination import CursorPaginator


def chunked_queryset_iterator(queryset, size, *, ordering=('id',)):
    pager = CursorPaginator(queryset, ordering)
    after = None
    while True:
        page = pager.page(after=after, first=size)
        if page:
            yield from page.items
        else:
            return
        if not page.has_next:
            break
        after = pager.cursor(instance=page[-1])


