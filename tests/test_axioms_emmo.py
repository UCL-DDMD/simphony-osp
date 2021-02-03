"""Test the API with the EMMO ontology."""

import unittest2 as unittest

try:
    from osp.core.namespaces import math
except ImportError:
    from osp.core.ontology import Parser
    from osp.core.namespaces import _namespace_registry
    Parser(_namespace_registry._graph).parse("emmo")
    _namespace_registry.update_namespaces()
    math = _namespace_registry.math


class TestRestrictionsEmmo(unittest.TestCase):
    """Test the restrictions in EMMO ontology."""

    def test_emmo_datatypes(self):
        """Test for classes Integer, Boolean, .. in EMMO."""
        for r in math.Integer.axioms:
            print(r)  # TODO finish tests


if __name__ == "__main__":
    unittest.main()
