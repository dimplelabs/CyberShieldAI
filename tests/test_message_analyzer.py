import unittest
from backend.message_analyzer import analyze_message

class MessageAnalyzerTests(unittest.TestCase):
    def test_otp_phishing(self):
        out=analyze_message('Urgent! Send me your OTP and click https://example.com')
        self.assertEqual(out['risk_level'],'High Risk')
        self.assertIn('OTP request',out['indicators'])
        self.assertIn('Phishing/link',out['indicators'])

if __name__ == '__main__': unittest.main()
