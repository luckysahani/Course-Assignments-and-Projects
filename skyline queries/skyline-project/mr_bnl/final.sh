python divison_mapper-mr-bnl.py < anti_100000_5 > out1.txt
sort -k1 -n out1.txt > out2.txt
python divison_reducer-mr-bnl.py < out2.txt > divison_job_reducer_output.txt
python merging_mapper-mr-bnl.py < divison_job_reducer_output.txt > out3.txt
python merging_reducer-mr-bnl.py < out3.txt