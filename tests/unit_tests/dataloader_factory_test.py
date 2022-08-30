import unittest

from torch.utils.data import DataLoader

from super_gradients.training.dataloaders.dataloader_factory import coco2017_train, coco2017_val, \
    coco2017_train_ssd_lite_mobilenet_v2, coco2017_val_ssd_lite_mobilenet_v2, cityscapes_train, cityscapes_val, \
    cityscapes_stdc_seg50_train, cityscapes_stdc_seg50_val
from super_gradients.training.datasets import COCODetectionDataset
from super_gradients.training.datasets.segmentation_datasets import CityscapesDataset


class DataLoaderFactoryTest(unittest.TestCase):
    def test_coco2017_train_creation(self):
        dl_train = coco2017_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, COCODetectionDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_coco2017_val_creation(self):
        dl_val = coco2017_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, COCODetectionDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_coco2017_train_ssdlite_mobilenet_creation(self):
        dl_train = coco2017_train_ssd_lite_mobilenet_v2()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, COCODetectionDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_coco2017_val_ssdlite_mobilenet_creation(self):
        dl_val = coco2017_val_ssd_lite_mobilenet_v2()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, COCODetectionDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_cityscapes_train_creation(self):
        dl_train = cityscapes_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, CityscapesDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_cityscapes_val_creation(self):
        dl_val = cityscapes_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, CityscapesDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_cityscapes_stdc_reg50_train_creation(self):
        dl_train = cityscapes_stdc_seg50_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, CityscapesDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_cityscapes_stdc_reg50_val_creation(self):
        dl_val = cityscapes_stdc_seg50_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, CityscapesDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_cityscapes_stdc_reg75_train_creation(self):
        dl_train = cityscapes_stdc_seg50_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, CityscapesDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_cityscapes_stdc_reg75_val_creation(self):
        dl_val = cityscapes_stdc_seg50_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, CityscapesDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_cityscapes_segreg48_train_creation(self):
        dl_train = cityscapes_stdc_seg50_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, CityscapesDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_cityscapes_segreg48_val_creation(self):
        dl_val = cityscapes_stdc_seg50_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, CityscapesDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)

    def test_cityscapes_ddrnet_train_creation(self):
        dl_train = cityscapes_stdc_seg50_train()
        self.assertTrue(isinstance(dl_train, DataLoader))
        self.assertTrue(isinstance(dl_train.dataset, CityscapesDataset))
        it = iter(dl_train)
        for _ in range(10):
            next(it)

    def test_cityscapes_ddrnet_val_creation(self):
        dl_val = cityscapes_stdc_seg50_val()
        self.assertTrue(isinstance(dl_val, DataLoader))
        self.assertTrue(isinstance(dl_val.dataset, CityscapesDataset))
        it = iter(dl_val)
        for _ in range(10):
            next(it)


if __name__ == '__main__':
    unittest.main()
