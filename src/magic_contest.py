from leaf_fairy import LeafFairy
from mermaid_fairy import MermaidFairy

if __name__ == "__main__":
    leaf_fairy = LeafFairy()
    mermaid_fairy = MermaidFairy()
    player_list = [leaf_fairy, mermaid_fairy]

    for player in player_list:
        player.do_magic("sea horse")
        unique_type = player.get_unique_type()
        print(f"{unique_type}")
        magic_type_list = player.get_magic_type_list()
        for magic_type in magic_type_list:
            print(f"{magic_type}")
        print(f"{player.name}")
