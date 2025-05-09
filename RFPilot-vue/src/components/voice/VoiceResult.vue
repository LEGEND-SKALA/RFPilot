<template>
  <ResultView
    title="🎤 발표 평가 결과"
    :score="score"
    :sections="sections"
  />
</template>

<script setup>
import { useRoute } from 'vue-router'

import { ref } from 'vue'
import ResultView from '../../components/common/ResultView.vue'

const route = useRoute()

const score = ref(Number(sessionStorage.getItem('voice_score') || 0))
const transcript = sessionStorage.getItem('voice_transcript') || ''
const feedback = JSON.parse(sessionStorage.getItem('voice_feedback') || '[]')

const sections = ref([
  { label: '내용', text: transcript },
  {
    label: 'AI 심사위원 평가',
    text: feedback.join('\n\n')
  }
])
</script>