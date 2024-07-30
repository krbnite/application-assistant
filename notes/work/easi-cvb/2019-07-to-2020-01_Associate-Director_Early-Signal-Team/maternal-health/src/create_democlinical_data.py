"""
This code is basically just a copy-and-paste from
JNB 02a__KU in the ./notebooks/ directory, which is where I
actually created the files... This code was extracted to
make it easier on the next person, if any.
"""

import pandas as pd

data = dict()

# MENTAL
# V3 Update: 
#   * all vars the same
#   * a single NaN still exists
#  -- NOTE: May have to drop all these vars (they are nearly constant)
v3_mental_cols = ['patid',
    'aantipsych2','antianx2','anticonv2','antidepress2','cantipsych2',
    'moodstab2','ssri2','stim2',]
mental = pd.read_csv('../../data/raw/Derived Variables of Interest Participants Only.mental_ill_DB.csv',
    usecols = v3_mental_cols)
mental.fillna(-999999, inplace=True)
mental.set_index('patid', inplace=True)
data['mental'] = mental


# ADAFPPAPPA
# V3 Update:  
#   * all vars the same
#   * Dani fixed missing value representation (-9999.99 --> -999999)
#     - no longer need: 
#       adafppappa.afpmom = adafppappa.afpmom.\
#           map(lambda x: -999999 if x == -9999.99 else x)

v3_adalc_cols = ['PATID','AFPMoM']
adafppappa = pd.read_csv('../../data/raw/adafppappa_DB.csv', usecols = v3_adalc_cols)
adafppappa.columns = map(str.lower, adafppappa.columns)
adafppappa.set_index('patid', inplace=True)
data['adafppappa'] = adafppappa


# ADALC 
# V3 Update: 
#   * use_cols: range(0,12) --> v3_adalc_vars
v3_adalc_vars = ['patid', 
    'Binge7T12', 'Binge7T22', 'BingeCountT1',
    'BingeCountT2', 'DrankAroundLMP2', 'MaxConsDDaysT1', 'MaxConsDDaysT2',
    'OneYrPrior6', 'TotalStdDrinksLMP', 'TotalStdDrinksT1',
    'TotalStdDrinksT2',]
adalc = pd.read_csv('../../data/raw/adalc_patid_DB.csv', usecols=v3_adalc_vars)
adalc.columns = map(str.lower, adalc.columns)
adalc.set_index('patid', inplace=True)
data['adalc'] = adalc


# ADCDRISC
# V3 Update:
#   * no longer need to set na_values='#NULL!' in read_csv (Dani fixed file)
#     - the file formerly contained on bad value like this; now it doesn't
#     - this obviates the need for the adcdrisc.fillna() command as well
#   * all vars the same though
v3_adcdrisc_cols = ['patid','CDRISC_Raw']
adcdrisc = pd.read_csv('../../data/raw/adcdrisc_DB.csv', usecols=v3_adcdrisc_cols)
adcdrisc.columns = map(str.lower, adcdrisc.columns)
adcdrisc.set_index('patid', inplace=True)
data['adcdrisc'] = adcdrisc


# ADDRG 
# V3 Update:
#   * following vars no longer included from the outset:
#     - 'Hair1YrPrior6', 'HairLMP2', 'HairT12', 'HairT22',
#       'Hookah1YrPrior6', 'HookahLMP2', 'HookahT12', 'HookahT22',
#       'MJ1YrPrior6'
#    * this means the "drop cols" list is slightly smaller as well
#-----
# It is essentially necessary to drop: 
#     hair1yrprior6 (0 nznn), hairlmp2 (0 nznn), hairt12 (0), hairt22 (2)
# It is likely necessary to drop: 
#     otherlmp2 (2 nznn instances)
# It might be worth dropping:
#     othert12 (14 nznn), othert22 (16), other1yrprior2 (20), methlmp2 (54)
# NOTE: nznn := nonzero/nonNull values
v3_addrg_cols = [ 'patid',
    'Meth1YrPrior6', 'MethLMP2', 'MethT12', 'MethT22',
    'MJLMP2', 'MJT12', 'MJT22', 'Other1YrPrior2', 
    'OtherLMP2', 'OtherT12', 'OtherT22',
]
addrg = pd.read_csv('../../data/raw/addrg_patid_DB.csv', usecols=v3_addrg_cols)
addrg.columns = map(str.lower, addrg.columns)
addrg_drop=False
if addrg_drop:
    addrg_drop_cols = ['otherlmp2','othert12','othert22','other1yrprior2','methlmp2']
    addrg.drop(addrg_drop_cols, axis=1, inplace=True)
