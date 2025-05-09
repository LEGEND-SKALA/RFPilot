<template>
  <UploadSection
    title="🎤 발표 음성 업로드"
    description="발표 음성 파일을 업로드하면, AI 심사위원의 평가 결과를 알려드립니다."
    accept=".mp3,.wav"
    actionText="AI 평가 실행"
    :onProcess="analyzeVoice"
    nextRoute="/voice-result"
  />
</template>

<script setup>
import UploadSection from '../../components/common/UploadSection.vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const analyzeVoice = async (file) => {
  console.log('📦 업로드할 파일:', file)
  const formData = new FormData()
  const fileName = sessionStorage.getItem('uploadedFileName')

  formData.append('file', file)
  formData.append('user_panel_count', 3)
  formData.append('doc_title', fileName)

  try {
    // ✅ 로딩 페이지로 이동 (요청 전이 아니라, 요청 직후에)
    sessionStorage.setItem('nextRoute', '/voice-result')
    router.push('/loading')

    const res = await axios.post('http://127.0.0.1:8000/pitch-evaluation', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })

    const result = res.data
    console.log('✅ 평가 결과:', result)

    sessionStorage.setItem('voice_transcript', result.transcript)
    sessionStorage.setItem('voice_feedback', JSON.stringify(result.panel_feedback))
    sessionStorage.setItem('voice_score', result.suitability_score)

    // ✅ 결과 페이지로 이동
    router.push('/voice-result')

  } catch (err) {
    console.error('❌ 평가 실패:', err)
    alert('서버 평가 요청에 실패했습니다.')

    // ✅ 실패 시 업로드 페이지로 다시 이동
    setTimeout(() => {
      router.push('/voice')
    }, 500)
  }
}
</script>