#!/usr/bin/python
from sudoku_maker import *
import sys

#a = SudokuMaker(generator_args={'clues':27, 'group_size':0}, pickle_to="./generated_puzzles");

#a.get_new_puzzle(0.5);

#a.make_batch()

def get_puzzle_string(clu,diflow, difhigh):
    a = SudokuGenerator(clues=clu);
    max_iter=10; niter=0
    while True:
        niter+=1
        puz,diff = a.make_unique_puzzle(); 
        #print "LOLO",diff.value>0.4 and  diff.value<0.5
        if (diff.value<=difhigh and diff.value>=diflow) or niter>max_iter:
            break
#    return puz
    #if puz: print puz,diff
    result = ""
    for i in puz.grid:
        for j in i:
            result += str(j)
    #print result
    return result

#result = a.generate_puzzle_for_difficulty(0.5); 

#a.assess_difficulty()

#print result.grid

def main():
    #ofile = open(sys.argv[1],"w")
#    get_puzzle_string(36,0.4,0.5)
    #result = get_puzzle_string(int(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
    result = get_puzzle_string(int(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    sys.stdout.write(result)
    #ofile.write(result)
    #ofile.close()


if __name__ == "__main__":
    main()
