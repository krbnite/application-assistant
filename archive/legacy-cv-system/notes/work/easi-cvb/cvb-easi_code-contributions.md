
# DL/HAR Related
| Project | Code | Comments |
|---------|------|----------|
| Gestures, Sensornet | Original GesturesNet 1DCNN-LSTM model | ...nuff said |
| Apnea-ECG, Sensornet, Data Augmentation | Warp Tools | Implements fcn similar to some paper |
| Apnea-ECG, Gestures, Sensornet | Generalized/Enhanced Gestures-1DCNN-LSTM Model | A more robust, flexible, bells-and-whistles-ed version of my INT003 model |
| Sensornet, Experimental Data Aug | Homotopic Augmentation |  Original idea for augmenting dataset by homotopically combining records |
| Sensornet, Experimental Data Aug | Noise Injection (w/ focus on its analysis) | Computation showing how much noise to inject |
| Sensornet, Exp Data Aug | Circulated Augmentations | ..... |


# Helper Tools
| Reuseable Bash Tools | positional_enforcement.sh, etc | how-to scripts for making bash fcns |
| Reuseable Bash Tools | EC2 Bashrc file | ... |
| AWS/Ec2 Helper Tools | ec2 (function) | Convenient awsclie wrapper fcn (e.g., ec2 start kevin) |
| AWS/Ec2 Helper Tools | awsusr (fcn) | quick and easy aws acct changer (e.g., awsuser idms, awsusr easi, etc) |
| Reuseable Bash Tools, Git Helper Tools  | git-mkref.sh | Easily update our Markdown reference tables in team repo |
| Git Helper Tools | Git aliases file | .... |
| Git Helper Tools | Git config file | .... |
| Git Helper Tools | Git Enhancement Tools (Examples) | tricks for using `git myFcn` where my Fcn can be Bash/Python/Etc script |
| Python Debugging Helper Tools | load_my_pkg_from_anywhere, reload_my_pkg, etc | simple, byte-sized code snippets for re-use |
| Docker Helper Scripts | e.g., base_docker.sh and docker.sh in apnea-ecg project | Supposed to be useful across projects, but at minimum it's just useful |
| Conda Env Scripts | e.g., in Apnea-ECG or SleepViz | To help easily recreate envs (usually just a simple wrapper over 1-2 conda cmds + a yml file) |



# Frozen Projects...

| Project | Code | Comments |
|---------|------|----------|
| NSL Examples | notebooks | was trying to do some graph DL type stuff if I recall |
| Rett Analysis Plan | a few notebooks tinkering... | Unsupervised time series segmentation, etc (vision written in various places; should be in write-ups |
 



# Computing Environments
| Project | Env Type | Comments |
|---------|----------|----------|
| Apnea-ECG | Docker | An early attempt at establishing "best practices"; includes helper scripts to properly startup Docker Image/File |
| EEG-WG | Conda | Attempts platform-independent build; starts w/ a suggestive yml file (constrained only to python version and channels to retrieve pkgs) and creates a temporary conda env; it then identifies Conda's solution to each requested pkg and creates a new yml file by updating the original w/ the sol'n's pkg versions (not for all pkgs in evn, but for the few specified in original temp yml file); uses the documented temp env to build a non-conda-listed eeg pkg (autoreject) using `conda skeleton`; it first builds on my macbook, then converts the build to many other OS architectures; finally, the platform-ind env can be built by anyone now...same basic env but now can specify the os-arch for the eeg autoreject pkg; the env is uploaded to anaconda acct (though havne't used that feature) |
| INT003/Gestures | Conda | Env solved for both MacOS and Linus; much simpler style than the EEG env! |
| SleepViz | Conda | Simple like INT003 (but w/ different specs); comes w/ some helper-tool bash scripts |

| 
