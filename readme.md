# Mapreduce programming with Python Example

This program is an equivalent of a word count problem in Java.

## Prerequisites

If you need data to run, consider `https://github.com/drkiettran/mapreduce/src/main/resources/tragedy`

Need these folders in hdfs:

```

/user/student/shakespeare
/user/student/shakespeare/output

```

## Running the program

```bash

hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -input /user/student/shakespeare -output /user/student/shakespeare/output -mapper /home/student/dev/week_8/mapreduce-py/mapper.py -reducer /home/student/dev/week_8/mapreduce-py/reducer.py

```

## Installing pip3:

sudo apt install python3-pip