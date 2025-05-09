<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import UploadSection from '../common/UploadSection.vue'
import axios from 'axios'

const router = useRouter()
const fileInputRef = ref(null)

onMounted(() => {
  // UploadSection의 파일 input을 직접 참조
  fileInputRef.value = document.querySelector('input[type="file"]')
  if (fileInputRef.value) {
    fileInputRef.value.addEventListener('change', handleFileChange)
  }
})

const handleFileChange = async (e) => {
  const file = e.target.files[0]
  if (!file) return

  const formData = new FormData()
  formData.append('file', file)

  try {
    const response = await axios.post(
      'http://localhost:8000/analyze-similarity',
      formData,
      { headers: { 'Content-Type': 'multipart/form-data' } }
    )

    // 결과를 세션스토리지에 저장
    sessionStorage.setItem('evaluation_result', JSON.stringify(response.data))

    // 결과 페이지로 이동
    router.push('/evaluation-result')
  } catch (error) {
    alert('평가 중 오류가 발생했습니다: ' + error.message)
  }
}
</script>

<template>
  <UploadSection
    title="📊 자료적합도 평가"
    description="업로드한 발표 자료를 기반으로, 제안서와의 연관성을 AI 심사위원이 평가합니다."
    accept=".pdf,.doc,.docx,.hwp"
    nextRoute="/evaluation-result"
  />
</template>
