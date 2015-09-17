#! /bin/bash

DATASET_MAIN_FILE1="/home/dbarbara/MOVIELENS/ml-100K/u.data"
DATASET_MAIN_FILE2="/home/dbarbara/MOVIELENS/ml-100K/u.item"

hadoop fs -rm /user/jmistry2/input/ratings.dat
hadoop fs -rm /user/jmistry2/input/movies.dat
hadoop fs -rm /user/jmistry2/input/u.data
hadoop fs -rm /user/jmistry2/input/u.item

hadoop fs -put $DATASET_MAIN_FILE1 /user/jmistry2/input/
hadoop fs -put $DATASET_MAIN_FILE2 /user/jmistry2/input/

mkdir /home/jmistry2/Assign2/Task1/Stripes/output
hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
		   -input /user/jmistry2/input/u.data \
		   -output /user/jmistry2/output/output1 \
		   -mapper /home/jmistry2/Assign2/Task1/Stripes/src/Stripes_map1.py \
		   -reducer /home/jmistry2/Assign2/Task1/Stripes/src/Stripes_reduce1.py

hadoop fs -get /user/jmistry2/output/output1 /home/jmistry2/Assign2/Task1/Stripes/output/

hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
		  -cacheFile '/user/jmistry2/input/u.item#movies.dat' \
		  -input /user/jmistry2/output/output1/part-00000 \
		  -output /user/jmistry2/output/output2 \
		  -mapper /home/jmistry2/Assign2/Task1/Stripes/src/Stripes_map2.py \
		  -reducer /home/jmistry2/Assign2/Task1/Stripes/src/Stripes_reduce2.py

hadoop fs -get /user/jmistry2/output/output2 /home/jmistry2/Assign2/Task1/Stripes/output/