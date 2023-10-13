import GamePage from '@/pages/GamePage.vue';
import MainPage from '@/pages/MainPage.vue';
import { createRouter, createWebHistory } from 'vue-router';

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

export const router =
    createRouter({
        history: createWebHistory(),
        routes
    })