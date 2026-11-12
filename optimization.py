# optimization.py
import os
import onnxruntime as ort

def use_optimization(max_threads=None):
    available = len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else (os.cpu_count() or 4)
    threads = max_threads if max_threads is not None else available

    if not getattr(ort.InferenceSession, "_is_patched", False):
        _orig_session = ort.InferenceSession

        def _custom_session(path_or_bytes, sess_options=None, **kwargs):
            if sess_options is None:
                sess_options = ort.SessionOptions()
            sess_options.intra_op_num_threads = threads
            sess_options.inter_op_num_threads = 1
            return _orig_session(path_or_bytes, sess_options=sess_options, **kwargs)

        _custom_session._is_patched = True
        ort.InferenceSession = _custom_session

    return threads
