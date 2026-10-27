"""Simple data formatting functions."""

from datetime import datetime


def format_currency(amount, symbol="$"):
    """1234.5 -> $1,234.50"""
    return f"{symbol}{amount:,.2f}"


def format_percent(value, decimals=1):
    """0.256 -> 25.6%"""
    return f"{value * 100:.{decimals}f}%"


def format_number(number):
    """1234567 -> 1,234,567"""
    return f"{number:,}"


def format_date(date_string, input_format="%Y-%m-%d", output_format="%d %b %Y"):
    """2026-10-27 -> 27 Oct 2026"""
    date = datetime.strptime(date_string, input_format)
    return date.strftime(output_format)


def format_phone(phone):
    """9876543210 -> (987) 654-3210"""
    digits = "".join(ch for ch in phone if ch.isdigit())
    if len(digits) != 10:
        return phone
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def format_name(name):
    """'  hari   PRAKASH ' -> 'Hari Prakash'"""
    return " ".join(name.split()).title()


def truncate(text, max_length=20):
    """Cut long text and add '...' at the end."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def format_list(items, separator=", "):
    """['a', 'b', 'c'] -> 'a, b, c'"""
    return separator.join(str(item) for item in items)


def format_file_size(size_in_bytes):
    """2048 -> 2.0 KB"""
    size = float(size_in_bytes)
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


if __name__ == "__main__":
    print(format_currency(1234.5))
    print(format_percent(0.256))
    print(format_number(1234567))
    print(format_date("2026-10-27"))
    print(format_phone("9876543210"))
    print(format_name("  hari   PRAKASH "))
    print(truncate("This is a very long sentence", 15))
    print(format_list(["a", "b", "c"]))
    print(format_file_size(2048))
