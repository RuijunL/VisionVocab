# Work Log | Vision Vocab 项目日志
> 用于记录项目阶段计划，成果展示，保证长期可维护性

---

## 项目成员
- 刘瑞钧 (Ruijun Liu)
- 兰青 (Qing Lan)

---

## 项目目标
一个基于图片识别的互动式词汇学习系统，用户可上传图片并点击图片中的区域，系统识别该区域中的物体，并展示词汇卡片（含词义、音标、例句等）。
> 本项目将组合 **image caption 模型** 与 **目标检测模型（如 YOLO）**，实现定位 + 描述能力的结合，从而支持交互式点击识别

---

## 文件管理结构
VisionVocab/
├── data/                                # 数据相关
│   ├── samples/                         # 测试图像
│   └── annotations.json                 # 人工标注真值（图中物体类别 + 坐标）
│
├── model_testing/                       # 模型测试代码
│   ├── run_combo.py                     # 跑模型组合（caption + detector）
│   ├── metrics.py                       # 评估指标 M1~M6 实现
│   └── combos.yaml                      # 模型组合配置文件
│
├── results/                             # 实验输出结果
│   ├── raw_outputs/                     # 模型原始输出（json）
│   ├── visualizations/                  # 可视化结果（检测框 + caption 图像）
│   └── summary_metrics.csv              # 所有组合的评估指标汇总
│
├── work_log.md                          # 项目开发过程日志


---

## 数据集说明
| 数据集名称     | 来源/链接 | 用途说明 |
|----------------|-----------|----------|
| COCO 2017 val  | [images](http://images.cocodataset.org/zips/val2017.zip), [annotations](http://images.cocodataset.org/annotations/annotations_trainval2017.zip) | 提取 10 张常见物体图片用于评估 caption + detection 组合性能 |
| Pascal VOC 2012 | http://host.robots.ox.ac.uk/pascal/VOC/ | 可选备用；类别少但结构简单，适合测试 |
| 自采图像（可选）| 本地图片，来自手机或网页截图 | 用于模拟用户实际上传场景 |

## 第一阶段目标：组合模型能力评估

### 说明
- image caption 模型（如 BLIP, GIT）具备优秀的图像描述能力，但**不提供位置信息**。
- 目标检测模型（如 YOLO）可以识别并框出图片中的每个物体，但不提供自然语言描述。
- 为实现“点击图像区域 → 得到物体名称”这一核心功能，**我们必须将两种模型能力结合**。

### 阶段目标
> 评估不同 image caption 模型 + 不同目标检测模型 的组合能力，选择效果最好的作为核心 pipeline。

### 使用指标编号
| 指标编号 | 名称                          | 含义                                 | 范围 | 备注             |
|----------|-------------------------------|--------------------------------------|------|------------------|
| M1       | Noun Coverage (NC)            | caption 是否提及了检测出的类别       | 0~1  | recall 类指标    |
| M2       | Caption Precision for Objects | caption 中的名词是否真实出现在图中   | 0~1  | precision 类指标 |
| M3       | Caption-Box F1                | M1 与 M2 的调和平均值                | 0~1  | 平衡性指标       |
| M4       | Click → Object Accuracy       | 点击区域返回的物体类别是否正确       | 0~1  | end-to-end 测试 |
| M5       | End-to-End Success Rate       | 是否成功展示词卡                     | 0~1  | 总体验指标       |
| M6       | 推理时间 / 图像（秒）         | 整个 pipeline 的单图耗时             | >0   | 影响实际部署体验 |


### 模型组合
| 组合编号 | Caption 模型 | Detector 模型 | NC (M1) | CPO (M2) | F1 (M3) | COA (M4) | E2ESR (M5) | 推理时间 (M6) | 模型备注                       |
|----------|---------------|----------------|---------|----------|---------|----------|------------|----------------|-------------------------------|
| C1       | BLIP          | YOLOv5s         |         |          |         |          |            |                | baseline 组合，轻量、推理快   |
| C2       | BLIP-2        | YOLOv8n         |         |          |         |          |            |                | 更强 caption + 最新 YOLO     |
| C3       | GIT           | YOLOv5m         |         |          |         |          |            |                | 微软模型，caption 连贯性强    |
| C4       | LLaVA         | GroundingDINO   |         |          |         |          |            |                | 多模态 + 高级检测模型（重）    |
| C5       | BLIP-2        | GroundingDINO   |         |          |         |          |            |                | 精准描述 + 定位               |
| C6       | BLIP          | YOLOv8n         |         |          |         |          |            |                | 轻量 caption + 精准 detector  |


