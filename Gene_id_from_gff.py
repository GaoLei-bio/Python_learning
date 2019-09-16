'''
e.g. 
SL4.0ch00       maker_ITAG      gene    93750   94430   .       +       .       ID=gene:Solyc00g500001.1;Alias=Solyc00g500001;Name=Solyc00g500001.1;length=680
SL4.0ch00       maker_ITAG      mRNA    93750   94430   .       +       .       ID=mRNA:Solyc00g500001.1.1;Parent=gene:Solyc00g500001.1;Name=Solyc00g500001.1.1;Note=Retrovirus-related Pol polyprotein from transposon TNT 1-94 (AHRD V3.3 *-* A0A2I0VJ33_9ASPA);_AED=0.01;_QI=0|-1|0|1|-1|0|1|0|227;_eAED=0.01
SL4.0ch00       maker_ITAG      exon    93750   94430   .       +       .       ID=exon:Solyc00g500001.1.1.1;Parent=mRNA:Solyc00g500001.1.1
SL4.0ch00       maker_ITAG      CDS     93750   94430   .       +       0       ID=CDS:Solyc00g500001.1.1.1;Parent=mRNA:Solyc00g500001.1.1

SLL_5000        maker   gene    78633   79709   .       +       .       ID=gene:TomatoPan000010;Name=TomatoPan000010;Alias=maker-SLL_ERR418075_k119_100886:550-103331-snap-gene-0.1;Note=Protein of unknown function;
SLL_5000        maker   mRNA    78633   79709   .       +       .       ID=mRNA:TomatoPan000010.1;Parent=gene:TomatoPan000010;Name=TomatoPan000010.1;Alias=maker-SLL_ERR418075_k119_100886:550-103331-snap-gene-0.1-mRNA-1;_AED=0.53;_QI=0|0|0|1|0|0|3|0|214;_eAED=0.46;Note=Protein of unknown function;
SLL_5000        maker   exon    78633   79013   .       +       .       ID=exon:TomatoPan000010.1.1;Parent=mRNA:TomatoPan000010.1;
SLL_5000        maker   CDS     78633   79013   .       +       0       ID=CDS:TomatoPan000010.1.1;Parent=mRNA:TomatoPan000010.1;
SLL_5000        maker   exon    79290   79332   .       +       .       ID=exon:TomatoPan000010.1.2;Parent=mRNA:TomatoPan000010.1;
SLL_5000        maker   CDS     79290   79332   .       +       0       ID=CDS:TomatoPan000010.1.2;Parent=mRNA:TomatoPan000010.1;
SLL_5000        maker   exon    79489   79709   .       +       .       ID=exon:TomatoPan000010.1.3;Parent=mRNA:TomatoPan000010.1;
SLL_5000        maker   CDS     79489   79709   .       +       2       ID=CDS:TomatoPan000010.1.3;Parent=mRNA:TomatoPan000010.1;
'''

import re

with open(annotation_gff) as infile:
    for line in infile:
        cells = convert_int(line.strip().split("\t"))
        if not line.startswith("#"):
            gene_id = re.findall(r":(.*?);",cells[8])[0]
            gene_id = re.sub("\..*", "", gene_id)
            
