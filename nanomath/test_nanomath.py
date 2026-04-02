import unittest
import nanomath as nm
import pandas as pd


class NanomathTest(unittest.TestCase):
    def test_ave_qual(self):
        """Test average quality calculation."""
        quals = list(range(128 + 1)) * 100
        mq = nm.ave_qual(quals, qround=True)
        self.assertEqual(mq, 14)

    def test_ultralong_stats(self):
        """Test ultralong read count and read/base percentages."""
        df = pd.DataFrame({"lengths": [50, 1000, 1500, 5000, 10000]})
        stats = nm.Stats(df, ultralong=1500)
        self.assertEqual(stats.number_of_ultralong_reads, 3)
        # Check ultralong stats tuple (count, bases)
        self.assertEqual(len(stats._ultralong_stats), 2)
        self.assertEqual(stats._ultralong_stats[0], 3)
        self.assertEqual(stats._ultralong_stats[1], 16500)
        # Test formatted output
        stats.long_features_as_string()
        self.assertIn("(60.0%)", stats.ultralong_reads)
        self.assertEqual(stats.ultralong_bases, "0.0Mb (94.0%)")


if __name__ == '__main__':
    unittest.main()
