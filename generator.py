import hashlib


def md5_hash(path):
    m = hashlib.md5()

    with open(path, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            m.update(line.encode('utf-8'))
            yield m.hexdigest()


generator = md5_hash('links_file.txt')

for item in generator:
    print(item)
