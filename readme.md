# Mapreduce programming with Python

This is a Python projects that contains two MapReduce applications:
    - Word Count
    - Flights By Carriers

## Assumption

Need to use cisc-525-util repository to:
    - start up hadoop
    - prepare data (make sure you have the data downloaded and stored in the right place)
    - verify data loaded correctly

## Run Word Count MR application

```shell script
cd word_count
./word_count_run.sh word_count_mapper.py word_count_reducer.py /user/student/shakespeare/tragedy/othello.txt /tmp/othello
hdfs dfs -cat /tmp/othelo/part-00000
```

## Run airline performance MR application

```shell script
cd air-traffic
./airline_run.sh flights_by_carriers_mapper.py flights_by_carriers_reducer.py /user/student/airline/1987.csv /tmp/1987
hdfs dfs -cat /tmp/1987/part-00000
```

## Create Python codes for flighs by origin
Mapper
```shell script
#!/usr/bin/env python3

import sys
import socket
import re


class FlightsByOriginCitiesMapper:
    def __init__(self):
        # initial code
        self.count = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)

    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)

    def map(self):
        for line in sys.stdin:
            # self._log(line)
            s = re.sub('[.,:;?!|]', ' ', line).split()
            # self._log(s[0])
            if s[0] == 'Year':
                self._log(line)
            else:
                print('{}\t{}'.format(s[16], 1))


# Main

def main(argv):
    flightsByOriginCitiesMapper = FlightsByOriginCitiesMapper()
    flightsOriginCitiesMapper.map()


if __name__ == "__main__":
    main(sys.argv[:1])
```

Reduccer

```shell script 
#!/usr/bin/env python3

import sys
import socket
import re

class FlightsByOriginCitiesReducer:
    def __init__(self):
        # initial code
        self.count = 0
        self.current_word = None
        self.word = None
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        
    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)
                
    def reduce(self):
        for line in sys.stdin:
            # self._log(line)
         
            line = line.strip()
            self.word, count = line.split('\t', 1)
            try:
                count = int(count)
            except ValueError:
                continue
            
            if self.current_word == self.word:
                self.current_count += count
            else:
                if self.current_word:
                    print ('{}\t{}'.format(self.current_word, self.current_count))
                self.current_count = count
                self.current_word = self.word
                
        if self.current_word == self.word:
            print('{}\t{}'.format(self.current_word, self.current_count))

# Main

def main(argv):
    flightsByOriginCitiesReducer = FlightsByOriginCitiesReducer()
    flightsByOriginCitiesReducer.reduce()

if __name__ == "__main__":
    main(sys.argv[:1])
```

## Run the application

```shell script
cd air-traffic
./airline_run.sh flights_by_origin_mapper.py flights_by_origin_reducer.py /user/student/airline/2000.csv /tmp/2000
hdfs dfs -cat /tmp/2000/part-00000
./airline_run.sh flights_by_origin_mapper.py flights_by_origin_reducer.py /user/student/airline/2001.csv /tmp/2001
hdfs dfs -cat /tmp/2001/part-00000
./airline_run.sh flights_by_origin_mapper.py flights_by_origin_reducer.py /user/student/airline/2000.csv /tmp/2002
hdfs dfs -cat /tmp/2002/part-00000

```

## Create Python codes for flighs by departure

## Run the application

```shell script
cd air-traffic
./airline_run.sh flights_by_depature_mapper.py flights_by_depature_reducer.py /user/student/airline/2000.csv /tmp/2000
hdfs dfs -cat /tmp/2000/part-00000
./airline_run.sh flights_by_depature_mapper.py flights_by_depature_reducer.py /user/student/airline/2001.csv /tmp/2001
hdfs dfs -cat /tmp/2001/part-00000
./airline_run.sh flights_by_depature_mapper.py flights_by_depature_reducer.py /user/student/airline/2000.csv /tmp/2002
hdfs dfs -cat /tmp/2002/part-00000




```
