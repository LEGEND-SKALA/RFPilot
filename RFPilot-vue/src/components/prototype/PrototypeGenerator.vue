<!-- PrototypeUpload.vue -->
<template>
  <UploadSection
    title="📄 프로토타입 생성"
    description="업로드된 파일의 양식에 맞춰 프로토타입을 생성해드립니다."
    accept=".pdf,.doc,.docx,.hwp"
    actionText="생성하기"
    nextRoute="/prototype-result"
  />
</template>

<script setup>
import UploadSection from './common/UploadSection.vue'
</script>