import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login'
import Register from "../views/Register";
import Profile from "../views/Profile";
import NewPoll from "../views/NewPoll";
import MyVoting from "../views/MyVoting";
import MyVote from "../views/MyVote";

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
    path: '/my-voting',
    name: 'My Voting',
    component: MyVoting
  },
  {
    path: '/my-vote',
    name: 'My Vote',
    component: MyVote
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