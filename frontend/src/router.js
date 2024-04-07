import { createWebHistory, createRouter } from 'vue-router'
import store from './store'
//customer routers
import SignIn from './views/SignIn.vue'
import SignUp from './views/SignUp.vue'
import HomePage from './views/HomePage.vue'
import ServiceAppointment from './views/ServiceAppointment.vue'
import UserForum from './views/UserForum.vue'
import MarketingActivities from './views/MarketingActivities.vue'
import CustomerService from './views/CustomerService.vue'

//below is staff routers
import StaffLgoin from './views/StaffLogin.vue'
//sales routers
import SalesHomePage from './views/SalesHomePage.vue'
import AppointmentManagement from './views/AppointmentManagement.vue'
import SalesAnalysis from './views/SalesAnalysis.vue'
import ActivitiesManagement from './views/ActivitiesManagement.vue'
import CustomerRelationship from './views/CustomerRelationship.vue'
//service routers
import ServiceHomePage from './views/ServiceHomePage.vue'
import StockManagement from './views/StockManagement.vue'
import ServiceRecord from './views/ServiceRecord.vue'

const routes = [
  //customer router
  { path: '/', component: HomePage},
  { path: '/signin', component: SignIn},
  { path: '/signup', component: SignUp},
  { path: '/appointment', component: ServiceAppointment},
  { path: '/forum', component: UserForum},
  { path: '/activities', component: MarketingActivities},
  {path: '/customer_service', component: CustomerService},

  //below are staff routers
  { path: '/staff_login', component:StaffLgoin},

  //sales routers
  {path: '/sales_home_page', 
  component: SalesHomePage,
  },
  { path: '/appointment_management', 
  component: AppointmentManagement,
  },
  {path: '/activities_management', component: ActivitiesManagement},
  {
    path: '/sales_analysis',
    name: 'SalesAnalysis',
    component: SalesAnalysis,
  },
  { path: '/customer_relationship', component:CustomerRelationship},

  //service routers
  { path: '/service_home_page', component:ServiceHomePage},
  { path:'/service_record', component: ServiceRecord},
  { path:'/stock_management', component: StockManagement},

]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresStaff)) {
    // 检查该路由是否需要职员权限
    if (store.getters.isStaff) {
      // 如果用户是职员，继续
      next();
    } else {
      // 如果用户不是职员，重定向到首页或登录页
      next({ path: '/staff_login' });
    }
  } else {
    // 如果不需要特殊权限，直接进入
    next();
  }
});

export default router