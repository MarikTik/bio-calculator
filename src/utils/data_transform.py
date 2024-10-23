from typing import List, Dict, Any
import re


def stringify(data: List[str]) -> str:
    """Attaches a list of strings with potential spaces into a single string
    
    Args:
        data (List[str]): A list containing strings that should be attached
    
    Returns:
        str: A single string composed of all the characters of individual strings joined together
    """
    return "".join(data).replace(" ", "")

def simplify_string(string: str) -> str:
    """Extracts a string without descriptions

    Args:
        string (str): A string containing descriptions in () parantheses

    Returns:
        str: The part of a string without descriptions
    """
    match = re.match(r"^(.*?)\s*\(.*\)$", string)
    return match.group(1) if match else string

def simplify_dictionary(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts a dictionary without descriptions

    Args:
        dictionary (Dict[str, Any]): A dictionary containing descriptions in values

    Returns:
        Dict[str, str]: A dictionary with values without descriptions
    """
    return {simplify_string(key): value for key, value in dictionary.items()}