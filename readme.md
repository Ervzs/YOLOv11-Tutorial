# YOLOv11 Tutorial

## Labeling Dataset from scratch
Watch and follow the instruction for [Labeling images](https://www.youtube.com/watch?v=r0RspiLG260&t=574s)

If you have labeled dataset already then skip this step.

## Setup Virtual Environment

1. Download and install [Python 3.10](https://www.python.org/downloads/) if you haven't already.
2. Check if Python is installed:
   ```sh
   python3 --version
   ```
3. Set Python 3.10 as your default. You can change this in System Environment.
4. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

## Install Dependencies

1. Visit [PyTorch](https://pytorch.org/) and choose the appropriate compute platform based on your GPU. 
###
2. To determine your CUDA version, run:
   ```sh
   nvidia-smi
   ```
###
   Select the matching or lower CUDA version when installing PyTorch.
   Remove torchaudio and 3 in pip before entering in the terminal
###   
3. Install Ultralytics YOLO:
   ```sh
   pip install ultralytics
   ```
   
4. Verify installation:
   ```sh
   yolo help
   ```

## Prepare Dataset

1. Use `split-datasets.py` to split your dataset:
   - 80% for training
   - 20% for validation
  
## Why do we need this split?

### Training Set (80%):

This portion of the data is used to train the YOLO model.
The model learns patterns, object features, and relationships from this dataset.
The larger the training set, the better the model can generalize to unseen images.

### Validation Set (20%):

This is used to evaluate the model during training but not used for learning.
It helps monitor the model’s performance and adjust hyperparameters (e.g., learning rate, batch size).
Prevents overfitting—where the model memorizes training images but performs poorly on new images.
##
2. Create a `data.yaml` file and follow the format provided in the repository. This file will be used for training.

## Train the Model

Start training using the following command:
```sh
yolo detect train data=C:\YOLO-Test\playing-card\data.yaml model=yolo11s.pt epochs=150 patience=20 imgsz=640 batch=-1
```
After training, it will show you the directory to where the model is saved.

## Test your Model
This will detect objects in your sample images:
```sh
yolo detect predict source=C:\_YOLO-Tutorial\Image-Test model=C:\_YOLO-Tutorial\runs\detect\train2\weights\best.pt
```

## Notes
- Ensure all dependencies are properly installed before training.
- Adjust `epochs` and `imgsz` according to your requirements.


---


