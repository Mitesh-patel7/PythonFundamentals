import ast

def parse_python_file(file_path):

    with open(file_path,"r",encoding="utf-8") as f:
        code = f.read()

    tree = ast.parse(code)

    functions = []
    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

    return {
        "code": code,
        "functions": functions,
        "classes": classes
    }