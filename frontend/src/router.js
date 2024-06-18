import { createWebHistory, createRouter } from 'vue-router'
import store from './store'
// test router
import TestView from '@/views/TestView.vue'

//customer routers
import SignIn from './views/SignIn.vue'
import SignUp from './views/SignUp.vue'
import HomePage from './views/HomePage.vue'
import ServiceAppointment from './views/ServiceAppointment.vue'
import UserForum from './views/UserForum.vue'
import MarketingActivities from './views/MarketingActivities.vue'
import CustomerService from './views/CustomerService.vue'
import CreatePost from '@/views/CreatePost.vue'
import PostDetail from '@/views/PostDetail.vue';
import UserProfile from '@/views/UserProfile.vue'
//below is staff routers
import StaffLgoin from './views/StaffLogin.vue'
//sales routers
import ChatBox from './views/ChatBox.vue'
import SalesHomePage from './views/SalesHomePage.vue'
import CustomerLeads from './views/CustomerLeads.vue'
import SalesAnalysis from './views/SalesAnalysis.vue'
import ActivitiesManagement from './views/ActivitiesManagement.vue'
import CustomerRelationship from './views/CustomerRelationship.vue'
import OpportunityList from '@/components/OpportunityList.vue';
import OpportunityForm from '@/components/OpportunityForm.vue';
//service routers
import ServiceHomePage from './views/ServiceHomePage.vue'
import StockManagement from './views/StockManagement.vue'
import ServiceRecord from './views/ServiceRecord.vue'
import PartDetails from './views/PartsDetails.vue'
import ServiceRecordDetails from './views/ServiceRecordDetails.vue';
import AppointmentManagement from './views/AppointmentManagement.vue'
const routes = [
  // test
  { path:'/test',component: TestView},
  //customer router
  { path: '/', component: HomePage},
  { path: '/user_profile/:id', component: UserProfile},
  { path: '/signin', component: SignIn},
  { path: '/signup', component: SignUp},
  { path: '/appointment', component: ServiceAppointment},
  { path: '/forum', component: UserForum},
  { path: '/activities', component: MarketingActivities},
  {path: '/customer_service', component: CustomerService},
  { path: '/create_post', component: CreatePost},
  {
    path: '/posts/:id',
    name: 'PostDetail',
    component: PostDetail,
    props: true
  },
  //below are staff routers
  { path: '/staff_login', component:StaffLgoin},

  //sales routers
  { path: '/opportunity_list', component: OpportunityList },
  { path: '/opportunity/new', component: OpportunityForm },
  { path: '/opportunity/edit/:id', component: OpportunityForm, props: true },
  {path:'/chat_box/:id',component:ChatBox},
  {path: '/sales_home_page', 
  component: SalesHomePage,
  },
  { path: '/customer_leads', component: CustomerLeads},
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
  { path:'/appointment_management', component: AppointmentManagement},
  { path: '/parts/:id', component: PartDetails },
  { path: '/service-records/:id', component: ServiceRecordDetails }
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