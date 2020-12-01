#!/usr/bin/env python
'''
Author: Christopher Duffy
Date: July 2015
Name: multi_process.py
Purpose: To identify live web applications with a list of IP addresses, using parallel processes
'''

import multiprocessing, urllib2, argparse, sys, logging, datetime, time

def host_request(host):
    print("[*] Testing %s") % (str(host))
    target = "http://" + host
    target_secure = "https://" + host
    timenow = time.time()
    record = datetime.datetime.fromtimestamp(timenow).strftime('%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(record)
    try:
        request = urllib2.Request(target)
        request.get_method = lambda : 'HEAD'
        response = urllib2.urlopen(request)
        response_data = str(response.info())
        logger.debug("[*] %s" % response_data)
        response.close()
    except:
        response = None
        response_data = None
    try:
        request_secure = urllib2.urlopen(target_secure)
        request_secure.get_method = lambda : 'HEAD'
        response_secure = str(urllib2.urlopen(request_secure).read())
        response_secure_data = str(response.info())
        logger.debug("[*] %s" % response_secure_data)
        response_secure.close()
    except:
        response_secure = None
        response_secure_data = None
    if response_data != None and response_secure_data != None:
        r = "[+] Insecure webserver detected at %s reported by %s" % (target, str(multiprocessing.Process().name))
        rs = "[+] Secure webserver detected at %s reported by %s" % (target_secure, str(multiprocessing.Process().name))
        logger.debug("[+] Insecure web server detected at %s and reported by process %s" % (str(target), str(multiprocessing.Process().name)))
        logger.debug("[+] Secure web server detected at %s and reported by process %s" % (str(target_secure), str(multiprocessing.Process().name)))
        return(r, rs)
    elif response_data == None and response_secure_data == None:
        r = "[-] No insecure webserver at %s reported by %s" % (target, str(multiprocessing.Process().name))
        rs = "[-] No secure webserver at %s reported by %s" % (target_secure, str(multiprocessing.Process().name))
        logger.debug("[-] Insecure web server was not detected at %s and reported by process %s" % (str(target), str(multiprocessing.Process().name)))
        logger.debug("[-] Secure web server was not detected at %s and reported by process %s" % (str(target_secure), str(multiprocessing.Process().name)))
        return(r, rs)
    elif response_data != None and response_secure_data == None:
        r = "[+] Insecure webserver detected at %s reported by %s" % (target, str(multiprocessing.Process().name))
        rs = "[-] No secure webserver at %s reported by %s" % (target_secure, str(multiprocessing.Process().name))
        logger.debug("[+] Insecure web server detected at %s and reported by process %s" % (str(target), str(multiprocessing.Process().name)))
        logger.debug("[-] Secure web server was not detected at %s and reported by process %s" % (str(target_secure), str(multiprocessing.Process().name)))
        return(r, rs)
    elif response_secure_data != None and response_data == None:
        r = "[-] No insecure webserver at %s reported by %s" % (target, str(multiprocessing.Process().name))
        rs = "[+] Secure webserver detected at %s reported by %s" % (target_secure, str(multiprocessing.Process().name))
        logger.debug("[-] Insecure web server was not detected at %s and reported by process %s" % (str(target), str(multiprocessing.Process().name)))
        logger.debug("[+] Secure web server detected at %s and reported by process %s" % (str(target_secure), str(multiprocessing.Process().name)))
        return(r, rs)
    else:
        logger.debug("[-] No results were recorded for %s or %s" % (str(target), str(target_secure)))

def log_init(log):
    level = logging.DEBUG                                                                             # Logging level
    format = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s") # Log format
    logger_obj = logging.getLogger()                                                                  # Getter for logging agent
    file_handler = logging.FileHandler(log)                                                           # File Handler
    #stderr_handler = logging.StreamHandler()                                                          # STDERR Handler
    targets_list = []

    # Configure logger formats for STDERR and output file
    file_handler.setFormatter(format)
    #stderr_handler.setFormatter(format)

    # Configure logger object
    logger_obj.addHandler(file_handler)
    #logger_obj.addHandler(stderr_handler)
    logger_obj.setLevel(level)

def main():
    # If script is executed at the CLI
    usage = '''usage: %(prog)s [-t hostfile] [-f logfile.log] [-m 2]  -q -v -vv -vvv'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-t", action="store", dest="targets", default=None, help="Filename for hosts to test")
    parser.add_argument("-m", "--multi", action="store", dest="multiprocess", default=1, type=int, help="Number of proceses, defaults to 1")
    parser.add_argument("-l", "--logfile", action="store", dest="log", default="results.log", type=str, help="The log file to output the results")
    parser.add_argument("-v", action="count", dest="verbose", default=1, help="Verbosity level, defaults to one, this outputs each command and result")
    parser.add_argument("-q", action="store_const", dest="verbose", const=0, help="Sets the results to be quiet")
    parser.add_argument('--version', action='version', version='%(prog)s 0.42b')
    args = parser.parse_args()

    # Argument Validator
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if (args.targets == None):
        parser.print_help()
        sys.exit(1)

    # Set Constructors
    targets = args.targets                                                                            # Targets to be parsed
    verbose = args.verbose                                                                            # Verbosity level
    processes = args.multiprocess                                                                            # Threads to be used
    log = args.log                                                                                    # Configure the log output file
    if ".log" not in log:
        log = log + ".log"

    # Load the targets into a list and remove trailing "\n"
    with open(targets) as f:
        targets_list = [line.rstrip() for line in f.readlines()]

    # Establish thread list
    pool = multiprocessing.Pool(processes=processes, initializer=log_init(log))

    # Queue up the targets to assess
    results = pool.map(host_request, targets_list)

    for result in results:
        for value in result:
            print(value)

'''
Finally, the following code uses the map function, which calls the host_request
function as it iterates through the list of targets. The map function allows a
multiprocessing script to queue work in a manner similar to the previous
multithreaded script. We can then use the processes variable loaded by the CLI
argument to define the number of subprocesses to spawn, which allows us to
dynamically control the number of processes that are forked. This is a very much
guess-and-check method of process control.
'''

if __name__ == '__main__':
    main()