from PIL import Image
from ultralytics import YOLO
import torch


def detect_img(model_name,path):

    if model_name == "YOLOv8":
        model = YOLO('models/best_ori.pt')  # select model
    elif model_name == "YOLOv8+small_target":
        model = YOLO('models/best_small_target.pt')  # select model
    elif model_name == "final_model":
        model = YOLO('models/best_final.pt')  # select model

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    results = model(path,device=device)  # results list

    # show the results
    for r in results:
        im_array = r.plot()  # plot a RGB numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('./results/images/results.jpg')  # save image
