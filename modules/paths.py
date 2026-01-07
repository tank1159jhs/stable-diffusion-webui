import os
import sys
from modules.paths_internal import models_path, script_path, data_path, extensions_dir, extensions_builtin_dir, cwd  # noqa: F401
import modules.safe  # noqa: F401

# Only support minimal SD 1.5 (japaneseDollLikeness) setup, no SDXL/sgm/BLIP/midas etc.
sys.path.insert(0, script_path)

# Find ldm path (Stable Diffusion core)
sd_path = None
possible_sd_paths = [os.path.join(script_path, 'repositories/stable-diffusion-stability-ai'), '.', os.path.dirname(script_path)]
for possible_sd_path in possible_sd_paths:
    if os.path.exists(os.path.join(possible_sd_path, 'ldm/models/diffusion/ddpm.py')):
        sd_path = os.path.abspath(possible_sd_path)
        break

if sd_path is not None:
    ldm_path = os.path.join(sd_path, 'ldm')
    k_diffusion_path = os.path.join(sd_path, '../k-diffusion')
    if os.path.exists(ldm_path):
        if ldm_path not in sys.path:
            sys.path.append(ldm_path)
    if os.path.exists(os.path.join(k_diffusion_path, 'k_diffusion/sampling.py')):
        k_diff_abs = os.path.abspath(k_diffusion_path)
        if k_diff_abs not in sys.path:
            sys.path.insert(0, k_diff_abs)
# No BLIP, sgm, SDXL, or other model support

# 기존 경로 변수들
paths = {
    "Stable Diffusion": os.path.abspath(os.path.join(script_path, "repositories", "stable-diffusion-stability-ai")),
    # 필요시 추가 경로 키를 여기에 정의
}

# No dynamic path_dirs, no fake modules, no warnings, no legacy code
