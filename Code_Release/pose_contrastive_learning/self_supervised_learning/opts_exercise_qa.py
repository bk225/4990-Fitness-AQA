# =========================
# Basic Training Parameters
# =========================

base_learning_rate = 0.001
train_batch_size_2dcnn = 16
test_batch_size_2dcnn = 16
max_epochs = 20

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

ssl_trajectories_dir = "PATH_TO_TRAJECTORIES/"
ssl_frames_dir = "PATH_TO_FRAMES/"
train_val_test_sets_dir = "PATH_TO_SPLITS/"

# =========================
# Other Training Settings
# =========================

model_ckpt_interval = 5
