### Dataset and Directory Structure
This is the format of the dataset that is required to pasted in this repository to train your model.
```
-Dataset (current folder)

--A4C
---Videos
----Videos.avi
---FileList.csv
---VolumneTracings.csv

--PSAX
---Videos
----Videos.avi
---FileList.csv
---VolumneTracings.csv
```

After you put up this dataset in the said directory structure, then you are asked to run the 2 preprocessing file which are in the utils folder, `filelist_modi.py` and `volumetracings_modi.py`. This will create the finalized version of the dataset, from which you can start training the model.