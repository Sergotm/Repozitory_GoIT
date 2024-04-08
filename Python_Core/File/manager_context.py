class FileWrite:
    def __init__(self, filename) -> None:
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            self.opened = False

if __name__ == '__main__':
    with FileWrite(filename='Python_Core\\File\\new_file.txt') as f:
        f.write('Hello world\n')
        f.write('Happy end\n')