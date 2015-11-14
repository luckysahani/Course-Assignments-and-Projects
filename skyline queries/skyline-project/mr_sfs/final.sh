python divison_mapper-mr-sfs.py < sample_data_1.txt > out1.txt
sort -k1 -n out1.txt > out2.txt
python divison_reducer-mr-sfs.py < out2.txt
python merging_mapper-mr-sfs.py < divison_job_reducer_output.txt > out3.txt
python merging_reducer-mr-sfs.py < out3.txt