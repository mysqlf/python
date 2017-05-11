from lxml import etree
html = """
    <div>hellos
        <p>H</p>
</div>
<div>hehe</div>
    <div>hello
        <p>E</p>
</div>
<div>hehe</div>
"""
sel = etree.HTML(html)
print(sel)
con = sel.xpath('//div/p/text()')  # [text()="hello"]
print(type(con))
print(len(con))
print(con[0])
# H
