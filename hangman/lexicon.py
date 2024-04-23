"""Word lists for Hangman-CLI game.

The _LEXICON_DICT dictionary has string values that can be split into lists.
This makes it much easier to add more lists, but the downside is that we can
only have single word puzzles.

When we fetch a word list for a specific category, we get a named tuple
called Lexicon, which contains the word list itself, and the singular form
of the category including the appropriate indefinite article.
For example, for the category "countries", we get a list of countries
and the string "a country".

This module also contains help text.
"""

from collections import namedtuple
from pathlib import Path


def is_valid_word_list(file_name: Path, max_bytes_to_read=1024) -> str:
    """Return encoding: str if file looks like a language dictionary
    else return empty string."""
    encodings = ['utf-8', 'latin-1']
    for enc in encodings:
        try:
            with open(file_name, 'r', encoding=enc) as file:
                content = file.read(max_bytes_to_read)
                lines = content.splitlines()  # Split content into lines

                # Check for one word per line within the read content
                for line in lines:
                    if len(line.split()) != 1:
                        return ''
                    for char in line:
                        if not char.isalpha() and char != "'":
                            return ''
                return enc
        except UnicodeDecodeError:
            # Try next encoding
            continue
    return ''


def get_system_dictionary(min_len: int = 3) -> list[str] | None:
    """Return list of words or None."""
    files = ("/usr/share/dict/words",
             "/usr/dict/words",
             "/usr/lib/dict/words")
    enc = ''
    lang_dict = None
    for file in files:
        lang_dict = Path(file)
        if lang_dict.is_file():
            enc = is_valid_word_list(Path(file))
            break
    if lang_dict:
        with open(lang_dict, 'r', encoding=enc) as fp:
            word_list = [line.strip() for line in fp.readlines()
                         if "'" not in line and
                         min_len <= len(line.strip())]
            return word_list
    else:
        return None


_SYSTEM_WORDS: list[str] | None = get_system_dictionary()

_LEXICON_DICT = {
    'animals': """
    Dog Cat Elephant Lion Tiger Giraffe Zebra Bear Koala
    Panda Kangaroo Penguin Dolphin Eagle Owl Fox Wolf Cheetah
    Leopard Jaguar Horse Cow Pig Sheep Goat Chicken Duck Goose
    Swan Octopus Shark Whale Platypus Chimpanzee Gorilla Orangutan
    Baboon Raccoon Squirrel Bat Hedgehog Armadillo Sloth Porcupine
    Anteater Camel Dingo Kangaroo Rat Lemur Meerkat Ocelot Parrot
    Quokka Vulture Wombat Yak Iguana jaguar Kakapo Lemming
    Manatee Nutria Ostrich Pangolin Quail Rhinoceros Serval
    Wallaby Coypu Tapir Pheasant beaver frog mongoose Anaconda
    """,

    'dinosaurs': """
    Tyrannosaurus Velociraptor Triceratops
    Stegosaurus Brachiosaurus Spinosaurus Pterodactyl Allosaurus
    Diplodocus Ankylosaurus Parasaurolophus Brontosaurus Apatosaurus
    Iguanodon Pachycephalosaurus Carnotaurus Deinonychus Archaeopteryx
    Dilophosaurus Edmontosaurus Giganotosaurus Oviraptor Troodon
    Baryonyx Corythosaurus Compsognathus Maiasaura Euoplocephalus
    Protoceratops Gallimimus Plateosaurus Sauropelta Coelophysis
    Stegoceras Suchomimus Heterodontosaurus Microraptor Therizinosaurus
    Micropachycephalosaurus Nodosaurus Ouranosaurus Quetzalcoatlus
    Shunosaurus Sinornithosaurus Styracosaurus Tsintaosaurus
    Yangchuanosaurus Zalmoxes Amargasaurus Camarasaurus Dryosaurus
    Einiosaurus Europasaurus Fukuiraptor Gasosaurus Hadrosaurus
    Hypsilophodon Jobaria Kentrosaurus Lambeosaurus Leaellynasaura
    Leptoceratops Lophorhothon Magyarosaurus Megalosaurus Minmi
    Monolophosaurus Nqwebasaurus Nipponosaurus Ornithomimus
    Pachyrhinosaurus Pentaceratops Psittacosaurus Saurolophus Segisaurus
    Siamosaurus Sordes Struthiomimus Talarurus Thescelosaurus Torosaurus
    Tsintaosaurus Tyrannotitan Utahraptor Wuerhosaurus Xenoceratops
    Yandusaurus Yimenosaurus Zuniceratops Einiosaurus Sinosauropteryx
    Iberomesornis Dacentrurus Beipiaosaurus Prenocephale Dromaeosaurus
    Othnielia Nanosaurus
    """,

    'flowers': """
    Primrose Lily Honeysuckle Rose Cherry Elder Cornflower Foxglove Columbine
    Daisy Gorse Bramble Poppy Parsley Garlic Bluebell crocus hyacinth snowdrop
    Thistle Celandine Cowslip Heather dandelion daffodil tulip wallflower
    campion buttercup orchid Yarrow Speedwell Chickweed Groundsel Delphinium
    Geranium Hollyhock Anemone lavender Peony violet Narcissus Iris allium
    """,

    'trees': """
    Oak Maple Pine Cedar Birch Spruce Ash Elm Cherry Willow Beech Fir
    Sycamore Redwood Sequoia Cypress Mahogany Chestnut Aspen Larch Poplar
    Hemlock Eucalyptus Gingko Alder Cottonwood Yew Walnut Apple Pear
    Plum Lemon Orange Olive Almond Pecan Hickory Mulberry Avocado Persimmon
    Fig Dogwood Banyan Hazelnut Kauri Baobab Palm Rowan Blackthorn
    sugarplum Crabapple Hornbeam Catalpa Hawthorn Maple Pineapple Guava
    Birch Avocado Pecan Hickory Mulberry Persimmon Dogwood Banyan
    """,

    'hard words': """
    abruptly absurd abyss affix askew avenue awkward
    axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz
    blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon
    buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet
    crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves
    embezzle equip espionage euouae exodus faking fishhook fixable fjord
    flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia
    funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly
    gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox
    injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy
    jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy
    jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch
    kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis
    matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays
    numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel
    pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips
    quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw
    schnapps scratch shiv snazzy sphinx spritz squawk staff strength
    strengths stretch stronghold stymied subway swivel syndrome thriftless
    thumbscrew topaz transcript transgress transplant triphthong twelfth
    twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo
    vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy
    whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch
    wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag
    zigzagging zilch zipper zodiac zombie
    """,

    'countries': """
    Afghanistan Albania Algeria Andorra Angola Antigua Argentina
    Armenia Australia Austria Azerbaijan Bahamas Bahrain Bangladesh
    Barbados Belarus Belgium Belize Benin Bhutan Bolivia Bosnia
    Botswana Brazil Brunei Bulgaria Burundi Cambodia Cameroon
    Canada Chad Chile China Colombia Comoros Congo Croatia Cuba
    Cyprus Denmark Djibouti Dominica Ecuador Egypt Eritrea Estonia
    Eswatini Ethiopia Fiji Finland France Gabon Gambia Georgia
    Germany Ghana Greece Grenada Guatemala Guinea Guyana Haiti
    Honduras Hungary Iceland India Indonesia Iran Iraq Ireland
    Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Kiribati
    Korea Kosovo Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho
    Liberia Libya Liechtenstein Lithuania Luxembourg Madagascar
    Malawi Malaysia Maldives Mali Malta Mauritania Mauritius Mexico
    Micronesia Moldova Monaco Mongolia Montenegro Morocco Mozambique
    Myanmar Namibia Nauru Nepal Netherlands Nicaragua Niger Nigeria
    Macedonia Norway Oman Pakistan Palau Palestine Panama Paraguay
    Peru Philippines Poland Portugal Qatar Romania Russia Rwanda
    Samoa Senegal Serbia Seychelles Singapore Slovakia Slovenia Somalia
    Spain Sudan Suriname Sweden Switzerland Syria Taiwan Tajikistan
    Tanzania Thailand Togo Tonga Trinidad Tunisia Turkey Turkmenistan
    Tuvalu Uganda Ukraine USA Uruguay England Ireland Scotland Uzbekistan
    Vanuatu Venezuela Vietnam Yemen Zambia Zimbabwe
    """
}


