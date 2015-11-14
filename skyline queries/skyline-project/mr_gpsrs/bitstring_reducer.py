# Algorithm 1 Mapper of the bitstring generation
# Input: A subset Ri of the data set R, the dimensionality of the data set d, and the PPD n.
# Output: A bitstring BSRi
# for all the nd partitions with respect to Ri.
# Initialize a bitstring BSRi with all n d bits set to 0
# for each tuple t ∈ Ri do
# Decide the partition pj that t belongs to 
# BSRi [j] ← 1
# Output(null, BSRi)