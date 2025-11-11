# Deep Learning: Revolution and Modern Use Cases

**Presenter:** Muhammed Hassan Mukhtar  
**Duration:** 45 min + Live Demos  
**Tone:** Engaging, Fact-Packed, Decision-Focused  

---

## Learning Outcomes
After completing this session, you will be able to:
- Choose the right CNN architecture for your computer vision tasks.
- Understand the transition from ANNs → CNNs → ViTs → ConvNeXt.
- Run LLMs locally using Ollama and integrate them with LangChain and LangGraph.
- Utilize Vector Databases for retrieval-augmented generation (RAG) systems.
- Design AI pipelines combining Computer Vision (CV) and Natural Language Processing (NLP) systems.

---

## Key Topics Covered
1. Revolution of Computer Vision  
   - ANN vs CNN  
   - Modern CNN Architectures (LeNet to ConvNeXt)  
   - Vision Transformers (ViT)  
   - Hybrid Models (MSCViT)  

2. Revolution in NLP  
   - From RNNs and LSTMs to Transformers  
   - Emergence of LLMs, RAG, and Agentic Systems  
   - LangChain, LangGraph, and Vector Databases  

3. Hands-On Examples  
   - ConvNeXt v2 Nano Fine-Tuning  
   - MSCViT Tiny Model Training  
   - Ollama LLaMA 3.2 Local Deployment  
   - LangChain + RAG + LangGraph Integration  
   - ReAct Agent for Self-Correcting Tasks  

---

## Key Algorithms and Papers (References)

| Algorithm / Model | Paper / Reference |
|-------------------|-------------------|
| LeNet (CNN foundation) | [Yann LeCun et al., Gradient-Based Learning Applied to Document Recognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf) |
| AlexNet (2012) | [Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton – ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) |
| VGGNet (2014) | [Karen Simonyan, Andrew Zisserman – Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) |
| GoogLeNet / Inception (2014) | [Szegedy et al. – Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842) |
| ResNet (2015) | [He, Zhang, Ren, Sun – Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) |
| Inception-v3 (2015) | [Szegedy et al. – Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567) |
| Xception (2016) | [François Chollet – Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357) |
| MobileNet (2017) | [Howard et al. – MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) |
| SENet (2017) | [Hu et al. – Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) |
| DenseNet (2017) | [Huang et al. – Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993) |
| EfficientNet (2019) | [Tan and Le – EfficientNet: Rethinking Model Scaling for CNNs](https://arxiv.org/abs/1905.11946) |
| Vision Transformer (2020) | [Dosovitskiy et al. – An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) |
| ConvNeXt (2022) | [Liu et al. – A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545) |
| MSCViT (2025) | [Liu et al. – Multi-Scale Convolutional Vision Transformer](https://arxiv.org/abs/2501.06040) |
| LangChain Framework | [LangChain GitHub](https://github.com/langchain-ai/langchain) |
| LangGraph | [LangGraph GitHub](https://github.com/langchain-ai/langgraph) |
| ReAct Agent (2022) | [Yao et al. – ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) |
| FAISS (Vector Search) | [Johnson et al. – Billion-Scale Similarity Search with GPUs](https://arxiv.org/abs/1702.08734) |

---

## GitHub and Code Resources

| Tool / Framework | Repository / Resource |
|------------------|----------------------|
| Ollama (Local LLMs) | [https://github.com/jmorganca/ollama](https://github.com/jmorganca/ollama) |
| FAISS (Vector Database for RAG) | [https://github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss) |
| Deep Learning Tutorials and Demos by Muhammed Hassan Mukhtar | [https://github.com/MHM-Rajpoot/Deep-Learning/tree/main/Tutorial/Week%2007](https://github.com/MHM-Rajpoot/Deep-Learning/tree/main/Tutorial/Week%2007) |
| ├── ReAct Math Agent.ipynb | [ReAct Math Agent.ipynb](https://github.com/MHM-Rajpoot/Deep-Learning/blob/main/Tutorial/Week%2007/ReAct%20Math%20Agent.ipynb) |
| ├── Prompt Engineering, LangChain, and LangGraph.ipynb | [Prompt Engineering, LangChain, and LangGraph.ipynb](https://github.com/MHM-Rajpoot/Deep-Learning/blob/main/Tutorial/Week%2007/Prompt%20Engineering%2C%20LangChain%2C%20and%20LangGraph.ipynb) |
| ├── Old School Natural Language Processing.ipynb | [Old School Natural Language Processing.ipynb](https://github.com/MHM-Rajpoot/Deep-Learning/blob/main/Tutorial/Week%2007/Old%20School%20Natural%20Language%20Processing.ipynb) |
| ├── ConvNeXt V2 Nano _ MSCViT Candy Classifier.ipynb | [ConvNeXt V2 Nano _ MSCViT Candy Classifier.ipynb](https://github.com/MHM-Rajpoot/Deep-Learning/blob/main/Tutorial/Week%2007/ConvNeXt%20V2%20Nano%20_%20MSCViT%20Candy%20Classifier.ipynb) |
| └── Old School Computer Vision.ipynb | [Old School Computer Vision.ipynb](https://github.com/MHM-Rajpoot/Deep-Learning/blob/main/Tutorial/Week%2007/Old%20School%20Computer%20Vision.ipynb) |

---

## Example Use Cases

### Computer Vision
- Object Classification and Detection using CNNs, ResNet, EfficientNet, YOLO  
- Image Segmentation using SAM, Mask R-CNN, and DeepLab  
- Object Tracking with DeepSORT and ByteTrack  
- Hybrid CV models with MSCViT for high-accuracy segmentation and detection  

### NLP and Generative AI
- Local Model Deployment using Ollama and LLaMA 3.2  
- Context-Aware Chatbots using LangChain with RAG and Vector Databases  
- Reasoning Agents using ReAct for self-correcting problem solving  

---

## How to Use This README  
1. Share this README with your attendees or include in your slide deck as a reference at the end.  
2. Provide links to the papers and code so participants can deep-dive after the talk.  
3. Encourage participants to clone the GitHub repos and run the Colab notebooks—for hands-on practice.

---

## Acknowledgements  
Thanks to all the open-source authors and researchers in the object detection and tracking community whose work underpins this presentation.

---

## License  
You may distribute these slides/README freely for educational purposes. Please cite original papers when referencing ideas.
