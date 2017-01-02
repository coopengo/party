from lxml import etree

countries = ('fr', 'be', 'it', 'mc', 'es', 'ch', 'gb', 'us')


def troncate_records():
    to_remove = []
    with open('address.xml', 'r') as f:
        tree = etree.parse(f)
    for element in tree.xpath("//record[@model='party.address.format']"):
        if element.attrib['id'][-2:] not in countries:
            to_remove.append(element)
    for element in to_remove:
        element.getparent().remove(element)
    with open('address.xml', 'w') as f:
        f.write('<?xml version="1.0"?>\n')
        tree.write(f, pretty_print=True, encoding='utf-8')


if __name__ == '__main__':
    troncate_records()
