#Task 1

class FileContextManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.f = None
        self.counter = 0

    def __enter__(self):
        self.counter += 1
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        if self.counter == 0:
            self.f.close()
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with value {exc_value}")
        return False

with FileContextManager("example.txt", "w") as f:
    f.write("Hello, world!")

with FileContextManager("example.txt", "r") as f:
    content = f.read()
    print(content)

#Task 2

import pytest

@pytest.fixture
def create_file_with_content():
    fname = "test_file.txt"
    with FileContextManager(fname, "w") as file:
        file.write("Test content")
    yield fname
    import os
    if os.path.exists(fname):
        os.remove(fname)

def test_file_read(create_file_with_content):
    fname = create_file_with_content
    with FileContextManager(fname, "r") as f:
        content = f.read()
        assert content == "Test content"

def test_file_write(create_file_with_content):
    filename = create_file_with_content
    with FileContextManager(filename, "w") as f:
        f.write("Updated content")

    with FileContextManager(filename, "r") as f:
        content = f.read()
        assert content == "Updated content"

def test_multiple_instances(create_file_with_content):
    filename = create_file_with_content
    with FileContextManager(filename, "w") as f1:
        f1.write("Content from file1")

    with FileContextManager(filename, "w") as f2:
        f2.write("Content from file2")

    with FileContextManager(filename, "r") as f3:
        content = f3.read()
        assert content == "Content from file2"

def test_exception_handling():
    with pytest.raises(ValueError):
        with FileContextManager("non_existent_file.txt", "r") as f:
            content = f.read()

print(1)