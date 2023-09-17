import { createStore } from 'vuex'
import Api from '@/services/Api'

export default createStore({
  state: {
    questions: [],
  },
  getters: {
    getStoredQuestions: (state) => {
      return state.questions
  },
  },
  mutations: {
    SET_QUESTIONS (state, payload) {
      state.questions = payload
    },
  },
  actions: {
    async getAllQuestions({ commit, state }, { setResult=true, tag, cb }) {
      return await Api()
          .get(`/?tag=${tag}`)
          .then((response) => {
              if (setResult) {
                  commit('SET_QUESTIONS', response.data.data)
              }
              if (cb) {
                  cb(response.data)
              }
              return response.data
          })
          .catch((error) => {
              return Promise.reject(error)
          })
  },
  },
  modules: {
  }
})
