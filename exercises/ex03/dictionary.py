"""This is my dictionary functions"""

__author__ = "730678802"


def invert(original: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}

    for key in original:
        values = original[key]
        if original[key] in result:
            raise KeyError("message")
        else:
            result[values] = key
    return result


def count(number: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    i = 0

    if i < len(number):
        item = number[1]

        if item in result:
            result[item] += 1
        else:
            result[item] = 1

        i += 1

    return result


def favorite_color(color: dict[str, str]) -> str:
    color_list: list[str] = []

    for key in color:
        color_list.append(color[key])
    color_count: dict[str, int] = count(color_list)
    for key_color in color_count:
        value: int = color_count[key_color]
        max = 0
        popular_color: str = ""
        if value > max:
            max = value
            popular_color = key_color
    return popular_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = set([word])
    return result
