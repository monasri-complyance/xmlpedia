import xml.etree.ElementTree as ET


def get_tag(tag):
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def get_namespace(tag):
    if "}" not in tag:
        return ""

    raw_namespace, _ = tag.split("}", 1)

    # remove the first starting bracket 
    return raw_namespace[1:]


def get_value(element):
    return (element.text or "").strip()


def get_attributes(element):
    return {
        get_tag(key): value
        for key, value in element.attrib.items()
    }


def get_children(element):
    return [
        build_tree(child)
        for child in element
    ]


def build_tree(element):

    node = {
        "tag": get_tag(element.tag),

        "namespace": get_namespace(element.tag),

        "value": get_value(element),

        "attributes": get_attributes(element),

        "children": []
    }


    node["children"] = get_children(element)

    return node


def parse_xml(data):

    root = ET.fromstring(data)

    return {
        "document_type": get_tag(root.tag),

        "tree": build_tree(root)
    }
    