addrg.set_index('patid', inplace=True)
data['addrg'] = addrg


# ADEDIN (merged edit bish)
# V3 Update:
#   * no updates necessary (same vars, same code)
#     - this means that Dani did not find and fix the single NaN in the file
#-----------
#  -- Do we want to keep the Endinburgh CycleID? (Bill recommneds not to, while
#     Dani thinks it can serve as a source of interaction information, e.g., within
#     a RF)
adedin_merged_edit_bish = pd.read_csv('../../data/raw/adedin_merged_edit_bish_DB.csv')
adedin_merged_edit_bish.columns = ['patid', 'edinburgh', 'edinburgh_cycle_id']
adedin_merged_edit_bish.fillna(-999999, inplace=True)
adedin_merged_edit_bish.set_index('patid', inplace=True)
data['adedin'] = adedin_merged_edit_bish


# ADELIG
# V3 Update:
#   * Vars: MAT_AGE, RACEAI4, RACENIH7
#     - i.e., no hispanic2 var, etc
#------
v3_adelig_cols = ['patid', 'MAT_AGE', 'RACEAI4', 'RACENIH7']
adelig = pd.read_csv('../../data/raw/adelig_DB.csv', 
                     usecols=v3_adelig_cols)
adelig.columns = map(str.lower, adelig.columns)
adelig.set_index('patid', inplace=True)
data['adelig'] = adelig


# ADFETALGROWTH
# V3 Update:
#   * No changes necessary (same vars)
v3_adfetalgrowth_cols = ['patid', 'FetusSex', 'DeviationIndex']
adfetalgrowth = pd.read_csv('../../data/raw/adfetalgrowth_BISHCORRECTED_01.24.19_persex_DB.csv',
                           usecols = v3_adfetalgrowth_cols)
adfetalgrowth.columns = ['patid', 'fetussex', 'growth_deviation_index']
adfetalgrowth.set_index('patid', inplace=True)
data['adfetalgrowth'] = adfetalgrowth


# ADMH
# V3 Update:
#   * added final list of vars and use `usecols` parameters in `read_csv`, 
#     obviating need for dropping any cols
#-----------
#  -- NOTE:  Each of the var listed below have less than 50 nonZero/nonNull instances (out of nearly 7k records):
#       'hxsuid2', 'hxsids2', 'hxsidssuid2', 'hx_baby_cleft2', 'hx_baby_down2',
#       'hx_baby_fas2', 'hx_baby_pfas2', 'hx_baby_heart2',
#       'hx_baby_hypoxiaencep2', 'hx_baby_iugrsga2', 'hx_baby_retard2',
#       'hx_baby_neuraltube2', 'hx_baby_poorweight2', 'hx_baby_shoulder2',
#       'sicklecellanemiaprior2', 'apsprior2', 'anxietyprior2',
#       'bloodclotprior2', 'cancerprior2', 'connectivetissuedisorderprior2',
#       'gdmprior2', 'gdmpriorfp2', 'hyperthyroidprior2', 'hypothyroidprior2',
#       'lupusprior2', 'abruptionprior2', 'abruptionpriorfp2',
#       'placentapreviaprior2', 'placentapreviapriorfp2', 'ppromprior2',
#       'pprompriorfp2', 'raprior2', 'thromboembolicdiseaseprior2'
#  -- most of the vars have less than 10% (~700) nznn values
#--------
# Note that Dani write ConnectiveTissueDisorderPrior2, but the var name in the file
#     is actually ConnectivetissuedisorderPrior2 (fewer capitals)
v3_admh_cols = ['patid',
    'AbruptionPrior2', 'AbruptionPriorFP2', 'ANEMIA3', 'AnxietyPrior2',
    'APSPrior2', 'BloodClotPrior2', 'CancerPrior2', 'CesareanPrior2', 
    'ConnectivetissuedisorderPrior2', 'DepressionPrior2', 'DiabetesPrior2',
    'EpilepsyPrior2', 'GDMPrior2', 'GDMPriorFP2', 'HeartDisPrior2',
    'HepatitisPrior2', 'HTNNotPregPrior2', 'HTNPregPrior2', 'HTNPregPriorFP2',
    'HX_Baby_Cleft2', 'HX_Baby_Down2', 'HX_Baby_fas2', 'HX_Baby_Heart2', 
    'HX_Baby_HypoxiaEncep2', 'HX_Baby_IUGRSGA2', 'HX_Baby_Jaundice2',
    'HX_Baby_NeuralTube2', 'HX_Baby_NICU2', 'HX_Baby_pfas2', 'HX_Baby_PoorWeight2',
    'HX_Baby_Retard2', 'HX_Baby_Shoulder2', 'HXAB2', 'HXFT2', 'HXID2', 
    'HXLB2', 'HXMC2', 'HXNT2', 'HXPT2', 'HXSB2', 'HXSIDS2', 'HXSIDSSUID2',
    'HXSUID2', 'HyperthyroidPrior2', 'HypothyroidPrior2', 'LupusPrior2',
    'PlacentaPreviaPrior2', 'PlacentaPreviaPriorFP2', 'PPROMPrior2',
    'PPROMPriorFP2', 'RAPrior2', 'RenalDisPrior2', 'SickleCellAnemiaPrior2',
    'tbprior2', 'ThromboembolicDiseasePrior2']
