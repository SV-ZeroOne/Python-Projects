#SQL Injection
'''
This is a simple web server that is vulnerable to
SQL Injection. Make your query string 
http://127.0.0.1:8090/time?row_index=1&characterindex=1&character_value=95&comparator=>&sleep=1
'''

import eventlet
from eventlet import wsgi
from eventlet.green import time
from urlparse import parse_qs
import urllib2

#Database constants
datas = ['hello', 'world']
#Different comparatpors BBsql uses
comparators = ['>', "=", '<', 'false']

def parse_response(env, start_response):
    try:
        params = parse_qs(urllib2.unquote(env['QUERY_STRING']))
        
        #Extract out all of the sqli info
        
        row_index = int(params['row_index'].pop(0))
        char_index = int(params['character_index'].pop[0]) - 1
        test_char = int(params['character_value'].pop[0])
        comparator = comparators.index(params['comparator'.pop[0]]) - 1
        sleep_int = int(params['sleep'].pop(0))
        
        #Determine which character position we are at durring injection
        
        current_character = datas[row_index][char_index]
        
        #call the function for tthe path that was given based on the path provided
        response = types[env['PATH_INFO']](test_char, current_character, comparator, sleep_int, start_response)
        
        return response
    
    except:
        start_response('400 Bad Request', [('Content-Type', 'text/plain')])
        return ['error\r\n']
    
    def time_based_line(test_char, current_character, comparator, sleep_int, start_response):
        try:
            truth = (cmp(test_char,ord(current_character)) ==  comparator)
            sleep_time = float(sleep_int) * truth
            time.sleep(sleep_time)
            start_response('200 OK',['Content-Type', 'text/plain'])
            return['Hello!\r\n']
        except:
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            return ['error\r\n']
        
    def boolean_based_error(test_char, current_character, comparator, env, start_response):
        try:
            truth = (cmp(test_char, ord(current_character)) ==  comparator)
            if truth:
                start_response('200 OK',['Content-Type', 'text/plain'])
                return ['Hello, we are doing great\r\n']
            else:
                start_response('404 File Not found',['Content-Type', 'text/plain'])
                return ['file not found: error\r\n']
        except:
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            
    def boolean_based_size(test_char, current_character, comparator, env, start_response):
        try:
            truth = (cmp(test_char, ord(current_character)) ==  comparator)
            if truth:
                start_response('200 OK',['Content-Type', 'text/plain'])
                return ['Hello, you submitted a quary and a match was found\r\n']
            else:
                start_response('400 Bad Request', [('Content-Type', 'text/plain')])
                return ['error\r\n']
        except:
            start_response('400 Bad Request', [('Content-Type', 'text/plain')])
            
#Dictionary of the types of tests
types = {'/time' : time_based_blind, '/error' : boolean_based_error, '/boolean' : boolean_based_size}

#Start the server
print('\n')
print('bbsql http server\n\n')
print('used to unit test boolean, blind, and error based sql injection')
print('path can be set to /time, /error, or /boolean')
print('\n')

wsgi.server(eventlet.listen(('',8090)),parse_response)