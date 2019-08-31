from algo.leaf_fairy import LeafFairy
from algo.mermaid_fairy import MermaidFairy

if __name__ == "__main__":
    leaf_fairy = LeafFairy()
    mermaid_fairy = MermaidFairy()
    player_list = [leaf_fairy, mermaid_fairy]

    for player in player_list:
        player.do_magic('sea horse')
        for magic_type in player.get_magic_type():
            print(f'{magic_type}')
