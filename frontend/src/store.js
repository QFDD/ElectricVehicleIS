import { createStore } from 'vuex';
import axios from 'axios';
import Vue from 'vue';
const store = createStore({
  state: {
    user: {
      id: null,
      userType: '' // 假定这是从后端获取的用户信息中的一部分
    },
    opportunities: []
  },
  actions: {
    setUser({ commit }, { userId, userType }) {
      commit('SET_USER_ID', userId);
      commit('SET_USER_TYPE', userType);
    },
    fetchOpportunities({ commit }) {
      axios.get('http://10.193.160.177:5000/sales/opportunities')
        .then(response => {
          commit('setOpportunities', response.data);
        });
    },
    addOpportunity({ commit }, opportunity) {
      axios.post('http://10.193.160.177:5000/sales/opportunities', opportunity)
        .then(response => {
          commit('addOpportunity', response.data);
          alert('successfully add opportunity')
        });
    },
    updateOpportunity({ commit }, opportunity) {
      axios.put(`http://10.193.160.177:5000/sales/opportunities/${opportunity.id}`, opportunity)
        .then(response => {
          commit('updateOpportunity', response.data);
        });
    },
    deleteOpportunity({ commit }, id) {
      axios.delete(`http://10.193.160.177:5000/sales/opportunities/${id}`)
        .then(() => {
          commit('deleteOpportunity', id);
        });
    }
  },
  mutations:{
    SET_USER_TYPE_NONE(state) {
      state.user.userType = '';
    },
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
    },
    SET_USER_ID(state, userId){
      state.user.id = userId
    },
    setOpportunities(state, opportunities) {
      state.opportunities = opportunities;
    },
    addOpportunity(state, opportunity) {
      state.opportunities.push(opportunity);
    },
    updateOpportunity(state, updatedOpportunity) {
      const index = state.opportunities.findIndex(opportunity => opportunity.id === updatedOpportunity.id);
      if (index !== -1) {
        Vue.set(state.opportunities, index, updatedOpportunity);
      }
    },
    deleteOpportunity(state, id) {
      state.opportunities = state.opportunities.filter(opportunity => opportunity.id !== id);
    }
  },
});

export default store