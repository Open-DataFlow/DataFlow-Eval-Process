from dataflow.data import DataFlowDataset
from dataflow.core import ScoreRecord
from datasets import Dataset
class Filter():

    def __init__(self, args=None):
        pass

    def filter_func(self):
        pass
    
    def __call__(self, dataset: DataFlowDataset):
        pass

class TextFilter(Filter):
    
    def __init__(self, args=None):
        self.data_type = "text"
        
    def __call__(self, dataset):
        init_len = len(dataset)
        score_record = ScoreRecord()
        dataset.set_score_record(score_record)
        labels = self.filter_func(dataset)
        if isinstance(dataset.dataset, Dataset):
            def filter_by_labels(example, index):
                return labels[index] == 1
            dataset.dataset = dataset.dataset.filter(filter_by_labels, with_indices=True)
            filtered_dataset = dataset
        else:
            filtered_dataset = dataset.filter(labels)

        print(f'Implemented {self.filter_name}. Data Number: {init_len} -> {len(filtered_dataset)}', flush=True)
        return filtered_dataset

class ImageFilter(Filter):
    
    def __init__(self, args=None):
        super().__init__()
        self.data_type = "image"
        
    def __call__(self, dataset: DataFlowDataset):
        init_len = len(dataset)
        score_record = ScoreRecord()
        dataset.set_score_record(score_record)
        filtered_dataset = dataset.filter(self.filter_func(dataset))
        print(f'Implemented {self.__class__.__name__}. Data Number: {init_len} -> {len(filtered_dataset)}')

        return filtered_dataset

class ImageTextFilter(Filter):
    
    def __init__(self, args=None):
        super().__init__()
        self.data_type = "image_caption"
        
    def __call__(self, dataset: DataFlowDataset):
        init_len = len(dataset)
        score_record = ScoreRecord()
        dataset.set_score_record(score_record)
        filtered_dataset = dataset.filter(self.filter_func(dataset))
        print(f'Implemented {self.__class__.__name__}. Data Number: {init_len} -> {len(filtered_dataset)}')

        return filtered_dataset

class VideoFilter(Filter):
    
    def __init__(self, args=None):
        self.data_type = "video"
        
    def __call__(self, dataset: DataFlowDataset):
        score_record = ScoreRecord()
        dataset.set_score_record(score_record)
        filtered_dataset = dataset.filter(self.filter_func(dataset))
        print(filtered_dataset.get_indices())
        return filtered_dataset

class VideoTextFilter(Filter):
    
    def __init__(self, args=None):
        self.data_type = "video_caption"
        
    def __call__(self, dataset: DataFlowDataset):
        score_record = ScoreRecord()
        dataset.set_score_record(score_record)
        filtered_dataset = dataset.filter(self.filter_func(dataset))
        print(filtered_dataset.get_indices())
        return filtered_dataset