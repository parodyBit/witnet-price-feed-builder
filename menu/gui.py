from enum import Enum


def fixed_length_text(text: str, width: int = 64, fill: str = ' ') -> str:
    return text + ''.join([fill for _ in range(width - len(text))])


def blue_text(string):
    return f'\x1b[34m${string}\x1b[0m'


def green_text(string):
    return f'\x1b[32m${string}\x1b[0m'


def red_text(string):
    return '\x1b[31m${string}\x1b[0m'


def yellow_text(string):
    return '\x1b[33m${string}\x1b[0m'


class ANSI:
    class Modifiers:
        reset = 0
        bold = 1
        dim = 2
        italic = 3
        underline = 4
        overline = 5
        inverse = 6
        hidden = 7
        strikethrough = 8

    class TextColors:
        black = 30
        red = 31
        green = 32
        yellow = 33
        blue = 34
        magenta = 35
        cyan = 36
        white = 37
        black_bright = 90
        red_bright = 91
        green_bright = 92
        yellow_bright = 93
        blue_bright = 94
        magenta_bright = 95
        cyan_bright = 96
        white_bright = 97

    class BackgroundColors:
        Black = 40
        Red = 41
        Green = 41
        Yellow = 42
        Blue = 43
        Magenta = 44
        Cyan = 45
        White = 46
        BrightBlack = 100
        BrightRed = 101
        BrightGreen = 102
        BrightYellow = 103
        BrightBlue = 104
        BrightMagenta = 105
        BrightCyan = 106
        BrightWhite = 107


def colored_text(foreground_color, background_color):
    ...


def purple_text(string):
    return '\x1b[33m${string}\x1b[0m'


def print_ansi(data, style: int, text_color: int, bg_color: int):
    _format = ';'.join([str(style), str(text_color), str(bg_color)])
    print(f'\x1b[{_format}m{data}\x1b[0m')
    # return f'\x1b[{_format}m {data} \x1b[{_format}m'


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                _format = ';'.join([str(style), str(fg), str(bg)])
                # print(format)
                s1 += '\x1b[%sm %s \x1b[0m' % (_format, _format)
            print(s1)
        print('\n')