admh = pd.read_csv('../../data/raw/admh_DB.csv', usecols=v3_admh_cols)
admh.columns = map(str.lower, admh.columns)
admh.set_index('patid', inplace=True)
data['admh'] = admh


# ADPTSD
# V3 Update:
#   * cols changed a bit
#   * Dani removed all non-BISH patients from file, so it is no
#     longer necessary to do so here
#   ** removed corresponding code:
#         bish_index = adptsd.patid.str.\
#             split('-').map(lambda x: x[1]) == 'BISH'
#         adptsd = adptsd[bish_index].reset_index(drop=True).dropna()
#----------------
#  -- MY REC:  DO NOT USE THIS STUFF AT ALL (here just in case we decide to)
v3_adptsd_cols = ['patid',
    'HTQ_Total_Raw_CID15-20', 'LEC_Events_CID15-20', 'LEC_Exp_CID15-20']
adptsd = pd.read_csv('../../data/raw/adptsd_DB.csv', usecols=v3_adptsd_cols)
adptsd.set_index('patid', inplace=True)
data['adptsd'] = adptsd


# ADSC
# V3 Update:
#   * a few additional targets were added (Cesarean2, DLVRY_DT, DLVRYGA_DYS_SBadj)
#   * code: twin removal is no longer done here; turns out that the outer
#       joins we do later just add them back in.  Moral: remove twins after all
#       outer joins take place.
#-----------------
#  -- THIS HAS 50 DUPLICATED PATIDs due to twins...
#  -- Udi dropped these...and for the time being, I suggest we do the same, since
#     it basically serves as doubling up data points (there is no twin-tuned sensor
#     data for example;  the only var that might change is gender).
#  -- NOTE: I added a few potential target vars that Dani didn't include in
#     her greenlit vars, namely: 'DLVRYGA_DYS', 'Preterm2', 'DLVRYBefore34Wks', 
#     and 'DLVRYBefore28wks'
#------------------------
# NOTE: When modeling, make sure to remove all targets from input set:
#     'LaborType_SpontaneousOrAugmented_DB', 'Cesarean2', 'DLVRY_DT', 
#     'DLVRYGA_DYS_SBadj', 'DLVRYBefore28wks', 'DLVRYBefore34Wks', 
#     'DLVRYGA_DYS'
#------------------------
# NOTE: in Dictionary, Dani lists TWIN2 and GENDER2; in the table these
#     are twin2 and gender2 (lowercase)
#------------------------
# IMPORTANT: TWINS must be dropped after all tables are OUTER joined
v3_adsc_cols = ['patid',
    'gender2', 'twin2', 'Cesarean2', 'DLVRY_DT', 'DLVRYBefore28wks',
    'DLVRYBefore34Wks', 'DLVRYGA_DYS', 'DLVRYGA_DYS_SBadj']
adsc = pd.read_csv('../../data/raw/adsc_DB.csv', usecols=v3_adsc_cols)
adsc.columns = map(str.lower, adsc.columns)
adsc.set_index('patid', inplace=True)
data['adsc'] = adsc


