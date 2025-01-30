# YOLOv11 Tutorial

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
2. Create a `data.yaml` file and follow the format provided in the repository. This file will be used for training.

## Train the Model

Start training using the following command:
```sh
yolo detect train data=C:/_YOLO-Tutorial/data.yaml model=yolo11n.pt epochs=50 imgsz=640
```

## Test your Model
This will detect objects in your sample images:
```sh
yolo detect predict source=C:\_YOLO-Tutorial\Image-Test model=C:\_YOLO-Tutorial\runs\detect\train2\weights\best.pt
```

## Notes
- Ensure all dependencies are properly installed before training.
- Adjust `epochs` and `imgsz` according to your requirements.


---


