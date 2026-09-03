import unittest

class TestCompatibilityShim(unittest.TestCase):
    def test_import_tapevision_enricher(self):
        import tapevision_enricher
        self.assertTrue(hasattr(tapevision_enricher, "run_enrichment_pipeline"))
        self.assertTrue(hasattr(tapevision_enricher, "parse_cvat_xml"))

    def test_import_tapevision_enricher_submodules(self):
        from tapevision_enricher.config import DEFAULT_CONFIG
        self.assertIn("output", DEFAULT_CONFIG)

        from tapevision_enricher.models import Track
        self.assertTrue(callable(Track))

        from tapevision_enricher.writers import write_play_annotation_json, write_tapevision_json
        self.assertIs(write_play_annotation_json, write_tapevision_json)

        from tapevision_enricher.cli import parse_args
        self.assertTrue(callable(parse_args))

if __name__ == "__main__":
    unittest.main()
