import sys
import unittest
from unittest.mock import patch

from play_annotation_generator.cli import parse_args, main


class TestBatchCLI(unittest.TestCase):

    def test_batch_subcommand_parsing(self):
        test_args = [
            "cli.py",
            "batch-generate-and-enrich",
            "--gt-dir", "tracking_outputs",
            "--template", "docs/UniversalTemplate.xml",
            "--key-actions", "KeyActions_Sheet.csv",
            "--player-tracks", "PlayerTrack_ID_Sheet.csv",
            "--output", "outputs/batch",
            "--limit", "5",
            "--play", "JetSweep",
            "--skip-existing",
            "--review"
        ]

        with patch.object(sys, "argv", test_args):
            args = parse_args()
            self.assertEqual(args.command, "batch-generate-and-enrich")
            self.assertEqual(args.gt_dir, "tracking_outputs")
            self.assertEqual(args.template, "docs/UniversalTemplate.xml")
            self.assertEqual(args.key_actions, "KeyActions_Sheet.csv")
            self.assertEqual(args.player_tracks, "PlayerTrack_ID_Sheet.csv")
            self.assertEqual(args.output, "outputs/batch")
            self.assertEqual(args.limit, 5)
            self.assertEqual(args.play, "JetSweep")
            self.assertTrue(args.skip_existing)
            self.assertFalse(args.overwrite)
            self.assertTrue(args.review)


if __name__ == "__main__":
    unittest.main()
