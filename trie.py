from hashed_file import HashedFile


class TrieNode:

    def __init__(self):
        self.children = {}
        self.files = set()


class Trie:

    def __init__(self, splitting_method):
        self.root = TrieNode()
        self.splitting_method = splitting_method
        self.empty_files = set()

    def add_file(self, hfile: HashedFile):
        node = self.root
        last_node = None
        hfile.reset()
        for chunk in self.splitting_method(hfile):
            if chunk not in node.children:
                node.children[chunk] = TrieNode()
            last_node = node
            node = node.children[chunk]
        if last_node:
            node.files.add(hfile.get_file_path())
        else:
            self.empty_files.add(hfile.get_file_path())

    def find_duplicates(self):
        duplicates = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if len(node.files) > 1:
                duplicates.append(node.files)
            for child in node.children.values():
                stack.append(child)
        if len(self.empty_files) > 1:
            duplicates.append(self.empty_files)
        return duplicates

    def print_tree(self, node=None, prefix=''):
        if node is None:
            node = self.root
        if node.files:
            print(f'{prefix}Files: {node.files}')
        for hash_chunk, child in node.children.items():
            print(f'{prefix}Chunk: {hash_chunk}')
            self.print_tree(child, prefix=prefix + '  ')
