from typing import TYPE_CHECKING, List, Tuple

from prompt_toolkit.styles.pygments import pygments_token_to_classname

from .base import StyleAndTextTuples

if TYPE_CHECKING:
    from pygments.token import Token

__all__ = [
    "PygmentsTokens",
]


class PygmentsTokens:
    """
    Turn a pygments token list into a list of prompt_toolkit text fragments
    (``(style_str, text)`` tuples).
    """

    def __init__(self, token_list: List[Tuple["Token", str]]) -> None:
        self.token_list = token_list

    def __pt_formatted_text__(self) -> StyleAndTextTuples:
        return [
            (f"class:{pygments_token_to_classname(token)}", text)
            for token, text in self.token_list
        ]
