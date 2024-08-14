def get_horizontal_rule(title: str, *, length: int, border: str, filler: str) -> str:
    if title:
        return _get_titled(title, length=length, border=border, filler=filler)
    return _get_untitled(length=length, border=border, filler=filler)


def _get_titled(title: str, *, length: int, border: str, filler: str) -> str:
    filler_length = max(length - 4 - len(title) - 2*len(border), 2)
    side_filler_length = -(filler_length // -2)  # ceiling division
    side_filler = filler * side_filler_length
    return f"{border} {side_filler} {title} {side_filler} {border[::-1]}"


def _get_untitled(*, length: int, border: str, filler: str) -> str:
    filler_length = max(length - 2 - 2*len(border), 1)
    return f"{border} {filler * filler_length} {border[::-1]}"
