
class FileNode():

    def __init__(self, name, data):
        self.name = name
        self.children = []
        self.data = data

    def mkdir(self, path):
        if "." in path:
            print("Folder cannot have extension")
            return

        item = path[1:].split("/")

        if len(item) == 1:
            self.children.append(FileNode(item[0], None))
            print(item[0] + " created")
            return

        found = False
        for child in self.children:
            if child.name == item[0]:
                found = True
                child.mkdir("/" + "/".join(item[1:]))
                break

        if not found:
            print("Invalid path")

    def write_file(self, path, data):
        if "." not in path:
            print("Filename needs to have extension")
            return

        item = path[1:].split("/")

        if len(item) == 1:
            self.children.append(FileNode(item[0], data))
            print(item[0] + " created")
            return

        found = False
        for child in self.children:
            if child.name == item[0] and "." not in child.name:
                found = True
                child.write_file("/" + "/".join(item[1:]), data)
                break

        if not found:
            print("Invalid path")

    def read_file(self, path):

        if "." not in path:
            print("Filename needs to have extension")
            return

        item = path[1:].split("/")

        if len(item) == 1:
            for child in self.children:
                if child.name == item[0] and "." in child.name:
                    print(child.data)
                    return

        found = False
        for child in self.children:
            if child.name == item[0] and "." not in child.name:
                found = True
                child.read_file("/" + "/".join(item[1:]))
                break

        if not found:
            print("Invalid path")


# /foo/bar
# /foo/baz
# /foo/lol/one
root = FileNode("root", None)
root.mkdir("/foo")
root.mkdir("/foo/bar")

root.write_file("/foo/test.txt", "test.txt")

root.read_file("/foo/test.txt")
root.read_file("/foo/bad.txt")

# root.write_file("/foo/test.txt/test.txt", "test.txt")
# root.mkdir("/foo")
# root.mkdir("/foo/baz/one")





