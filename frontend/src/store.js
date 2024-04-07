import { createStore } from 'vuex';

const store = createStore({
  state: {
    user: {
      userType: '' // 假定这是从后端获取的用户信息中的一部分
    }
  },
  mutations:{
    SET_USER_TYPE_SALES(state) {
      state.user.userType = 'sales';
    }, 
    // 设置用户类型为维修
    SET_USER_TYPE_SERVICE(state) {
      state.user.userType = 'service';
    },   
    // 设置用户类型为用户
    SET_USER_TYPE_CUSTOMER(state) {
      state.user.userType = 'customer';
    }
  },

});

export default store