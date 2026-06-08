import ast

class AsyncTokenBucketInjector(ast.NodeTransformer):
    def visit_AsyncFunctionDef(self, node):
        if node.name == 'process_webhook_payload':
            bucket_logic = ast.parse('''
async def process_webhook_payload(payload):
    import asyncio
    if not hasattr(self, "_token_bucket"):
        self._token_bucket = asyncio.Semaphore(100)
    async with self._token_bucket:
        await original_process_webhook_payload(payload)
''').body[0]
            bucket_logic.args = node.args
            bucket_logic.decorator_list = node.decorator_list
            return ast.copy_location(bucket_logic, node)
        return self.generic_visit(node)

def apply_runtime_hot_patch(source_code: str) -> str:
    tree = ast.parse(source_code)
    patched_tree = AsyncTokenBucketInjector().visit(tree)
    ast.fix_missing_locations(patched_tree)
    return ast.unparse(patched_tree)
