from unittest import IsolatedAsyncioTestCase

import artdex_indexer


class ExampleTest(IsolatedAsyncioTestCase):
    async def test_example(self):
        assert artdex_indexer