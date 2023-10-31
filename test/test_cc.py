import unittest
import ast
from metrics.cc import cyclomatic_complexity


class TestCyclomaticComplexity(unittest.TestCase):

    def test_simple_function(self):
        code = """
        def simple_function():
            return 42
        """
        node = ast.parse(code)
        function_node = node.body[0]
        self.assertEqual(cyclomatic_complexity(function_node), 1)

    def test_function_with_conditions(self):
        code = """
        def complex_function(x):
            if x > 10:
                return x
            elif x < 0:
                return -x
            else:
                return 0
        """
        node = ast.parse(code)
        function_node = node.body[0]
        self.assertEqual(cyclomatic_complexity(function_node), 4)


# ... additional tests

if __name__ == "__main__":
    unittest.main()
