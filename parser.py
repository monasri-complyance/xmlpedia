from lxml import etree

def get_tag(tag):
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag

def get_namespace(tag):
    if "}" not in tag:
        return ""
    return tag.split("}", 1)[0][1:]

def get_value(element):
    return (element.text or "").strip()

def get_attributes(element):
    return {
        get_tag(key): value
        for key, value in element.attrib.items()
    }

def build_tree(element):
    node = {
        "tag": get_tag(element.tag),
        "full_tag": element.tag,
        "namespace": get_namespace(element.tag),
        "value": get_value(element),
        "attributes": get_attributes(element),
        "line": element.sourceline,
        "children": []
    }

    for child in element:
        node["children"].append(
            build_tree(child)
        )

    return node

def parse_xml(data):
    root = etree.fromstring(data)

    return {
        "document_type": get_tag(root.tag),
        "tree": build_tree(root),
        "xml": data.decode("utf-8-sig")
    }