import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    user: null,
    token: null,
    investments: []
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setToken(state, token) {
      state.token = token
    },
    setInvestments(state, investments) {
      state.investments = investments
    }
  },
  actions: {
    async login({ commit }, credentials) {
      const response = await axios.post('/auth/login', credentials)
      commit('setToken', response.data.access_token)
      commit('setUser', response.data.user)
    },
    async fetchInvestments({ commit }) {
      const response = await axios.get('/investments')
      commit('setInvestments', response.data)
    }
  },
  modules: {}
})
