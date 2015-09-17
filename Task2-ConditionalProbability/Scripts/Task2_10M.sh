#! /bin/bash

BASE_FOLDER="/home/jmistry2/Assign2/Task2"
BASE_FOLDER_OUTPUT=$BASE_FOLDER"/output/"
DATASET_MAIN_FILE1="/home/dbarbara/MOVIELENS/ml-10M100K/ratings.dat"
DATASET_MAIN_FILE2="/home/dbarbara/MOVIELENS/ml-10M100K/movies.dat"
STREAMING_JAR="/apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar"
HADOOP_USER_INPUT="/user/jmistry2/input/"
HADOOP_USER_OUTPUT="/user/jmistry2/output/"
INPUT1=$HADOOP_USER_INPUT"ratings.dat"
OUTPUT1=$HADOOP_USER_OUTPUT"output1"

mkdir $BASE_FOLDER_OUTPUT
hadoop fs -rm $HADOOP_USER_INPUT"ratings.dat"
hadoop fs -rm $HADOOP_USER_INPUT"movies.dat"

hadoop fs -put $DATASET_MAIN_FILE1 $HADOOP_USER_INPUT
#hadoop fs -put $DATASET_MAIN_FILE2 $HADOOP_USER_INPUT

echo "Creating the co-occurrence matrix..."

hadoop jar $STREAMING_JAR \
		   -input $INPUT1 \
		   -output $OUTPUT1 \
		   -mapper $BASE_FOLDER/src/UserMovieMap.py \
		   -combiner $BASE_FOLDER/src/UserMovieReduce.py \
		   -reducer $BASE_FOLDER/src/UserMovieReduce.py

echo "Computing the relational frequencies..."

hadoop fs -get $OUTPUT1 $BASE_FOLDER_OUTPUT

OUTPUT2=$HADOOP_USER_OUTPUT"output2" 
hadoop jar $STREAMING_JAR \
		   -D stream.num.map.output.key.fields=2 \
		   -D stream.num.reduce.output.key.fields=2 \
		   -D mapred.text.key.partitioner.options=-k1,1 \
		   -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
		   -D mapred.text.key.comparator.options="-k1n -k2n" \
		   -input $OUTPUT1/part-00000 \
		   -output $OUTPUT2 \
		   -mapper $BASE_FOLDER/src/MoviePairMap.py \
		   -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
		   -reducer $BASE_FOLDER/src/MoviePairReduce.py

hadoop fs -get $OUTPUT2 $BASE_FOLDER_OUTPUT

#echo "Deleting intermediate results..."
#hadoop fs -rmr $OUTPUT1

echo "Producing expected results..."
OUTPUT3=$HADOOP_USER_OUTPUT"output3"
hadoop jar $STREAMING_JAR  \
          -files '/home/dbarbara/MOVIELENS/ml-10M100K/movies.dat#movies.dat'	\
          -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
          -D mapred.text.key.comparator.options="-k1nr" \
          -input $OUTPUT2/part-00000 \
          -output $OUTPUT3 \
          -mapper $BASE_FOLDER/src/FinalResultMap.py \
          -reducer org.apache.hadoop.mapred.lib.IdentityReducer

hadoop fs -get $OUTPUT3 $BASE_FOLDER_OUTPUT
#hadoop fs -get $OUTPUT3/part-00000 $BASE_FOLDER/output
echo "Done" 
