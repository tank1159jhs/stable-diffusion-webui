import os
import torch
import safetensors.torch
from omegaconf import OmegaConf
from modules import paths, devices, sd_vae
import modules.shared

# lean: Realistic Vision 모델 사용 (일본 배경/풍경 특화)
# 다운로드: https://civitai.com/models/4201/realistic-vision-v51
# 실제 파일명: realisticVisionV60B1_v51HyperVAE.safetensors
MODEL_FILENAME = os.path.abspath(os.path.join(paths.models_path, "Stable-diffusion", "realisticVisionV60B1_v51HyperVAE.safetensors"))

# Fallback: japaneseDollLikeness (MODEL_FILENAME이 없으면 자동 폴백)
FALLBACK_MODEL = os.path.abspath(os.path.join(paths.models_path, "Stable-diffusion", "japaneseDollLikeness.safetensors"))

# 모델 파일 존재 확인 및 폴백
if not os.path.exists(MODEL_FILENAME):
    print(f"⚠️ 모델 없음: {os.path.basename(MODEL_FILENAME)}")
    if os.path.exists(FALLBACK_MODEL):
        print(f"✅ Fallback 모델 사용: {os.path.basename(FALLBACK_MODEL)}")
        MODEL_FILENAME = FALLBACK_MODEL
    else:
        raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {MODEL_FILENAME}")

# CheckpointInfo 클래스 정의 (AUTOMATIC1111 호환)
class CheckpointInfo:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.basename(filename)
        self.model_name = os.path.splitext(os.path.basename(filename))[0]
        self.hash = self.model_name
        self.shorthash = self.model_name[:10]
        self.sha256 = self.model_name
        self.name = self.title
        self.name_for_extra = self.title

# checkpoints_list를 CheckpointInfo 객체 리스트로 변경
_checkpoint_info = CheckpointInfo(MODEL_FILENAME)
checkpoints_list = [_checkpoint_info]
checkpoint_aliases = {os.path.basename(MODEL_FILENAME): _checkpoint_info}
model_path = os.path.dirname(MODEL_FILENAME)

class ModelData:
    def __init__(self):
        self.sd_model = None

    def set_sd_model(self, model):
        self.sd_model = model

    def get_sd_model(self):
        return self.sd_model

model_data = ModelData()

