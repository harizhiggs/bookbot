def count_words(script) -> int:
    words = script.split()
    return len(words)

def count_characters(script) -> dict[str, int]:
    characters = {}

    text = script.lower()
    
    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def sort_on(character: tuple[str, int]) -> int:
    return character[1]

def chars_dict_to_sorted_list(character_dict: dict[str, int]) -> list[tuple[str, int]]:
    cl = list(character_dict.items())
    scl = sorted(cl, reverse=True, key=sort_on)
    return scl

