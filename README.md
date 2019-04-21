# Welcome to chen-qut-PRED, a  protein Quaternary Structural Type predictor.
![chen-qut-pred](https://raw.githubusercontent.com/linch1226/chen-qut-PRED/master/Img/flow.png)
Specific steps we can clearly see in the flow chart
## Prerequisites：
###### Python2.7 
###### biopython
###### mysql
## Introduction:
The main script for the predictor contains the main commands.＜/br＞
GO_descriptor: it is used to construct protein sequences. This program includes how to find homologous proteins and how to search local databases. Some of the codes need to install specific packages, which we mentioned in the requirements＜/br＞
Pfam_deccriptor : The Pfam program contains an online search for http://pfam.xfam.org to capture the functional domain  of a specific protein by searching the website. So we construct vectors＜/br＞
Jacknife_rf contains classification algorithms and cross-validation procedures

## For help:
if someone have any questions and suggestions, please tell me. ＜/br＞
Send mail to :cwjlinch@163.com
## Note:
Because this method is based on gene ontology. With the update of gene ontology, users can download the latest go data from the official website. We believe that the forecast results will be further increased.
