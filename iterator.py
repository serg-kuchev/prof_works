import json

class Wikilink:

    def __init__(self, file_path, start):
        self.file = open(file_path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common']
        country_link_name = country.replace(' ', '_')
        link = 'https://en.wikipedia.org/wiki/' + country_link_name
        return country, link


if __name__ == '__main__':
    with open('links_file.txt', 'w', encoding='utf-8') as lf:
        for country, item in Wikilink('countries.json', -1):
            lf.write(str(country) + ' ' + str(item) + '\n')
