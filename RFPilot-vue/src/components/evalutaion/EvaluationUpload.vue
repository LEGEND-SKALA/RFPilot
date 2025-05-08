<template>
  <UploadSection
    title="📊 자료적합도 평가"
    description="업로드한 발표 자료를 기반으로, 제안서와의 연관성을 AI 심사위원이 평가합니다."
    accept=".pdf,.doc,.docx,.hwp"
    nextRoute="/evaluation-result"
  />
</template>

<script setup>
import UploadSection from '../common/UploadSection.vue'
</script>