<template>
  <div class="container">
    <UploadSection
      title="🎤 발표 음성 업로드"
      description="발표 음성 파일을 업로드하면, 텍스트로 변환한 뒤 AI 심사위원의 반응을 시뮬레이션해드려요."
      accept=".mp3,.wav"
      actionText="심사위원 반응 시뮬레이션 출력"
      :onProcess="analyzeVoice"
      nextRoute="/voice-result" 
    />
  </div>
  <!-- template 내에서 -->
  <button
    v-if="uploadedFileName"
    class="generate-button"
    @click="handleAction"
    >
    {{ actionText || "생성하기" }}
  </button>
</template>

<script setup>
import { ref } from 'vue'
import UploadSection from './common/UploadSection.vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  title: String,
  description: String,
  actionText: String,
  accept: String,
  onProcess: Function,     // 처리 콜백
  nextRoute: String        // 결과 페이지로 이동할 경로
})

const router = useRouter()
const fileInput = ref(null)
const uploadedFile = ref(null)
const uploadedFileName = ref('')

const triggerFileInput = () => fileInput.value?.click()

const handleFileChange = (e) => {
  uploadedFile.value = e.target.files[0]
  if (uploadedFile.value) {
    uploadedFileName.value = uploadedFile.value.name
  }
}

const handleAction = async () => {
  if (props.onProcess) {
    await props.onProcess(uploadedFile.value)
  }
  if (props.nextRoute) {
    router.push(props.nextRoute)
  }
}
</script>

<style scoped>
.container {
  padding: 40px;
}
</style>