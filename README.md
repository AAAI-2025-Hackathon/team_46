## Team 46
### Theme : AI for Healthcare


#### Team Members: 
1. **Nikhileswara Rao Sulake**   
   - GitHub: [Nikhil-Rao20](https://github.com/Nikhil-Rao20)  
   - LinkedIn: [Nikhileswara Rao Sulake](https://www.linkedin.com/in/nikhileswara-rao-sulake-847802254/)
   - Email: nikhil01446@gmail.com

2. **Sai Manikanta Eswar Machara**  
   - GitHub: [EswarMachara](https://github.com/EswarMachara)
   - LinkedIn: [Sai Manikanta Eswar Machara](https://www.linkedin.com/in/sai-manikanta-eswar-machara)
   - Email: macharasaimanikantaeswar@gmail.com
### University & Location:
- **RGUKT, Nuzvid**, India  
- **B.Tech in Computer Science and Engineering, 2nd Year**  

------


## Project Idea:
This project comes under AI for HealthCare Theme. While various medical image modalities like MRI, CT, XRay are the main target of the research in current going medical image trend, there are various modalities like
UOT, EIT, MSOT, Radiomics and Pediatrics. In this project, we target to solve one of the most critical problem, **Pediatrics**. We recognize that two significantly concerning issues often encountered by infants are Bone Fractures and Heart Diseases. While it is acknowledged that there are numerous challenges, for the purposes of this research associated with the hackathon, we will confine our focus to these two topics. 

## Track 1
### **1) Multi-Task Left Ventricular Segmentation and Ejection Fraction determination from Pediatric Echocardiograms**

**Reason of Study**:   Echocardiography is one of the most widely **applicable**, **safe**, and **cost-effective** diagnostic tools available in cardiovascular medicine [[James N Kirkpatrick]](https://pubmed.ncbi.nlm.nih.gov/30459125/#:~:text=Echocardiography%20is%20one%20of%20the%20most%20widely%20applicable%2C%20safe%2C%20and%20cost%2Deffective%20diagnostic%20tools%20available%20in%20cardiovascular%20medicine.) . One of the studies highlights the main challenges encountered when initially students learn echocardiography and what might be helpful during the learning process. These findings could be useful in developing curriculums or new teaching materials for echocardiography. One suggestion is to create digital resources such as **virtual laboratories** (vLABs)[[Anna Dieden]](https://pubmed.ncbi.nlm.nih.gov/31196099/#:~:text=This%20study%20shows,virtual%20laboratories%20(vLABs).) . Recent studies have explored AI-enhanced frameworks aimed at automating echocardiographic assessments. However, extensive research is still needed to validate these technologies in clinical settings [[James P McDonald]](https://pubmed.ncbi.nlm.nih.gov/31290034/) . Studies have also shown that 3D echocardiography is significantly better for analyzing features that are not as clearly present in 2D imaging, which is the currently dominant modality. Although 3D echocardiography is still an area of active research [[Victor Chien-Chia Wu]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5364152/#:~:text=Several%20important%20advantages,2D%20echocardiography%20(2DE).), the quality and quantity of research on 2D imaging remain insufficient to fully understand its modalities and drive novel contributions. One particularly underexplored area is pediatric echocardiography. The main challenge in echocardiographic datasets is left ventricular segmentation and ejection fraction determination.

**Current Methodology and SOTA**:    In the [EchoNet Pediatric Dataset](https://echonet.github.io/pediatric/), the state-of-the-art model has achieved a Dice score of around **0.89** and **3.6%** MSE for segmentation and ejection fraction estimation, respectively [[Charitha D Reddy]](https://pubmed.ncbi.nlm.nih.gov/36754100/#:~:text=EchoNet%2DPeds%20segments%20the%20left%20ventricle%20with%20a%20Dice%20similarity%20coefficient%20of%200.89.%20EchoNet%2DPeds%20estimates%20EF%20with%20a%20mean%20absolute%20error%20of%203.66%25). Typically, two separate models are used—one for segmentation and another for ejection fraction determination, where the latter takes echocardiographic video as input and produces a numerical output. The R(2+1)D model is commonly used for Ejection Fraction task. 

However, we propose a **multitask model** that processes echocardiogram videos and simultaneously performs both left ventricle **segmentation** and ejection fraction **determination** based on systolic and diastolic volumes. This is the core idea of Task 1.

----

## Track 2
### **2) Efficient Bone Fracture Detection in Infacts using Modified YOLOv11 Model**

-----
