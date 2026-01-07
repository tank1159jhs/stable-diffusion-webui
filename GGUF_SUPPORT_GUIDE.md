# GGUF 파일 지원 가이드

## 🚨 현재 문제
- **visionRealisticGGUFQ4_v2FluxDev.gguf** 파일이 인식되지 않습니다
- SD WebUI lean 버전은 **SafeTensors만** 지원합니다
- GGUF는 llama.cpp/Flux 전용 포맷입니다

## ⚠️ GGUF 파일 특징
- **GGUF** = GGML Universal Format
- **용도**: llama.cpp, Flux, 경량 모델 (양자화)
- **장점**: 파일 크기 작음 (Q4 양자화 = 4bit)
- **단점**: SD WebUI 기본 지원 안 함

## ✅ 해결 방법 1: SafeTensors 버전 사용 (권장) ⭐

### **Realistic Vision V5.1 SafeTensors 다운로드**

1. **CivitAI에서 다운로드**
   ```
   https://civitai.com/models/4201/realistic-vision-v51
   ```

2. **파일 선택**
   - ✅ `realisticVisionV51_v51VAE.safetensors` (pruned, ~2.1GB)
   - ❌ GGUF 버전은 선택하지 마세요

3. **파일 이동**
   ```bash
   mv ~/Downloads/realisticVisionV51_v51VAE.safetensors \
      /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/
   ```

4. **GGUF 파일 삭제 (또는 백업)**
   ```bash
   mv /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/visionRealisticGGUFQ4_v2FluxDev.gguf \
      ~/Downloads/backup/
   ```

5. **SD WebUI 재시작**
   ```bash
   cd /Users/systemi/stable-diffusion-webui
   ./webui.sh --port 7861
   ```

### **장점:**
- ✅ 즉시 작동 (코드 수정 불필요)
- ✅ 안정적인 로딩
- ✅ SD WebUI 100% 호환

---

## 🔧 해결 방법 2: GGUF 지원 추가 (고급, 비추천)

### **필요한 작업:**

1. **gguf 라이브러리 설치**
   ```bash
   pip install gguf
   ```

2. **sd_models.py 수정 (복잡)**
   ```python
   import gguf
   
   def load_model():
       if MODEL_FILENAME.endswith('.gguf'):
           # GGUF 로드 로직 (복잡)
           reader = gguf.GGUFReader(MODEL_FILENAME)
           # ... 텐서 변환 로직
       else:
           # 기존 SafeTensors 로드
           state_dict = safetensors.torch.load_file(MODEL_FILENAME)
   ```

3. **GGUF → PyTorch 텐서 변환**
   - GGUF는 양자화 포맷이므로 역양자화 필요
   - 복잡한 변환 로직 작성 필요

### **단점:**
- ❌ 매우 복잡함 (100줄+ 코드)
- ❌ 불안정할 수 있음
- ❌ SD WebUI lean 취지에 맞지 않음
- ❌ 양자화 해제 시 메모리 증가

---

## 📊 SafeTensors vs GGUF 비교

| 항목 | SafeTensors | GGUF |
|------|-------------|------|
| **SD WebUI 지원** | ✅ 기본 지원 | ❌ 미지원 |
| **파일 크기** | ~2-5GB | ~1-3GB (양자화) |
| **품질** | 최고 (FP16/FP32) | 약간 낮음 (Q4) |
| **로딩 속도** | 빠름 | 빠름 |
| **안정성** | 매우 높음 | 보통 |
| **호환성** | 모든 SD 툴 | llama.cpp, Flux |

---

## 🎯 권장 사항

### **일반 사용자: SafeTensors 사용** ⭐⭐⭐⭐⭐
```bash
# 1. GGUF 파일 제거
rm /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/visionRealisticGGUFQ4_v2FluxDev.gguf

# 2. SafeTensors 다운로드
# https://civitai.com/models/4201/realistic-vision-v51
# realisticVisionV51_v51VAE.safetensors

# 3. 파일 이동 후 재시작
```

### **고급 사용자: GGUF 컨버터 사용**
```bash
# GGUF → SafeTensors 변환 (Python 스크립트 필요)
python convert_gguf_to_safetensors.py \
  visionRealisticGGUFQ4_v2FluxDev.gguf \
  realisticVisionV51.safetensors
```

---

## 🆘 문제 해결

### Q: GGUF 파일을 꼭 써야 하나요?
A: ❌ 아니요. SD WebUI는 SafeTensors를 권장합니다.

### Q: GGUF가 용량이 작은데 왜 SafeTensors를 써야 하나요?
A: GGUF는 **양자화**(품질 손실)로 용량을 줄인 것입니다. SafeTensors는 원본 품질을 유지합니다.

### Q: GGUF를 SafeTensors로 변환할 수 있나요?
A: 이론적으로는 가능하지만, **양자화 해제**가 필요하고 품질이 완전히 복구되지 않습니다.

### Q: 6.3GB GGUF vs 2.1GB SafeTensors, 왜 GGUF가 더 큰가요?
A: `visionRealisticGGUFQ4_v2FluxDev.gguf`는 **Flux Dev 모델**일 수 있습니다. Flux는 SD 1.5보다 큰 모델입니다.

---

## 🚀 빠른 해결 (추천)

```bash
# 1. GGUF 파일 백업
mkdir -p ~/Downloads/backup_models
mv /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/visionRealisticGGUFQ4_v2FluxDev.gguf \
   ~/Downloads/backup_models/

# 2. CivitAI에서 SafeTensors 다운로드 (브라우저)
# https://civitai.com/models/4201/realistic-vision-v51
# realisticVisionV51_v51VAE.safetensors

# 3. 다운로드한 파일 이동
mv ~/Downloads/realisticVisionV51_v51VAE.safetensors \
   /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/

# 4. 확인
ls -lh /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/

# 5. SD WebUI 재시작
cd /Users/systemi/stable-diffusion-webui
./webui.sh --port 7861
```

---

## 📝 요약

- ❌ **GGUF 파일**: SD WebUI lean 버전 미지원
- ✅ **SafeTensors 파일**: SD WebUI 표준 포맷
- 🎯 **권장**: Realistic Vision V5.1 SafeTensors 다운로드
- ⚡ **효과**: 즉시 작동, 최고 품질

**제작일**: 2026년 1월 2일  
**목적**: GGUF vs SafeTensors 이해 및 해결
