<template>
    <header class="header">
      <img src="../../assets/logo.png" alt="RFPilot Logo" class="logo" />
      <div class="menu-wrapper">
        <button class="hamburger" @click="toggleMenu">☰</button>
        <div v-if="showMenu" class="dropdown">
          <button
            v-for="(item, index) in menuList"
            :key="index"
            class="dropdown-item"
            @click="navigate(item.route)"
          >
            {{ item.text }}
          </button>
        </div>
      </div>
    </header>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const showMenu = ref(false)
  const toggleMenu = () => (showMenu.value = !showMenu.value)
  
  const navigate = (path) => {
    if (path === '/') {
      sessionStorage.clear() 
    }
    router.push(path)
    showMenu.value = false
  }
  
  const menuList = [
    { text: '제안서 업로드', route: '/' },
    { text: '프로토 타입 생성', route: '/prototype' },
    { text: '자료 적합도 평가', route: '/evaluation' },
    { text: '발표 스크립트 업로드', route: '/script' },
    { text: '발표 음성 평가', route: '/voice' }
  ]

  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    border-bottom: 1px solid #eee;
    background-color: #ffffff;
  }
  
  .logo {
    width: 200px;
  }
  
  .menu-wrapper {
    position: absolute;
    top: 20px;
    right: 40px;  /* ✅ 좌우 간격 확보 */
  }
  
  .hamburger {
    font-size: 28px;
    background: none;
    border: none;
    cursor: pointer;
  }
  
  .dropdown {
    position: absolute;
    right: 0;
    top: 100%;
    margin-top: 12px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  }
  
  .dropdown-item {
    padding: 12px 16px;
    width: 200px;
    background: white;
    border: none;
    text-align: left;
    cursor: pointer;
  }
  
  .dropdown-item:hover {
    background-color: #f0f4fa;
  }
  </style>