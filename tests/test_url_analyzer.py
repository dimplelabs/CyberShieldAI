import unittest
from backend.url_analyzer import analyze_url

class URLAnalyzerTests(unittest.TestCase):
    def test_http_is_flagged(self):
        out=analyze_url('http://example.com')
        self.assertIn(out['risk_level'], {'Low Risk','Suspicious'})
    def test_ip_and_http_raise_risk(self):
        out=analyze_url('http://192.168.1.1/login')
        self.assertIn(out['risk_level'], {'Suspicious','High Risk'})
        self.assertTrue(any('IP address' in x for x in out['indicators']))

if __name__ == '__main__': unittest.main()
