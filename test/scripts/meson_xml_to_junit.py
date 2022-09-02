#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET


def main(infile, outfile):
    tree = ET.parse(infile)
    root = tree.getroot()
    for tsuite in root:
        for tcase in tsuite:
            failure = tcase.find('failure')

            if failure is not None:
                error = tcase.find('system-err')
                failure.text = error.text


    with open(outfile, 'wb') as outfd:
        outfd.write(ET.tostring(root, xml_declaration=True, encoding='UTF-8'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
