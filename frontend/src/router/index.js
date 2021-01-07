import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login'
import Register from "../views/Register";
import Profile from "../views/Profile";
import NewPoll from "../views/NewPoll";
import MyPolls from "../views/MyPolls";
import MyVotes from "../views/MyVotes";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/profile/:id',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/new-poll',
    name: 'New Voting',
    component: NewPoll
  },
  {
    path: '/user/:id/polls',
    name: 'My polls',
    component: MyPolls
  },
  {
    path: '/votes',
    name: 'My Vote',
    component: MyVotes
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
