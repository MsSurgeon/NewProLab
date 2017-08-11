#!/usr/bin/env sh

hadoop fs -rm -r -f /user/roman.smirnov/results

hadoop jar ~/hadoop-streaming.jar \
	-D mapred.reduce.tasks=1 \
	-input /labs/facetz_2015_02_12/* \
	-output /user/roman.smirnov/results \
	-file ./m.py \
	-mapper m.py \
	-file ./r.py \
	-reducer r.py
