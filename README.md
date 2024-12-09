# 519_team_Frog
519 Final Project


gaia_matched folder:
Contains all of the data which has been already crossmatched with Gaia using TOPCAT. The data in this folder is not cleaned
        DESY_LT_crossmatch:
            the cross-matched brown dwarfs from DESY in Gaia in its native fits format
        DESY_M_crossmatch:
            the cross-matched m-dwarfs from DESY in Gaia in its native fits format
        DESY_MDwarfs_Crossmatch:
            the cross-matched m-dwarfs from DESY in Gaia in csv format
        DESY_NotMDwarfs_Crossmatch:
            the cross-matched brown dwarfs from DESY in Gaia in csv format
        JOHNSTON_MDwarfs_Crossmatch
            the cross-matched m-dwarfs from Johnston in Gaia in native csv format
        JOHNSTON_NotMDwarfs_Crossmatch
            the cross-matched brown dwarfs from Johnston in Gaia in native csv format
        RANDOM_Stars_Crossmatch:
            the cross-matched random list of stars from Gaia in csv format

info folder:
Contains important links and documentation
        AI Project outline + resources
            original outline provided in canvas
        GAIA Data Documentations
            link to all parameters provided by Gaia and their definitions
        SourcesList
            markdown cell with links and DOIs to sources of data
        ToDo
            markdown cell with list of tasks to do and progess (not often updated lol)

pre_matched_csv folder:
all data in csv format before fed through TOPCAT for crossmatching
        BrownDwarfs
            all brown dwarf data from both Johnston and DESY
        DESY_MDwarfs
            prematched m-dwarfs from DESY
        DESY_NotMDwarfs
            prematched brown dwarfs from DESY
        JOHNSTON_MDwarfs
            prematched m-dwarfs from Johnston
        JOHNSTON_NotMDwarfs
            prematched brown dwarfs from Johnston
        RANDOM_Stars
            prematched list of random RAs and DECs

raw_data folder:
all raw data completely unprocessed
        brown_dwarf_list_only_data
            Brown dwarf list from Johnston without extra header information. Includes all spectral types of dwarfs and their native parameters
        browndwarflist
            brown dwarf list from Johnston with full header. Includes all spectral types of dwarfs and their native parameters  
        DESY3_LTcatalog
            fits file containing all DESY brown dwarfs and their native parameters
        DESY3_Mcatalog
            fits file containing all DESY m-dwarfs and their native parameters

ALL_M&NotMDwarfs
    Contains all dwarfs from both data sets cross-matched and in CSV format

ALL_STARS
    contains all stars used cross-matched and in csv format

CombineCSVs
    used to combine our crossmatched CSV files

DataCleaning
    used to convert Johnston data into CSVs

FITs_to_CSV
    used to convert DESY data into CSVs

k_neighbors_spectral
    used to clean data and pick out spectroscopic data, ultimately pieces were taken and added to sup_learn_para

RandomForest
    uses random forest classifer from sklearn to classify data

RandomStars
    generates random RAs and DECs to crossmatch to a random list of stars

sup_learn_para
    holds entire k-nearest neighbors pipeline

sup_learn_para+parameters
    holds decision tree classifier and correlation matrices addition to k-nearest neighbors pipeline