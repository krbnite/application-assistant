"""
This code is basically just a copy-and-paste from
JNB 02b__KU in the ./notebooks/ directory, which is where I
actually created the files... This code was extracted to
make it easier on the next person, if any.
"""

import pandas as pd




#####################################################
#########            TOI                #############
#####################################################
toi = pd.read_csv('../data/raw/Fetal_Toitu_Physio_Features_Early_Signal_093019.csv')
# Drop "meta data" cols (Dec 10, 2019)
#   Question: Drop these now, or develop file to drop them if we choose to at model time?
#     -- some of these are definite drops (e.g., age, site, filename), but some
#        of the data quality vars might inform a random forest...who knows...
toi_drop_cols = ['F1_hrsegs1', 'F1_totsegs1', 'F1_totsegs4', 'F1_ccsegs4',
                'F1_MVT_PWR_numberSegments.1', 'F1_MVT_PWR_numberUsedPwrCoh',
                'F2_hrsegs1', 'F2_totsegs1', 'F2_totsegs4', 'F2_ccsegs4',
                'F2_MVT_PWR_numberSegments.1', 'F2_MVT_PWR_numberUsedPwrCoh',
                'F31f_hrsegs1', 'F31f_totsegs1', 'F32f_hrsegs1', 'F32f_totsegs1',
                'F3_totsegs4', 'F3_ccsegs4',
                'F3_MVT_PWR_numberSegments.1', 'F3_MVT_PWR_numberUsedPwrCoh']
toi.drop(toi_drop_cols, axis=1, inplace=True)
# Standardize (lowercase, patid index)
toi.columns = map(str.lower, toi.columns)
toi.set_index('patid', inplace=True)
# Remove All-NaN Rows
valid_index = ~(toi.isnull().sum(axis=1) == toi.columns.__len__())
toi = toi[valid_index]
# Drop Duplicated IDs
duplicated_IDs = toi.reset_index().groupby('patid')['patid'].count().to_frame('cnt').query('cnt > 1').index
toi.drop(duplicated_IDs, inplace=True)
toi_wide = toi  # naming convention for consistency

    

#####################################################
#########           MON RMSSD           #############
#####################################################
rmssd = pd.read_csv('../data/raw/BISH_RMSSD_MONICA_052218_EARLY_SIGNAL2.csv')
# Drop "meta data" cols
#   Question: Drop these now, or develop file to drop them if we choose to at model time?
#     -- some of these are definite drops (e.g., age, site, filename), but some
#        of the data quality vars might inform a random forest...who knows...
rmssd_drop_cols = ['Age', 'Site', 'FileName', 'F1_Total', 'F1_AS Total',
     'F1_QS Total', 'F1_AS Reject', 'F1_QS Reject', 'F1_ASR%',
     'F1_QSR%', 'F2_Study ID +', 'F2_Study ID', 'F2_Study ID.1', 'F2_Study ID.2',
     'F2_Site', 'F2_Total', 'F2_AS Total', 'F2_QS Total', 'F2_AS Reject',
     'F2_QS Reject', 'F2_ASR%', 'F2_QSR%', 'F3_Study ID +', 'F3_Study ID',
     'F3_Study ID.1', 'F3_Study ID.2', 'F3_Site', 'F3_Total',
     'F3_AS Total', 'F3_QS Total', 'F3_AS Reject', 'F3_QS Reject',
     'F3_ASR%', 'F3_QSR%', ]
rmssd.drop(rmssd_drop_cols, axis=1, inplace=True)
# Standardize (lower case, patid index)
rmssd.columns = map(str.lower, rmssd.columns)
rmssd.set_index('patid', inplace=True)
keep_only_f1 = False
drop_f3 = False
if keep_only_f1:
    f12f_vars = [var for var in rmssd.columns 
           if 'f1' in var and '2f' in var]
    rmssd = rmssd[f12f_vars]
rmssd_wide = rmssd  # naming convention for consistency
# You might choose to drop F3 data at this step, or leave it in for 
#   downstream dropping....




#####################################################
#########             MON MHR           #############
#####################################################
mhr = pd.read_csv('../data/raw/Maternal HR XFER 052318.csv')
mhr.columns = map(str.lower, mhr.columns)
mhr.set_index('patid', inplace=True)
# Drop "meta data" cols
mhr_drop_cols = ['file name', 'numbersegments', 'meanpercentbad',
                'startsecond', 'endsecond', 'numbersegments.1', 
                'numberusedpwrcoh', 'numberusedcrscor']
mhr.drop(mhr_drop_cols, axis=1, inplace=True)
# BAND POWER
mhr['bandpwr'] = mhr.mhr_bandpwr1 + mhr.mhr_bandpwr2 + mhr.mhr_bandpwr3 + mhr.mhr_bandpwr4
mhr['relative_bandpwr1'] = mhr.mhr_bandpwr1/mhr.bandpwr
mhr['relative_bandpwr2'] = mhr.mhr_bandpwr2/mhr.bandpwr
mhr['relative_bandpwr3'] = mhr.mhr_bandpwr3/mhr.bandpwr
mhr['relative_bandpwr4'] = mhr.mhr_bandpwr1/mhr.bandpwr
mhr1 = mhr.query("timepoint=='F1'").drop('timepoint', axis=1)
mhr1.columns = map(lambda x: 'f1_'+x, mhr1.columns)
mhr2 = mhr.query("timepoint=='F2'").drop('timepoint', axis=1)
mhr2.columns = map(lambda x: 'f2_'+x, mhr2.columns)
mhr3 = mhr.query("timepoint=='F3'").drop('timepoint', axis=1)
mhr3.columns = map(lambda x: 'f3_'+x, mhr3.columns)
# Widening
mhr_wide = mhr1.join(mhr2, how='outer').join(mhr3, how='outer')
# You might choose to drop F3 data at this step, or leave it in for 
#   downstream dropping....



