# LLM推理优化（北航2024顶点课程课设）
## 使用
conda配置环境
```
git clone git@github.com:ILSparkle/Llama_Infer.git
conda create - n Llama_Infer
conda activate Llama_Infer 
pip install -r requirements.txt
```

huggingface代理设置（如果模型下载缓慢）
```
export HF_ENDPOINT=https://hf-mirror.com
```

运行 `python run.py` 来启动程序