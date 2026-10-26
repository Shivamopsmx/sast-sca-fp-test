# LIKELY FALSE POSITIVE: eval() is flagged, but its argument is a hardcoded
# constant literal defined in this file — no user input ever reaches it.
_FORMULA = "2 * 21"


def answer() -> int:
    return eval(_FORMULA)
