#! /bin/bash

BASE_FOLDER="/home/jmistry2/Assign2/Task1/Pairs"
DATASET_MAIN_FILE1="/home/dbarbara/MOVIELENS/ml-10M100K/ratings.dat"
DATASET_MAIN_FILE2="/home/dbarbara/MOVIELENS/ml-10M100K/movies.dat"
HADOOP_USER_INPUT="/user/jmistry2/input/"
HADOOP_USER_OUTPUT="/user/jmistry2/output/"
INPUT1=$HADOOP_USER_INPUT"ratings.dat"
OUTPUT1=$HADOOP_USER_OUTPUT"/outputPhase1/" 
STREAMING_JAR="/apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar"

echo "Counting the movies rated highly by each person..."

mkdir $BASE_FOLDER/output/
hadoop fs -put $DATASET_MAIN_FILE1 $HADOOP_USER_INPUT
hadoop fs -put $DATASET_MAIN_FILE2 $HADOOP_USER_INPUT

hadoop jar $STREAMING_JAR \
		  -D mapreduce.job.maps=1 \
		  -input $INPUT1 \
          -output $OUTPUT1 \
          -mapper $BASE_FOLDER/src/Task1_1M_Map1.py \
          -combiner $BASE_FOLDER/src/Task1_100K_Reduce1.py \
          -reducer $BASE_FOLDER/src/Task1_100K_Reduce1.py

#mkdir $BASE_FOLDER/output/outputPhase1/
hadoop fs -get $OUTPUT1 $BASE_FOLDER/output/

echo "Computing the Co-Occurrence Matrix..."

OUTPUT2=$HADOOP_USER_OUTPUT"/outputPhase2/" 
hadoop jar $STREAMING_JAR \
          -D stream.num.map.output.key.fields=2 \
          -D stream.num.reduce.output.key.fields=2 \
          -input $OUTPUT1/part-00000 \
          -output $OUTPUT2 \
          -mapper $BASE_FOLDER/src/Task1_100K_Aggregate_Map2.py \
          -reducer aggregate

OUTPUT3=$HADOOP_USER_OUTPUT"/outputPhase3/"

#mkdir $BASE_FOLDER/output/outputPhase2/
hadoop fs -get $OUTPUT2 $BASE_FOLDER/output/

echo "Computing the most frequent movie pairs..."

hadoop jar $STREAMING_JAR \
		  -files '/home/dbarbara/MOVIELENS/ml-10M100K/movies.dat#movies.dat' \
          -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
          -D mapred.text.key.comparator.options="-k1nr" \
          -input $OUTPUT2/part-00000 \
          -output $OUTPUT3 \
          -mapper $BASE_FOLDER/src/Task1_1M_Final_Map3.py \
          -reducer org.apache.hadoop.mapred.lib.IdentityReducer

#echo "Deleting temp files and folders..."

#rm -r $OUTPUT1
#rm -r $OUTPUT2

#mkdir $BASE_FOLDER/output/outputPhase3/
hadoop fs -get $OUTPUT3 $BASE_FOLDER/output/

head -n 20 $BASE_FOLDER/output/outputPhase3/part-00000 > $BASE_FOLDER/output/Task1_ml-10M_Pairs_output.txt

#rm -r $OUTPUT3

#hadoop fs -rm -r $HADOOP_USER_OUTPUT

echo "Output file "$BASE_FOLDER/output/Task1_ml-10M_Pairs_output.txt" created..."

echo "Done" 