#####################################################
#########             MON MVMT          #############
#####################################################
mvmt = pd.read_csv('../data/raw/maternal_MVMT_monica_EHG_EHG_XFER_240s_Epochs_051818.csv')
mvmt['cid'] = mvmt['Study ID'].apply(lambda x: x.split('-')[-1] if type(x)==str else x)
mvmt['patid'] = mvmt['Study ID'].apply(lambda x: '-'.join(x.split('-')[:-2]))
mvmt.columns = mvmt.columns.to_frame().replace(' ','_',regex=True).iloc[:,0].map(str.lower).values
mvmt.set_index('patid', inplace=True)
# Drop "meta data" cols
mvmt_drop_cols = ['study_id', 'file_name', 'studyid', 'numbersegments', 
                  'meanpercentbad','startsecond', 'endsecond', 'numbersegments__1', 
                  'numberusedpwrcoh', 'numberusedcrscor', ]
mvmt.drop(mvmt_drop_cols, axis=1, inplace=True)
# BAND POWER
## Heart Rate
mvmt['hr_bandpwr'] = mvmt.hr_bandpwr1 + mvmt.hr_bandpwr2 + mvmt.hr_bandpwr3 + mvmt.hr_bandpwr4
mvmt['hr_relative_bandpwr1'] = mvmt.hr_bandpwr1/mvmt.hr_bandpwr 
mvmt['hr_relative_bandpwr2'] = mvmt.hr_bandpwr2/mvmt.hr_bandpwr 
mvmt['hr_relative_bandpwr3'] = mvmt.hr_bandpwr3/mvmt.hr_bandpwr 
mvmt['hr_relative_bandpwr4'] = mvmt.hr_bandpwr4/mvmt.hr_bandpwr 
## Movement
mvmt['mvt_bandpwr'] = mvmt.mvt_bandpwr1 + mvmt.mvt_bandpwr2 + mvmt.mvt_bandpwr3 + mvmt.mvt_bandpwr4
mvmt['mvt_relative_bandpwr1'] = mvmt.mvt_bandpwr1/mvmt.mvt_bandpwr 
mvmt['mvt_relative_bandpwr2'] = mvmt.mvt_bandpwr2/mvmt.mvt_bandpwr 
mvmt['mvt_relative_bandpwr3'] = mvmt.mvt_bandpwr3/mvmt.mvt_bandpwr 
mvmt['mvt_relative_bandpwr4'] = mvmt.mvt_bandpwr4/mvmt.mvt_bandpwr 
# MVMT Widening
mvmt1 = mvmt.query("cid=='10'").drop('cid', axis=1)
mvmt1.columns = map(lambda x: 'cid10_'+x, mvmt1.columns)
mvmt2 = mvmt.query("cid=='15'").drop('cid', axis=1)
mvmt2.columns = map(lambda x: 'cid15_'+x, mvmt2.columns)
mvmt3 = mvmt.query("cid=='20'").drop('cid', axis=1)
mvmt3.columns = map(lambda x: 'cid20_'+x, mvmt3.columns)
mvmt_wide = mvmt1.join(mvmt2, how='outer').join(mvmt3, how='outer')
# You might choose to drop F3 data at this step, or leave it in for 
#   downstream dropping....


#----------------------------------------------------------
# Dec 12: Put instrument name in front of col names
#----------------------------------------------------------
toi_wide.columns = map(lambda x: 'sensor_toi_' + x, toi_wide.columns)
rmssd_wide.columns = map(lambda x: 'sensor_monrmssd_' + x,
                         rmssd_wide.columns)
mhr_wide.columns = map(lambda x: 'sensor_monmhr_' + x, mhr_wide.columns)
mvmt_wide.columns = map(lambda x: 'sensor_monmvmt_' + x, mvmt_wide.columns)


#----------------------------------------------------------
# JOIN
#----------------------------------------------------------
# All MON
mon_wide_all = rmssd_wide.\
        join(mhr_wide, how='outer').\
        join(mvmt_wide, how='outer')

# All Sensors
sensors = toi_wide.join(mon_wide_all, how='outer')


#----------------------------------------------------------
# SAVE
#----------------------------------------------------------
toi_wide.to_csv('../../data/interim/toi_20191209_KU.csv')
rmssd_wide.to_csv('../../data/interim/mon-rmssd_20191209_KU.csv')
mhr_wide.to_csv('../../data/interim/mon-mhr_20191209_KU.csv')
mvmt_wide.to_csv('../../data/interim/mon-mvmt_20191209_KU.csv')
mon_wide_all.to_csv('../../data/interim/mon-all_20191209_KU.csv')
sensors.to_csv('../../data/interim/sensors-all_20191209_KU.csv')
