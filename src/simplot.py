import random
import pathlib
from Bio import SeqIO, AlignIO
# "Reference_genomes_profile_mafft_GINSI.fa"

# TODO: Need to make this global, don't initialise it everytime simplot is run
# seqs = SeqIO.to_dict(SeqIO.parse(file,"fasta"))

def isolate_sequence(seqs_dict,seq):
	"""
	Write the selected sequence in a temporary file in order to create a simplot
	"""
	randname = random.randit(0,100000000000)
	fout =  PATH + str(randname) + ".fa"


def align(muscle_bin, db_gene_f):
	"""
	Profile alignment the desired sequence with the 4 represenatives (A-D 1)
	Profile alignment is used to gain speed
	The A-D sequence database is already aligned with mafft g-insi parameters (DOI:10.1093/nar/gkf436)
	"""
	aln_cline = MuscleCommandline(cmd = muscle_bin, in1=f, in2=db_gene_f, out=f, profile=True)

def calculate_similarities(qseq, aln_f, step, window):
	"""
	Seq is the query sequence based on which the similarities are calculated
	"""
	results = {}
	def _distance(seq1, seq2, ignore_gaps=False):
		"""
		P-distance is calculated in this function
		"""
		dissimilar = 0
		seqsize = 0
		for char1, char2 in zip(seq1,seq2):
			if ignore_gaps:
				if char1 == "-" or char2 == "-":
					continue
			seqsize += 1
			if char1 != char2:
				dissimilar += 1
		return round(dissimilar/seqsize,3)
	
	aln = AlignIO.read(aln_f,"fasta")
	names = []
	indeces = list(range(len(aln)))
	for idx in indeces:
		name = aln[idx].id
		if qseq == name:
			break
	indeces.remove(idx)
	qidx = idx
	aln_len = aln.get_alignment_length()

	for idx in indeces:
		positions = []
		db_name = aln[idx].id
		results[db_name] = []
		pos = 0
		while pos < aln_len:
			positions.append(pos)
			#TODO: For some reason the simplot in the end is different from Simplot software and TRECS
			# Maybe they ditch the if TRUE condition?
			if pos+window+1 > aln_len:
				seq1 = str(aln[qidx, pos:aln_len].seq) 
				seq2 = str(aln[idx , pos:aln_len].seq)
			else:
				seq1 = str(aln[qidx, pos:pos+window+1].seq)
				seq2 = str(aln[idx , pos:pos+window+1].seq)
			identity = (1 - _distance(seq1,seq2)) * 100
			results[db_name].append(identity)
			pos += step
	tmp_qseq = str(aln[qidx].seq).replace("-","")
	tmp_qseq_size = len(tmp_qseq)
	return positions, results, aln_len, tmp_qseq_size

def rm_tmpfile(file):
	"""
	Removes the temporary files that are created for the simplot graph 
	"""
	if type(file) != pathlib.Path():
		file = pathlib.Path(file)
	try:
		file.unlink()
	except:
		pass