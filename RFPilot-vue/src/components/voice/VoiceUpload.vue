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
  formData.append('file', file)
  formData.append('user_panel_count', 3)
  formData.append('doc_title', 'AI,디지털 기반 방송프로그램 제작지원 사업 추가 공고문.pdf') // ✅ 필요 시 동적으로 변경

  try {
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

    router.push('/voice-result')
  } catch (err) {
    console.error('❌ 평가 실패:', err)
    alert('서버 평가 요청에 실패했습니다.')
  }
}
</script>