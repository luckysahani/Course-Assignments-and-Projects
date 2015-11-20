python building_mapper-mr-bitmap.py < dim_10000_5 > out1.txt
sort -k1 -n out1.txt > out2.txt
python building_reducer-mr-bitmap.py < out2.txt > out3.txt
python examining_mapper-mr-bitmap.py < dim_10000_5 > out4.txt
sort -k1 -n out4.txt > out5.txt
python examining_reducer-mr-bitmap.py < out5.txt