"""Word lists for Hangman-CLI game."""


_WORD_LISTS = {
    'animals': """
    Dog Cat Elephant Lion Tiger Giraffe Zebra Bear Koala
    Panda Kangaroo Penguin Dolphin Eagle Owl Fox Wolf Cheetah
    Leopard Jaguar Horse Cow Pig Sheep Goat Chicken Duck Goose
    Swan Octopus Shark Whale Platypus Chimpanzee Gorilla Orangutan
    Baboon Raccoon Squirrel Bat Hedgehog Armadillo Sloth Porcupine
    Anteater Camel Dingo Kangaroo Rat Lemur Meerkat Ocelot Parrot
    Quokka Vulture Wombat Yak Iguana jaguar Kakapo Lemming
    Manatee Nutria Ostrich Pangolin Quail Rhinoceros Serval
    Wallaby Coypu Tapir Pheasant
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

    'hard words': """abruptly absurd abyss affix askew avenue awkward
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
"""
}


def get_word_list(category: str = 'animals') -> list[str]:
    """Return a list of words."""
    category = category.lower()

    try:
        words: str = _WORD_LISTS[category]
        return [word.upper() for word in words.split()]
    except KeyError as exc:
        raise ValueError("Invalid category.") from exc


def get_categories():
    """Return a tuple of word categories."""
    return tuple(_WORD_LISTS.keys())
