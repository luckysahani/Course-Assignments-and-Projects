python divison_mapper-mr-angle.py < sample_data_1.txt > out1.txt
sort -k1 -n out1.txt > out2.txt
python divison_reducer-mr-angle.py < out2.txt
python merging_mapper-mr-angle.py < divison_job_reducer_output.txt > out3.txt
python merging_reducer-mr-angle.py < out3.txt