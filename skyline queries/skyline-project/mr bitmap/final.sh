python building_mapper-mr-bitmap.py < sample_data_3.txt > out1.txt
sort -k1 -n out1.txt > out2.txt
python building_reducer-mr-bitmap.py < out2.txt 
python examining_mapper-mr-bitmap.py < building_job_reducer_output.txt > out3.txt
# python examining_reducer-mr-bitmap.py < out3.txt