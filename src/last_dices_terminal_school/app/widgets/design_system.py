from __future__ import annotations


def divider(label: str) -> str:
    return f"{label}\n" + "=" * len(label)


def status_marker(state: str, message: str) -> str:
    tag = state.upper()
    return f"[{tag}] {message}"


def bracket_button(label: str) -> str:
    return f"[ {label.upper()} ]"


def progress_bar(percent: int, width: int = 26) -> str:
    p = max(0, min(100, percent))
    fill = int((p / 100) * width)
    return "[" + ("#" * fill) + ("-" * (width - fill)) + f"] {p}%"


def terminal_table(headers: list[str], rows: list[list[str]]) -> str:
    widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            widths[i] = max(widths[i], len(col))

    fmt = " | ".join([f"{{:<{w}}}" for w in widths])
    sep = "-+-".join(["-" * w for w in widths])

    lines = [fmt.format(*headers), sep]
    for row in rows:
        lines.append(fmt.format(*row))
    return "\n".join(lines)
