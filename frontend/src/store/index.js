import { createStore } from 'vuex'
import Api from '@/services/Api'

export default createStore({
  state: {
    questions: [],
    organizations: [],
    issues: [],
    pageNumber: 1
  },
  getters: {
    getStoredQuestions: (state) => {
      return state.questions
  },
  getStoredOrganizations: (state) => {
    return state.organizations
},
getStoredIssues: (state) => {
  return state.issues
},
  },
  mutations: {
    SET_QUESTIONS(state, payload) {
      state.questions = payload
    },
    SET_ORGANIZATIONS(state, payload) {
      state.organizations = payload
    },
    SET_ISSUES(state, payload) {
      state.issues = payload
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
  async getAllIssues({ commit, state }, { setResult=true, url, cb }) {
    return await Api()
        .get(`issues?url=${url}`)
        .then((response) => {
            if (setResult) {
                commit('SET_ISSUES', response.data.data)
            }
            if (cb) {
                cb(response.data.data)
            }
            return response.data.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
},
  async createOrganization({ commit }, { payload, cb }) {
    return await Api()
        .post('/organizations', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async getAllOrganizations({ commit, state }, { setResult=true, cb }) {
    return await Api()
        .get(`/organizations?page=${state.pageNumber}`)
        .then((response) => {
            if (setResult) {
                commit('SET_ORGANIZATIONS', response.data.results)
            }
            if (cb) {
                cb(response.data.results)
            }
            return response.data.results
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async deleteOrganization({ commit }, { uuid, cb }) {
  return await Api()
      .delete(`organizations/${uuid}/`)
      .then((response) => {
          if (cb) {
              cb(response.data)
          }
          return response.data
      })
      .catch((error) => {
          return Promise.reject(error)
      })
  }
  
  },
  modules: {
  }
})
