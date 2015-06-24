#!usr/local/bin/python3

# Name: Andrea Halweg-Edwards
# Date: 02/17/2015
# Homework #: 4
# Objectives: Calculate the Hamming distance and similarity scores for DNA
# sequences. Determine the identity of unknown sequence based on known
# sequences.

import os


def hamming_dist(seq1, seq2):
    # Hamming distance calculator
    hd = 0
    for nt in range(0, len(seq1)):
        if seq1[nt] != seq2[nt]:
            hd += 1
    return(hd)


def similarity_score(seq1, seq2):
    # Similarity score calculator
    hd = hamming_dist(seq1, seq2)
    similarity_score = float((len(seq1) - hd) / len(seq1))
    return('%.6f' % similarity_score)


def MouseCompare(mouse_seq_file, unknown_seq_file):
    return(similarity_score(open(mouse_seq_file, "r").read(),
           open(unknown_seq_file, "r").read()))


def HumanCompare(human_seq_file, unknown_seq_file):
    return(similarity_score(open(human_seq_file, "r").read(),
           open(unknown_seq_file, "r").read()))


def DetermineUnknown(mouse_seq_file, human_seq_file, unknown_seq_file):
    if len(open(mouse_seq_file, "r").read()) == len(open(human_seq_file,
                                                         "r").read()):
        MouseSim = MouseCompare(mouse_seq_file, unknown_seq_file)
        print("MouseCompare = ", MouseSim)
        HumanSim = HumanCompare(human_seq_file, unknown_seq_file)
        print("HumanCompare = ", HumanSim)
        if abs(float(MouseSim) - float(HumanSim)) < 0.0001:
            print("identity cannon be determined")
        elif MouseSim > HumanSim:
            print("mouse")
        else:
            print("human")
    else:
        print("Sequences do not have equal length")


DetermineUnknown(os.getcwd() + os.sep + 'mouseDNA.txt',
                 os.getcwd() + os.sep + 'humanDNA.txt',
                 os.getcwd() + os.sep + 'unknownDNA.txt')
