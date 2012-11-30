import json
from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd


class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''        
    def get_counts2(self, sequence):
        counts = defaultdict(int) # values will initialize to 0
        for x in sequence:
            counts[x] += 1
        return counts
            
    def do_stuff(self):
        path = '/home/murdo/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
        records = [json.loads(line) for line in open(path)]
        time_zones = [rec['tz'] for rec in records if 'tz' in rec]
        #print time_zones
        #counts = self.get_counts2(time_zones)
        
        counts = Counter(time_zones)
        
        print counts.most_common(10)
        
        frame = DataFrame(records)
        #tz_counts = frame['tz'].value_counts()
        
        clean_tz = frame['tz'].fillna('Missing')

        clean_tz[clean_tz == ''] = 'Unknown'

        tz_counts = clean_tz.value_counts()
        
        print tz_counts[:10]
        
        tz_counts[:10].plot(kind='barh', rot=0)
        
        return -1
    
def main():
    clsTest = MyClass()
    ret_val = clsTest.do_stuff()
    print ret_val
    
if __name__ == "__main__":
    main()