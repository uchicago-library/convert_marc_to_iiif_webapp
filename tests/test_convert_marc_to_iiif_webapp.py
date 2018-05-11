import unittest
import convert_marc_to_iiif_webapp


class Tests(unittest.TestCase):
    def setUp(self):
        # Perform any setup that should occur
        # before every test
        pass

    def tearDown(self):
        # Perform any tear down that should
        # occur after every test
        pass

    def testPass(self):
        self.assertEqual(True, True)

    def testVersionAvailable(self):
        x = getattr(convert_marc_to_iiif_webapp, "__version__", None)
        self.assertTrue(x is not None)


if __name__ == "__main__":
    unittest.main()
