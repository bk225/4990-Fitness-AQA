# =========================
# Basic Training Parameters
# =========================

base_learning_rate = 0.001
train_batch_size_2dcnn = 4
test_batch_size_2dcnn = 4
max_epochs = 2

randomseed = 42

# =========================
# Image / Input Settings
# =========================

input_resize_2dcnn = (224, 224)
H_2dcnn = 224
W_2dcnn = 224
C_2dcnn = 3

# =========================
# Dataset Paths (YOU MUST EDIT THESE)
# =========================

ssl_trajectories_dir = "/content/drive/MyDrive/Fitness-AQA_WORKING/OHP_REAL/trajectories/bar_trajectories_scalar/"
ssl_frames_dir = "/content/drive/MyDrive/Fitness-AQA_WORKING/OHP_REAL/frames_extracted/"
train_val_test_sets_dir = "/content/drive/MyDrive/Fitness-AQA_WORKING/OHP_REAL/Splits_SSL_TEMP/"

# =========================
# Other Training Settings
# =========================

model_ckpt_interval = 5
