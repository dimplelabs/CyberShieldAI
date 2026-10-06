import unittest
from backend.security_scanner import scan_text

class SecurityScannerTests(unittest.TestCase):
    def test_detects_xss(self):
        self.assertTrue(any(x['category']=='XSS' for x in scan_text('<script>alert(1)</script>')['findings']))
    def test_clean_text(self):
        self.assertEqual(scan_text('hello safe world')['risk_level'],'Low Risk')

if __name__ == '__main__': unittest.main()