def load_model():
    if model_data.sd_model is not None:
        modules.shared.sd_model = model_data.sd_model
        return model_data.sd_model
    # safetensors 로드
    state_dict = safetensors.torch.load_file(MODEL_FILENAME, device=devices.get_optimal_device_name())
    # config.yaml 자동 매칭 (japaneseDollLikeness.yaml이 있으면 사용, 없으면 v1-inference.yaml)
    config_path = os.path.splitext(MODEL_FILENAME)[0] + ".yaml"
    if not os.path.exists(config_path):
        config_path = os.path.join(paths.script_path, "configs", "v1-inference.yaml")
    sd_config = OmegaConf.load(config_path)
    # 모델 인스턴스화
    from ldm.util import instantiate_from_config
    model = instantiate_from_config(sd_config.model)
    # state_dict 키가 'state_dict'로 한 번 더 래핑되어 있을 수 있음
    if isinstance(state_dict, dict) and 'state_dict' in state_dict:
        state_dict = state_dict['state_dict']
    model.load_state_dict(state_dict, strict=False)
    model = model.to(devices.device)
    # lean: 강제 device 속성 패치 (macOS/mps/cpu 환경에서 CUDA 참조 방지)
    if hasattr(model, 'cond_stage_model'):
        if hasattr(model.cond_stage_model, 'device'):
            # 강제로 device를 devices.device로 덮어씀
            model.cond_stage_model.device = devices.device
    model.eval()
    # lean: AUTOMATIC1111 호환 더미 속성 일괄 할당
    class DummyCheckpointInfo:
        name_for_extra = os.path.basename(MODEL_FILENAME)
        title = os.path.basename(MODEL_FILENAME)
        filename = MODEL_FILENAME
        model_name = "japaneseDollLikeness"
        hash = "japaneseDollLikeness"
        info = "japaneseDollLikeness"
        def __init__(self):
            self.name = os.path.basename(MODEL_FILENAME)
            self.title = os.path.basename(MODEL_FILENAME)
            self.filename = MODEL_FILENAME
            self.model_name = "japaneseDollLikeness"
            self.hash = "japaneseDollLikeness"
            self.info = "japaneseDollLikeness"
            self.lowvram = False  # <-- lowvram 속성 더미로 추가
    model.sd_checkpoint_info = DummyCheckpointInfo()
    # 주요 모델 속성 일괄 패치
    def patch_missing_attrs(obj, attrs):
        for k, v in attrs.items():
            if not hasattr(obj, k):
                setattr(obj, k, v)
    patch_missing_attrs(model, {
        "is_sdxl": False,
        "is_sd3": False,
        "is_onnx": False,
        "is_sdxl_inpaint": False,  # SDXL inpaint 여부도 False로 고정
        "latent_channels": 4,
        "sd_model_hash": "japaneseDollLikeness",
        "sd_model_name": "japaneseDollLikeness",
        "sd_model_filename": MODEL_FILENAME,
        "sd_model_title": "japaneseDollLikeness",
        "sd_model_info": "japaneseDollLikeness",
        "lowvram": False,  # <-- lowvram 속성 더미로 추가
    })
    patch_missing_attrs(model.sd_checkpoint_info, {
        "model_name": "japaneseDollLikeness",
        "hash": "japaneseDollLikeness",
        "info": "japaneseDollLikeness",
    })
    # lean: textual inversion embedding init 더미 메서드 monkey patch
    def dummy_encode_embedding_init_text(self, text, n):
        return torch.zeros((n, 768))
    if not hasattr(model.cond_stage_model, "encode_embedding_init_text"):
        import types
        model.cond_stage_model.encode_embedding_init_text = types.MethodType(dummy_encode_embedding_init_text, model.cond_stage_model)
    model_data.sd_model = model
    modules.shared.sd_model = model  # <-- 반드시 shared에 등록
    # VAE 로드(옵션, 에러 무시)
    try:
        sd_vae.load_vae(model, None, None)
    except Exception:
        import traceback
        print("[경고] VAE 로드 중 오류 무시:")
        traceback.print_exc()
    return model

def get_model():
    return load_model()

def setup_model():
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 setup_model 함수 추가.
    내부적으로 get_model()만 호출.
    """
    get_model()

def list_models():
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 list_models 함수 추가.
    단일 모델(japaneseDollLikeness.safetensors)만 반환.
    """
    return [MODEL_FILENAME]

def get_closet_checkpoint_match(name):
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 get_closet_checkpoint_match 함수 추가.
    단일 모델(japaneseDollLikeness.safetensors)만 지원.
    """
    # name이 japaneseDollLikeness.safetensors와 일치하면 반환, 아니면 None
    if name == os.path.basename(MODEL_FILENAME) or name == MODEL_FILENAME:
        return MODEL_FILENAME
    return None

def checkpoint_tiles(use_short=False):
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 checkpoint_tiles 함수 추가.
    단일 모델(japaneseDollLikeness.safetensors)만 지원.
    """
    if use_short:
        return [os.path.basename(MODEL_FILENAME)]
    else:
        return [MODEL_FILENAME]

def unload_model_weights():
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 unload_model_weights 함수 추가.
    단일 모델 환경에서는 실제로 아무 작업도 하지 않음.
    """
    model_data.sd_model = None
    return True

def reload_model_weights():
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 reload_model_weights 함수 추가.
    단일 모델 환경에서는 아무 작업도 하지 않음.
    """
    return True

def apply_token_merging(model, value):
    """
    기존 AUTOMATIC1111 코드와의 호환성을 위해 apply_token_merging 함수 추가.
    단일 모델 환경에서는 아무 작업도 하지 않음.
    """
    return

def apply_alpha_schedule_override(model, p):
    """
    AUTOMATIC1111 호환: alpha schedule 관련 기능을 lean 환경에서는 무시 (더미 함수)
    """
    return
