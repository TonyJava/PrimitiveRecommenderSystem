#! /bin/bash

BASE_FOLDER="/home/jmistry2/Assign2/Task4"
BASE_FOLDER_OUTPUT=$BASE_FOLDER"/output/"
DATASET_MAIN_FILE1="/home/dbarbara/MOVIELENS/ml-100K/u.data"
DATASET_MAIN_FILE2="/home/dbarbara/MOVIELENS/ml-100K/u.item"
STREAMING_JAR="/apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar"
HADOOP_USER_INPUT="/user/jmistry2/input/"
HADOOP_USER_OUTPUT="/user/jmistry2/output/"
INPUT1=$HADOOP_USER_INPUT"u.data"
OUTPUT1=$HADOOP_USER_OUTPUT"output1"

mkdir $BASE_FOLDER_OUTPUT
hadoop fs -rm $HADOOP_USER_INPUT"ratings.dat"
hadoop fs -rm $HADOOP_USER_INPUT"movies.dat"
hadoop fs -rm $HADOOP_USER_INPUT"u.data"
hadoop fs -rm $HADOOP_USER_INPUT"u.item"

hadoop fs -put $DATASET_MAIN_FILE1 $HADOOP_USER_INPUT
hadoop fs -put $DATASET_MAIN_FILE2 $HADOOP_USER_INPUT

echo "Creating buckets...."

hadoop jar $STREAMING_JAR \
		   -input $INPUT1 \
		   -output $OUTPUT1 \
		   -mapper $BASE_FOLDER/src/UserMovieMap.py \
		   -combiner $BASE_FOLDER/src/UserMovieReduce.py \
		   -reducer $BASE_FOLDER/src/UserMovieReduce.py

echo "computing frequent item sets using apriori..."

hadoop fs -get $OUTPUT1 $BASE_FOLDER_OUTPUT

OUTPUT2=$HADOOP_USER_OUTPUT"output2" 
hadoop jar $STREAMING_JAR \
		   -input $OUTPUT1/part-00000 \
		   -output $OUTPUT2 \
		   -mapper $BASE_FOLDER/src/apriori_Map.py \
		   -reducer $BASE_FOLDER/src/apriori_Reduce.py

hadoop fs -get $OUTPUT2 $BASE_FOLDER_OUTPUT

echo "Computing final output...."
OUTPUT3=$HADOOP_USER_OUTPUT"output3"
hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
		   -cacheFile '/user/jmistry2/input/u.item#movies.dat' \
		   -cacheFile '/user/jmistry2/output/output2/part-00000#candidateItemSets.dat' \
		   -input /user/jmistry2/output/output1/part-00000 \
		   -output /user/jmistry2/output/output3 \
		   -mapper /home/jmistry2/Assign2/Task3/src/SON_Map.py \
		   -reducer /home/jmistry2/Assign2/Task3/src/SON_Reduce.py

hadoop fs -get $OUTPUT3 $BASE_FOLDER_OUTPUT

echo "Done" 
