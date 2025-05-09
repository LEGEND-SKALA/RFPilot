<template>
    <div class="loading-container">
      <!-- 상단 좌측 로고 -->
      <div class="logo-wrapper">
        <img src="../../assets/logo.png" alt="RFPilot Logo" class="logo" />
      </div>
  
      <!-- 메인 콘텐츠 -->
      <div class="content">
        <!-- 왼쪽: 로봇 이미지 -->
        <div class="left">
          <img src="../../assets/loading.png" alt="AI Robot" class="robot" />
        </div>
  
        <!-- 오른쪽: 텍스트 및 스피너 -->
        <div class="right">
          <div class="message">
            자료 분석 및 심사위원 초빙 중...
          </div>
          <div class="spinner-wrapper">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
<script setup>
  import { onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  onMounted(() => {
    const checkInterval = setInterval(() => {
      const result = sessionStorage.getItem('analysisResult')
      const error = sessionStorage.getItem('uploadError')
  
      if (result) {
        clearInterval(checkInterval)
        router.push('/summary')
      }
  
      if (error) {
        clearInterval(checkInterval)
        alert('분석 중 오류가 발생했습니다.')
        sessionStorage.removeItem('uploadError')
        router.push('/')
      }
    }, 1000) // check every 1s
  })
</script>
  
<style scoped>
.loading-container {
  position: relative;
  height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 20px 40px;
  box-sizing: border-box;
}

.logo-wrapper {
  position: absolute;
  top: 20px;
  left: 20px;
}

.logo {
  width: 200px;
}

.content {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 60px;
  flex-wrap: wrap; /* 반응형 처리 */
}

.left,
.right {
  flex: 1 1 300px; /* 최소 너비 300px로 줄어듦 */
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 20px;
}

.right {
  align-items: flex-start;
  text-align: left;
}

.robot {
  max-width: 100%;
  height: auto;
  max-height: 400px;
  margin-bottom: 16px;
}

.loading-text {
  font-weight: 600;
  font-size: 1.2rem;
  color: #333;
}

.message {
  font-size: 1.5rem;
  font-weight: bold;
  color: #1e2a39;
  margin-bottom: 20px;
}

.spinner-wrapper {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
</style>