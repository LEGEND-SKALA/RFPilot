<template>
  <UploadSection
    title="발표 스크립트 업로드"
    description="발표 내용을 담은 스크립트를 업로드해보세요. 구조를 분석해드릴게요!"
    accept=".txt,.docx,.pdf"
    nextRoute="/script-analysis"
  />
</template>

<script setup>
import UploadSection from '../common/UploadSection.vue'
</script>
