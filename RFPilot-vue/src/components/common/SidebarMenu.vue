<template>
    <aside class="sidebar">
      <div class="menu">
        <h2>다른 기능 해보기</h2>
        <ul>
          <li v-for="(item, index) in menuItems" :key="index" @click="goTo(item.route)">
            <span class="star">⭐</span>
            <div>
              <strong>{{ item.title }}</strong>
              <p>{{ item.description }}</p>
            </div>
          </li>
        </ul>
      </div>
    </aside>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  const menuItems = [
    {
      route: '/prototype',
      title: '프로토타입 생성',
      description: '신청 양식에 대한 프로토타입을 생성합니다.',
    },
    {
      route: '/evaluation',
      title: '자료 적합도 평가',
      description: 'RFP에 해당하는 자료가 적합한지 평가받습니다.',
    },
    {
      route: '/script',
      title: '발표 스크립트 평가',
      description: '발표 스크립트 파일을 업로드해 평가받습니다.',
    },
    {
      route: '/voice',
      title: '발표 음성 평가',
      description: '자신의 발표 음성 파일을 업로드해 평가받습니다.',
    },
    {
      route: '/',
      title: '첫 화면으로 돌아가기',
      description: '첫 업로드 화면으로 돌아갑니다.',
    },
  ]
  
  const goTo = (route) => {
    if (route === '/') {
      sessionStorage.clear()  // ✅ 여기에 추가
    }
    router.push(route)
  }
  </script>
  
  <style scoped>
  .sidebar {
    width: 400px;
    padding: 20px;
    background-color: #f9fafb;
    border-right: 1px solid #ddd;
  }
  
  .menu h2 {
    margin-bottom: 40px;
    font-size: 25px;
    font-weight: bold;
  }
  
  .menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .menu li {
    display: flex;
    gap: 15px;
    margin-bottom: 30px;
    cursor: pointer;
  }
  
  .menu li div {
    display: flex;
    flex-direction: column;
  }
  
  .menu li strong {
    font-size: 15px;
    font-weight: 600;
  }
  
  .menu li p {
    font-size: 13px;
    color: #666;
    margin: 5px 1 1;
  }
  </style>