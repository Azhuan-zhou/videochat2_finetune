import os as __os  # add "__" if not want to be exported
from copy import deepcopy as __deepcopy

anno_root_it = "."

# ============== pretraining datasets=================
available_corpus = dict(
    # video
    caption_HumanML3D = [
        f"{anno_root_it}/HumanML3D/train.json", 
        "./HumanML3D",
        "video"]
)


available_corpus["videochat2_instruction"] = [
    available_corpus["caption_HumanML3D"]
]


# add smit
available_corpus["videochat2_instruction_new"] = [
    available_corpus["caption_HumanML3D"]
]


# add more high-quality data
available_corpus["videochat2_instruction_hd"] = [  
    available_corpus["caption_HumanML3D"]
]
