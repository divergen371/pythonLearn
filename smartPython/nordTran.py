import ast

class ReplaceBinOp(ast.NodeTransformer):
    """二項演算を加算に置き換える"""
    def visit_BinOp(self, node):
        return ast.BinOp(left=node.left,
                         op=ast.Add(),
                         right=node.right)

tree = ast.parse("x = 1/3")
ast.fix_missing_locations(tree)
eval(compile(tree, '', 'exec'))
print(ast.dump(tree))
print(x)

tree = ReplaceBinOp().visit(tree)
ast.fix_missing_locations(tree)
print(ast.dump(tree))
eval(compile(tree, '', 'exec'))
print(x)