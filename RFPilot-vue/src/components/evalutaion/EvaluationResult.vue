<script setup>
import { onMounted, ref } from 'vue'
import SidebarMenu from '../common/SidebarMenu.vue'

const score = ref(0)
const summary = ref('')
const evaluations = ref('')

onMounted(() => {
  const data = JSON.parse(sessionStorage.getItem('evaluation_result'))
  if (data) {
    score.value = Math.round(data.average_similarity * 100)
    summary.value = `가장 유사한 문장: ${data.most_similar_sentences.join('\n')} \n\n가장 덜 유사한 문장: ${data.least_similar_sentences.join('\n')}`
    evaluations.value = data.evaluated_sentences.join('\n\n')
  }
})
</script>

<template>
  <div class="result-container">
    <SidebarMenu />

    <section class="content">
      <h1>자료 평가 결과</h1>

      <div class="score-line">
        <span>적합도 점수는</span>
        <strong class="score">{{ score }}점</strong>
        <span>입니다!</span>
      </div>

      <div class="block">
        <h4>요약</h4>
        <textarea readonly>{{ summary }}</textarea>
      </div>

      <div class="block">
        <h4>AI 심사위원 평가</h4>
        <img src="../../assets/judges.png" alt="Judging Robots" class="judges" />
        <textarea readonly>{{ evaluations }}</textarea>
      </div>
    </section>
  </div>
</template>

  
  <style scoped>
  .result-container {
    display: flex;
    height: 100vh;
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  .content {
    flex: 1;
    padding: 40px 60px;
  }
  
  .content h1 {
    font-size: 28px;
    margin-bottom: 28px;
    color: #1e2a39;
  }
  
  .score-line {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
    font-size: 18px;
  }
  
  .score-line .score {
    font-size: 28px;
    color: #1e2a39;
    font-weight: 700;
  }
  
  .block {
    margin-bottom: 32px;
  }
  
  .block h4 {
    font-size: 16px;
    margin-bottom: 12px;
    color: #1e2a39;
  }
  
  textarea {
    width: 100%;
    height: 100px;
    padding: 14px;
    font-size: 14px;
    border: 1px solid #ddd;
    border-radius: 8px;
    resize: none;
  }
  
  .judges {
    margin: 12px 0;
    width: 200px;
  }
  </style>