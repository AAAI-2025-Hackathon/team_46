# Check-In

- Title of your submission: **Efficient Models for Infacts Cardiac Health and Bone Fracture Detection**
- Team Members: [Nikhileswara Rao Sulake](mailto:nikhil01446@gmail.com), [Sai Manikanta Eswar Machara](mailto:macharasaimanikantaeswar@gmail.com)
- [x] All team members agree to abide by the [Hackathon Rules](https://aaai.org/conference/aaai/aaai-25/hackathon/)
- [x] This AAAI 2025 hackathon entry was created by the team during the period of the hackathon, February 17 – February 24, 2025
- [ ] The entry includes a 2-minute maximum length demo video here: [Link](#)
- [x] The entry clearly identifies the selected theme in the README and the video.



## Team 46
### Theme : AI for Healthcare


#### Team Members: 
1. **Nikhileswara Rao Sulake**   
   - GitHub: [Nikhil-Rao20](https://github.com/Nikhil-Rao20)  
   - LinkedIn: [Nikhileswara Rao Sulake](https://www.linkedin.com/in/nikhileswara-rao-sulake-847802254/)

2. **Sai Manikanta Eswar Machara**  
   - GitHub: [EswarMachara](https://github.com/EswarMachara)
   - LinkedIn: [Sai Manikanta Eswar Machara](https://www.linkedin.com/in/sai-manikanta-eswar-machara)

### University & Location:
- **RGUKT, Nuzvid**, India  
- **B.Tech in Computer Science and Engineering, 2nd Year**  

------


## Project Idea:
This project comes under AI for HealthCare Theme. While various medical image modalities like MRI, CT, XRay are the main target of the research in current going medical image trend, there are various modalities like
UOT, EIT, MSOT, Radiomics and Pediatrics. In this project, we target to solve one of the most critical problem, **Pediatrics**. We recognize that two significantly concerning issues often encountered by infants are Bone Fractures and Heart Diseases. While it is acknowledged that there are numerous challenges, for the purposes of this research associated with the hackathon, we will confine our focus to these two topics. 

## Track 1
### **1) Multi-Task Left Ventricular Segmentation and Ejection Fraction determination from Pediatric Echocardiograms**

**Reason of Study**:   Echocardiography is one of the most widely **applicable**, **safe**, and **cost-effective** diagnostic tools available in cardiovascular medicine [[James N Kirkpatrick]](https://pubmed.ncbi.nlm.nih.gov/30459125/#:~:text=Echocardiography%20is%20one%20of%20the%20most%20widely%20applicable%2C%20safe%2C%20and%20cost%2Deffective%20diagnostic%20tools%20available%20in%20cardiovascular%20medicine.) . One of the studies highlights the main challenges encountered when initially students learn echocardiography and what might be helpful during the learning process. These findings could be useful in developing curriculums or new teaching materials for echocardiography. One suggestion is to create digital resources such as **virtual laboratories** (vLABs) [[Anna Dieden]](https://pubmed.ncbi.nlm.nih.gov/31196099/#:~:text=This%20study%20shows,virtual%20laboratories%20(vLABs).) . Recent studies have explored AI-enhanced frameworks aimed at automating echocardiographic assessments. However, extensive research is still needed to validate these technologies in clinical settings [[James P McDonald]](https://pubmed.ncbi.nlm.nih.gov/31290034/) . Studies have also shown that 3D echocardiography is significantly better for analyzing features that are not as clearly present in 2D imaging, which is the currently dominant modality. Although 3D echocardiography is still an area of active research [[Victor Chien-Chia Wu]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5364152/#:~:text=Several%20important%20advantages,2D%20echocardiography%20(2DE).), the quality and quantity of research on 2D imaging remain insufficient to fully understand its modalities and drive novel contributions. One particularly underexplored area is pediatric echocardiography. The main challenge in echocardiographic datasets is left ventricular segmentation and ejection fraction determination.

**Current Methodology and State-of-the-Art (SOTA)**:    In the [EchoNet Pediatric Dataset](https://echonet.github.io/pediatric/), the state-of-the-art model has achieved a Dice score of around **0.89** and **3.6%** MSE for segmentation and ejection fraction estimation, respectively [[Charitha D Reddy]](https://pubmed.ncbi.nlm.nih.gov/36754100/#:~:text=EchoNet%2DPeds%20segments%20the%20left%20ventricle%20with%20a%20Dice%20similarity%20coefficient%20of%200.89.%20EchoNet%2DPeds%20estimates%20EF%20with%20a%20mean%20absolute%20error%20of%203.66%25). Typically, two separate models are used—one for segmentation and another for ejection fraction determination, where the latter takes echocardiographic video as input and produces a numerical output. The R(2+1)D model is commonly used for Ejection Fraction task. 

However, we propose a **multitask model** that processes echocardiogram videos and simultaneously performs both left ventricle **segmentation** and ejection fraction **determination** based on systolic and diastolic volumes. This is the core idea of Task 1.

----

## Track 2
### **2) Efficient Bone Fracture Detection in Infacts using Enhanced YOLO Model**
**Reason for Study:**
Accurate detection of bone fractures in infants is crucial, as undiagnosed fractures can lead to severe complications and may be indicative of underlying conditions, including non-accidental trauma. Traditional diagnostic methods rely heavily on the expertise of radiologists, but the increasing demand for imaging services has led to significant workloads and potential delays in diagnosis. To address these challenges, the integration of Artificial Intelligence (AI) into radiological practices has emerged as a promising solution. AI-enhanced imaging tools have demonstrated potential in improving diagnostic accuracy and efficiency, thereby supporting healthcare professionals in making timely and informed decisions.

Mark Chapman, director of HealthTech at the National Institute for Health and Care Excellence (NICE), stated:
> [*"Using AI technology to help highly skilled professionals in urgent care centres to identify which of their patients has a fracture could potentially speed up diagnosis and reduce follow-up appointments needed because of a fracture missed during an initial assessment."*](https://www.nice.org.uk/news/articles/ai-technologies-recommended-for-use-in-detecting-fractures?utm_source=chatgpt.com#:~:text=%E2%80%9CUsing%20AI%20technology%20to%20help%20highly%20skilled%20professionals%20in%20urgent%20care%20centres%20to%20identify%20which%20of%20their%20patients%20has%20a%20fracture%20could%20potentially%20speed%20up%20diagnosis%20and%20reduce%20follow%20up%20appointments%20needed%20because%20of%20a%20fracture%20missed%20during%20an%20initial%20assessment.%E2%80%9D%C2%A0)

Similarly, a systematic review highlighted that AI models, such as convolutional neural networks, have demonstrated superior accuracy, sensitivity, and specificity in diagnosing bone fractures compared to traditional methods [[Mohammed Kutbi]](https://www.mdpi.com/2075-4418/14/17/1879#:~:text=It%20evaluates%20the%20performance%20of%20various%20AI%20models%2C%20such%20as%20convolutional%20neural%20networks%20(CNNs)%2C%20in%20diagnosing%20bone%20fractures%2C%20highlighting%20their%20superior%20accuracy%2C%20sensitivity%2C%20and%20specificity%20compared%20to%20traditional%20diagnostic%20methods). Given these developments, exploring advanced AI models, such as modified versions of the YOLO algorithm, for infant bone fracture detection is both timely and essential.

**Current Methodology and State-of-the-Art (SOTA):**
In the domain of infant bone fracture detection, traditional diagnostic methods primarily rely on radiological skeletal surveys interpreted by experienced radiologists. However, the integration of Artificial Intelligence (AI) into this field has led to significant advancements. Recent studies have explored the application of deep learning models to enhance diagnostic accuracy and efficiency. For instance, a study by Rui-Yang Ju and Weiming Cai applied the YOLOv8 algorithm to pediatric wrist trauma X-ray images, achieving a mean average precision (mAP) of **0.638**, surpassing previous models. 
[[Rui-Yang Ju]](https://arxiv.org/abs/2304.05071)

Another study conducted a comparative analysis of various deep learning models for bone fracture detection, reporting the following performance metrics:
- **Convolutional Neural Network (CNN) on X-ray images:** Accuracy of **95%**, Sensitivity of **94%**, Specificity of **96%**.  
- **Hybrid CNN-Recurrent Neural Network (RNN) on CT scans:** Accuracy of **97%**, Sensitivity of **96%**, Specificity of **98%**.  
- **Transfer Learning CNN on MRI images:** Accuracy of **93%**, Sensitivity of **92%**, Specificity of **94%**.  
[[S. Hareesh]](https://ijcrt.org/viewfull.php?&p_id=IJCRT2410106)

We propose an **enhanced YOLO** model, with pre-processsing technique that significantly improves the accuracy and efficiency of **infant bone fracture detection**. This is the core idea of Task 2. 



-----
