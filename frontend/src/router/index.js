import { createRouter, createWebHistory } from 'vue-router';

import GamePage from '../pages/GamePage.vue';
import MainPage from '../pages/MainPage.vue';

const routes = [{
  path: '/',
  name: 'Main',
  component: MainPage
},
{
  path: '/game',
  name: 'Game',
  component: GamePage
}]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
