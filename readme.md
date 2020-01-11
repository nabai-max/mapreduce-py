# Mapreduce programming with Python 
This project contains two MapReduce (MR) applications:
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
