class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head
        "korea"
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
                print(current_node.data)
            else:
                return False

        if current_node.data:
            return True
        else:
            return False


    def search_with_check_iscontain(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
                if current_node.data != None:
                    if current_node.data != string:
                        return False # "NO"

        return True


    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words






import heapq as hq

num_loop = int(input())

for _ in range(num_loop):
    len_numbers = int(input())

    numbers = Trie()
    numbers_list = []
    for _ in range(len_numbers):
        number = input()
        numbers.insert(number)
        numbers_list.append(number)


    answer = True
    for number in numbers_list:
        if numbers.search_with_check_iscontain(number) == False:
            answer = False
            break
    answer = "YES" if answer == True else "NO"
    print(answer)

