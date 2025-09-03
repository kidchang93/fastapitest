import {createRouter, createWebHistory} from 'vue-router';
import UserRegister from '../components/UserRegister.vue';
import UserLogin from '../components/UserLogin.vue';
import TodoList from '../components/TodoList.vue';
import Home from "../components/Home.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegister
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },
  {
    path: '/todos',
    name: 'TodoList',
    component: TodoList
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
