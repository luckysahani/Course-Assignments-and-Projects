python divison_mapper-mr-bnl.py < sample_data_1.txt > out1.txt
sort -k1 -n out1.txt > out2.txt
python divison_reducer-mr-bnl.py < out2.txt