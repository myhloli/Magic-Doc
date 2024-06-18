
from magic_pdf.model.doc_analyze_by_pp_structurev2 import CustomPaddleModel
from magic_doc.utils import split_to_chunks
import paddle 
from concurrent.futures import ThreadPoolExecutor, as_completed


class SeqPaddle:
    def __init__(self, **kwargs):
        self.model = CustomPaddleModel(ocr=True, show_log=False)

    def __call__(self, params):
        """
        params: list[(idx, image, *args)]
        """
        results = [] 
        for idx, img in params:
            ocr_res = self.model(img)
            results.append((idx, ocr_res))

        return results 
