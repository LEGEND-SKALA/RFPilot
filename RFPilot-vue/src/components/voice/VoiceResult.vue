<template>
  <ResultView
    title="🎤 발표 평가 결과"
    :score="score"
    :sections="sections"
  />
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import ResultView from '../components/common/ResultView.vue'
import axios from 'axios'

// 파일과 심사위원 수를 params로 전달받음
const route = useRoute()
const uploadedFile = route.query.file // Blob 객체가 아님에 주의
const panelCount = route.query.panelCount || 3

const score = ref(0)
const sections = ref([])

onMounted(async () => {
  try {
    const formData = new FormData()
    formData.append('file', uploadedFile)
    formData.append('user_panel_count', panelCount)

    const response = await axios.post('http://127.0.0.1:8000/pitch-evaluation', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })

    const data = response.data
    score.value = data.suitability_score || 0
    sections.value = [
      { label: '요약', text: data.transcript },
      {
        label: 'AI 심사위원 평가',
        image: '/assets/judges.png',
        text: data.panel_feedback.join('\n\n')
      }
    ]
  } catch (error) {
    console.error('음성 평가 요청 실패:', error)
  }
})
</script>