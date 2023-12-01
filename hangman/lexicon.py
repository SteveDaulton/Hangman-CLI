"""Word lists for Hangman-CLI game."""


def get_word_list(category: str = 'animals') -> list[str]:
    """Return a list of quiz words.

    Define your list of words here.
    Words must be separated by white-space only.
    Each word list must have a unique name, and have an
    entry in the word_list_dict.

    Parameters
    ----------
    category: str
        Types of words, default: "animals"

    Returns
    -------
    list[str]
        List of words of selected category

    Raises
    ------
    ValueError
        If 'category' invalid.
    """

    category = category.lower()

    animal_words = """
    Dog Cat Elephant Lion Tiger Giraffe Zebra Bear Koala
    Panda Kangaroo Penguin Dolphin Eagle Owl Fox Wolf Cheetah
    Leopard Jaguar Horse Cow Pig Sheep Goat Chicken Duck Goose
    Swan Octopus Shark Whale Platypus Chimpanzee Gorilla Orangutan
    Baboon Raccoon Squirrel Bat Hedgehog Armadillo Sloth Porcupine
    Anteater Camel Dingo Kangaroo Rat Lemur Meerkat Ocelot Parrot
    Quokka Vulture Wombat Yak Iguana jaguar Kakapo Lemming
    Manatee Nutria Ostrich Pangolin Quail Rhinoceros Serval
    Wallaby Coypu Tapir Pheasant
    """

    dinosaur_words = """
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
    """

    flower_words = """
    Primrose Lily Honeysuckle Rose Cherry Elder Cornflower Foxglove Columbine
    Daisy Gorse Bramble Poppy Parsley Garlic Bluebell crocus hyacinth snowdrop
    Thistle Celandine Cowslip Heather dandelion daffodil tulip wallflower
    campion buttercup orchid Yarrow Speedwell Chickweed Groundsel Delphinium
    Geranium Hollyhock Anemone lavender Peony violet Narcissus Iris allium
    """

    word_list_dict = {'animals': animal_words,
                      'dinosaurs': dinosaur_words,
                      'flowers': flower_words}

    try:
        words: str = word_list_dict[category]
        return [word.upper() for word in words.split()]
    except KeyError as exc:
        raise ValueError("Invalid category.") from exc