# ADSCMAT
# V3 Update:
#   * Removed: AugmentedLabor2, CesareanNoLabor2, InducedLabor2
#   * Added: LaborType_SpontaneousOrAugmented_DB
#   * Dani fixed missing value representation (string percentages, "-9999.99%",
#     to integer -999999), so no longer need to do so here
#   **Removed corresponding code:
#         fix = list(set(v3_adscmat_cols).difference(['patid']))
#         adscmat[fix] = adscmat[fix].\
#             applymap(lambda x: x.split('.')[0]).astype(int).\
#             applymap(lambda x: int(x/100) if x < 0 else x)
#------------------------
# NOTE: When modeling, make sure to remove all targets from input set:
#     'LaborType_SpontaneousOrAugmented_DB', 'Cesarean2', 'DLVRY_DT', 
#     'DLVRYGA_DYS_SBadj', 'DLVRYBefore28wks', 'DLVRYBefore34Wks', 
#     'DLVRYGA_DYS'
#------------------------
# NOTE: what Dani calls 'NULLIPAROUS2' is listed as 'Nulliparous2' 
#       in the CSV table
v3_adscmat_cols = [ 'patid',
    'LaborType_SpontaneousOrAugmented_DB',
    'EDUC_COMBOHS4', 'EMPL', 'EMPL_COMB4', 'Fertility2',
    'GrossIncome7', 'Nulliparous2', 'PARITY', 'PreCareFirstGA',
    'PreCareT1_2', 'ToiletWater2',
]
adscmat = pd.read_csv('../../data/raw/adscmat_DB.csv', usecols=v3_adscmat_cols)
adscmat.columns = map(str.lower, adscmat.columns)
adscmat.set_index('patid', inplace=True)
data['adscmat'] = adscmat


# ADSMK 
# V3 Update:
#   * No changes necessary
v3_adsmk_cols = ['patid','AvgNumCigHome']
adsmk = pd.read_csv('../../data/raw/adsmk_patid_DB.csv', 
                    usecols=v3_adsmk_cols)
adsmk.columns = map(str.lower, adsmk.columns)
adsmk.set_index('patid', inplace=True)
data['adsmk'] = adsmk


# ADSTAI
# V3 Update:
#   * no changes necessary
#----------------
#  -- Do we want to keep STAI_AGE (mother's age at time of test)?  We already have
#     an age variable (MAT_AGE from adelig_DB.csv).  Assuming this test is administered
#     within several months of when MAT_AGE was recorded, it would be fairly redundant
#     info (even up to a year in separation, if you ask me).
#----------------
#  -- UPDATE:  we drop STAI_AGE below, when we join all tables.
adstai = pd.read_csv('../../data/raw/adstai_DB.csv', 
                     usecols=['patid','S_Anxiety','STAI_AGE','T_Anxiety'])
adstai.columns = map(str.lower, adstai.columns)
adstai.set_index('patid', inplace=True)
data['adstai'] = adstai


# ADVS
# V3 Update:
#   * no changes necessary
#--------------------
# NOTE: what Dani calls "PrePregBMI" in the data dictionary is actually
#     "PREPREGBMI" in the CSV table
v3_advs_cols = ['patid','ARMCIRMM','BMIRI','HEIGHT','PREPREGBMI','PREPREGWEIGHT']
advs = pd.read_csv('../../data/raw/advs_DB.csv', 
                   usecols=v3_advs_cols)
advs.columns = map(str.lower, advs.columns)
advs.set_index('patid', inplace=True)
data['advs'] = advs


#===================================================
#===================================================
#===================================================


#--------------------
# V3 Update:  
#  * this is now where we remove twins
#  * we choose one of two maternal age vars here, and
#    one of two fetal sex vars
#-------------------------
def join_all_tables(
    sex='gender2',
    age='mat_age',
):
    tbl1 = pd.DataFrame()
    for tbl2 in data.keys():
        tbl1 = tbl1.join(data[tbl2], how='outer')
    tbl1.drop(tbl1.index[tbl1.twin2 > 0], inplace=True)
    tbl1.drop('twin2', axis=1, inplace=True)
    if sex.lower() != 'fetussex':
        # * we have two fetal sex vars, gender2 and fetussex
        # * gender2 seems to be more populated and better quality,
        #   so we drop fetussex by default
        tbl1.drop('fetussex', axis=1, inplace=True)
    if age.lower() != 'stai_age':
        # * we have two maternal age vars, mat_age and stai_age
        # * both are basically the same, except taken a few months
        #   a part (and stai_age is fractional while mat_age only
        #   integer)
        # * we use mat_age by default
        tbl1.drop('stai_age', axis=1, inplace=True)
    tbl1.fillna(-999999, inplace=True)
    return tbl1

#---------------------------------------------------------------------
# NOTE: When modeling, make sure to remove all targets from input set:
#     'LaborType_SpontaneousOrAugmented_DB', 'Cesarean2', 'DLVRY_DT', 
#     'DLVRYGA_DYS_SBadj', 'DLVRYBefore28wks', 'DLVRYBefore34Wks', 
#     'DLVRYGA_DYS'
#---------------------------------------------------------------------
democlinical = join_all_tables()
democlinical.to_csv('../../data/interim/democlinical_20191210_KU.csv')