def _get_words_of_length(words, min_length, max_length) -> list[str]:
    """Return words from language dictionary in length range."""
    return [word.upper() for word in words
            if min_length <= len(word) <= max_length]


Lexicon = namedtuple('Lexicon', ['word_list', 'singular'])

lexicon_dict = {}
if _SYSTEM_WORDS is not None:
    lexicon_dict = {
        'short words': Lexicon(_get_words_of_length(_SYSTEM_WORDS, 3, 5),
                               singular='a short word'),
        'medium length words': Lexicon(
            _get_words_of_length(_SYSTEM_WORDS, 5, 8),
            singular='a medium length word'),
        'long words': Lexicon(_get_words_of_length(_SYSTEM_WORDS, 8, 50),
                              singular='a long word'),
    }


def _get_word_list(category: str = 'animals') -> list[str]:
    """Return a list of words."""
    category = category.lower()
    try:
        words: str = _LEXICON_DICT[category]
        return [word.upper() for word in words.split()]
    except KeyError as exc:
        raise ValueError("Invalid category.") from exc


# Category words
lexicon_dict.update({
    'animals': Lexicon(word_list=_get_word_list('animals'),
                       singular='an animal'),
    'dinosaurs': Lexicon(word_list=_get_word_list('dinosaurs'),
                         singular='a dinosaur'),
    'flowers': Lexicon(word_list=_get_word_list('flowers'),
                       singular='a flower'),
    'trees': Lexicon(word_list=_get_word_list('trees'),
                     singular='a tree'),
    'countries': Lexicon(word_list=_get_word_list('countries'),
                         singular='a country'),
    'hard words': Lexicon(word_list=_get_word_list('hard words'),
                          singular='a hard word'),
})


HELP_TEXT = """
How to Play
===========

1. Enter your name when prompted.
2. Select a category when prompted.
3. The computer will think of a secret word
   and tell you how many letters are in the word.
4. Make guesses one letter at a time to guess
   the secret word.
5. If you think that you know the word, you may
   guess the entire word.
6. Each time you guess a letter, all occurrences
   of that letter in the word will be shown.
7. If your guess is incorrect, a part of the hangman
   figure will be drawn.
8. Continue guessing letters to reveal the entire word.
9. You may quit at any time by pressing "Ctrl + C".
10.To view the help menu, enter a question mark '?'.
"""
