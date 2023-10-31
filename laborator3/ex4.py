def build_xml_element(tag, content, **kwargs):

    element = f"<{tag}"

    for key, value in kwargs.items():
        element += f' {key}="{value}"'

    element += f">{content}"

    element += f"</{tag}>"

    return element

# Example usage:
xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)
