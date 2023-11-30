"""ASCII art images for Hangman-CLI game."""


def ascii_images() -> tuple[str, ...]:
    """Return a tuple of hangman (ascii) drawings."""
    return (
        r"""






=====""",

        r"""
    +
    |
    |
    |
    |
    |
=====""",

        r"""
 +--+
    |
    |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",

        r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""
    )
