DATA_LIST              = '../data/annotations/info.json'
TRAIN                  = '../data/annotations/train.jsonl'
VAL                    = '../data/annotations/val.jsonl'
TEST_CLASSIFICATION_GT = '../data/annotations/test_cls.gt.jsonl'
TEST_DETECTION_GT      = '../data/annotations/test_det.gt.jsonl'
TEST_CLASSIFICATION    = '../data/annotations/test_cls.jsonl'


RECALL_N               = (1, 5)
SIZE_RANGES            = [
    ('all', (0., 4096.)),
    ('large', (32., 4096.)),
    ('medium', (16., 32.)),
    ('small', (0., 16.)),
]
ATTRIBUTES             = [
    'occluded',
    'bgcomplex',
    'distorted',
    'raised',
    'wordart',
    'handwritten',
]
MAX_DET_PER_IMAGE      = 1000
IOU_THRESH             = .5