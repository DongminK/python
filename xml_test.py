from xml.etree.ElementTree import Element, dump, SubElement, ElementTree

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"

dummy = Element("dummy")
dummy.text = "DUM"
note.insert(1, dummy)
note.insert(2, dummy)

dump(note)

ElementTree(note).write("note.xml")


a = "TEST"
b = 123
print(a.encode("utf-8"))
