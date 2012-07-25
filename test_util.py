import unittest
from bson import timestamp
from util import (verify_url, 
                  bson_ts_to_long, 
                  long_to_bson_ts, 
                  retry_until_ok)
              
                  
def err_func():
    err_func.counter += 1
    if err_func.counter == 3:
        return True
    else:
        raise TypeError
    
err_func.counter = 0


class UtilTester(unittest.TestCase):
    
    def runTest(self):
        super(UtilTester, self).__init__()
        
            
    def test_verify_url(self):
        
        #Testing verify_url
        bad_url = "weofkej"
        good_url = "http://www.google.com"
        no_http_url = "www.google.com"
        good_host_bad_path = "http://www.google.com/-##4@3weo$%*"
        
        self.assertTrue(verify_url(good_url))
        
        self.assertFalse(verify_url(no_http_url))
        self.assertFalse(verify_url(bad_url))
        self.assertFalse(verify_url(good_host_bad_path))
        print 'PASSED TEST VERIFY URL'
        
    def test_bson_ts_to_long(self):
        #Testing bson_ts_to_long and long_to_bson_ts
        ts = timestamp.Timestamp(0x12345678, 0x90abcdef)
        
        self.assertEqual(0x1234567890abcdef, bson_ts_to_long(ts))
        self.assertEqual(long_to_bson_ts(0x1234567890abcdef), ts)
        print 'PASSED BSON TS TO LONG'
        
    def test_retry_until_ok(self):
        #Testing retry_until_ok
        self.assertTrue(retry_until_ok(err_func))
        self.assertEqual(err_func.counter, 3)
        print 'PASSED RETRY UNTIL OK'
        
        
if __name__ == '__main__':

    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    