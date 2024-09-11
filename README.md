# Photo capturing
This repo was created to collect ground truth images. We assume that you have installed `Python3.10` and the "IntelSense" driver and library from the root repo pointing to this one. Otherwise you won't be able to run this application.

> Note: You will need to plug the camera of the Cobot to the usb-c port of the PC

## Setup
create a `python3.10` virtual environment by typing the following command in the terminal:

```bash
python3.10 -m venv .venv
```

Then install all dependencies by:

```bash
pip install -r requirements.txt
```

Afterwards run:

```bash
python main.py
```

This will open a window showing the pciture of the camera.

## Instructions

- The 's' key on your keyboard will save the image as `png` beginning with gt, the formatted UTC time including seconads and ms, and the count for the base name in the `.gt/` directory, e.g:  'gt_2024-09-04_14-26-59_1.png'
- It will also create the corresponding `txt` file with the same base name as the image
- The 'q' key will quit the application
- The `resize.py` is just for testing the resizing of images and inspecting its quality. NO actual use for it. 

> Note: You can run this app just for demonstration. The actual images are already moved in another repo
