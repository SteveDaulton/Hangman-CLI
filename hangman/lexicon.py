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
    Oak Maple Pine Cedar Birch Spruce Ash Elm Cherry Willow Beech Fir Poplar
    Sycamore Redwood Sequoia Cypress Mahogany Chestnut Aspen Douglasfir Larch
    Hemlock Eucalyptus Gingko Alder Cottonwood Yew Walnut Boxelder Apple Pear
    Plum Lemon Orange Olive Almond Pecan Hickory Mulberry Avocado Persimmon
    Fig Dogwood Banyan Tuliptree Hazelnut Kauri Baobab Palm Rowan Blackthorn
    Serviceberry Crabapple Hornbeam Catalpa Hawthorn Maple Pineapple Guava
    Birch Avocado Pecan Hickory Mulberry Persimmon Dogwood Banyan Tuliptree
    Hazelnut Kauri Baobab Palm Rowan Blackthorn Serviceberry Crabapple
    Hornbeam Catalpa Hawthorn
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
