import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login'
import Register from "../views/Register";
import Profile from "../views/Profile";
import NewPoll from "../views/NewPoll";
import PollWindow from "../views/PollWindow";
import Reports from "../views/MyReports";
import AllPolls from "../views/Allpolls";
import Users from "../views/Users";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/all-polls',
    name: 'AllPolls',
    component: AllPolls
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
    path: '/poll/:id',
    name: 'Poll',
    component: PollWindow

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
  {
    path: '/reports',
    name: 'Reports',
    component: Reports
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
