from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode missing tag")
        elif self.children == None:
            raise ValueError("ParentNode missing children")
        else:
            if len(self.children) <= 0:
                return ""
            
            children_html = ""
            for child in self.children:
                children_html += f"{child.to_html()}"
        
            if isinstance(self.props, dict):
                return f"<{self.tag} {self.props_to_html()}>" + children_html + f"</{self.tag}>"
            else:
                return f"<{self.tag}>" + children_html + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    