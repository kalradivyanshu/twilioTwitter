import datetime
import sys
import os

class Logger:
    def error(self, log):
        print(log)
        with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/logs/error.log','a') as outFile:
            outFile.write('\n' + str(datetime.datetime.now()) + str("  "+str(log)))

    def access(self, log):
        print(log)
        with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/logs/access.log','a') as outFile:
            outFile.write('\n' + str(datetime.datetime.now()) + str("  "+str(log)))

    def debug(self, log):
        print(log)
        with open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/logs/debug.log','a') as outFile:
            outFile.write('\n' + str(datetime.datetime.now()) + str("  "+str(log)))
