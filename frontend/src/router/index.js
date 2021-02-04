import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue';
import Login from '../views/Login';
import Register from "../views/Register";
import Profile from "../views/Profile";
import NewPoll from "../views/NewPoll";
import NewReport from "../views/NewReport";
import PollWindow from "../views/PollWindow";
import Reports from "../views/MyReports";
import ReportWindow from "../views/ReportWindow";
import AllPolls from "../views/Allpolls";
import Users from "../views/Users";
import Settings from "../views/Settings";
import Admin from "../views/Admin";
import ChangePass from "../views/ChangePass";

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
    path: '/new-report',
    name: 'New Report',
    component: NewReport
  },
  {
    path: '/poll/:id',
    name: 'Poll',
    component: PollWindow

  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings

  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin

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
    path: '/report/:id',
    name: 'ReportWindow',
    component: ReportWindow
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
  {
    path: '/change_pass',
    name: 'ChangePass',
    component: ChangePass
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
