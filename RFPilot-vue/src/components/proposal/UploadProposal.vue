<template>
  <div class="container">
    <div class="left">
      <img src="../../assets/logo.png" alt="RFPilot Logo" class="logo" />
      <h2 class="subtitle">
        RFP 작성과 발표, AI가 함께 준비해주는<br />
        스마트 심사 시뮬레이션
      </h2>
      <p class="description">
        내가 만든 제안서, 어떻게 평가받을지 궁금하신가요?<br />
        지금 파일을 올려보세요.
      </p>

      <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        style="display: none"
        accept=".pdf,.doc,.docx,.hwp"
      />

      <!-- 업로드 버튼 -->
      <button class="upload-button" @click="triggerFileInput">
        <span>{{ uploadedFileName || "파일 업로드 하기" }}</span>
      </button>

      <!-- 생성하기 버튼: 파일이 업로드된 경우에만 표시 -->
      <button
        v-if="uploadedFileName"
        class="generate-button"
        @click="goToSummary"
      >
        생성하기
      </button>
    </div>


    <div class="right">
      <img src="../../assets/homerobot.png" alt="AI Robot" class="robot" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const fileInput = ref(null)
const uploadedFileName = ref('')
const router = useRouter()

const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    uploadedFileName.value = file.name
  }
}

const goToSummary = () => {
  router.push('/summary') // 반드시 라우터에 이 경로 등록되어 있어야 함
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100vh;
  padding: 0 150px; /* 공통 padding */
  box-sizing: border-box;
}
.left,
.right {
  max-width: 50%;
}



.logo {
  width: 180px;
  margin-bottom: 20px;
}

.subtitle {
  font-size: 1.4rem;
  font-weight: 600;
  color: #1e2a39;
  margin-bottom: 24px;
}

.description {
  font-size: 1rem;
  color: #333;
  line-height: 1.6;
  margin-bottom: 32px;
}

.upload-button,
.generate-button {
  background-color: #1e2a39;
  color: #ffffff;
  padding: 12px 20px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  align-items: center;
  display: flex;
  gap: 8px;
  margin-bottom: 12px;
}

.upload-button:hover,
.generate-button:hover {
  background-color: #32425a;
}

.robot {
  width: 600px;
  max-width: 100%;
}
</style>