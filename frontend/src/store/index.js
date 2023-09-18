import { createStore } from 'vuex'
import Api from '@/services/Api'

export default createStore({
  state: {
    questions: [],
    organizations: [],
    issues: [],
    pageNumber: 1,
    user: null,
    tags: [],
    tags_selections: []
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
getStoredUser: (state) => {
  return state.user
},
getStoredTags: (state) => {
  return state.tags
},
getStoredTagSelections: (state) => {
  return state.tags_selections
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
    SET_USER(state, payload) {
      state.user = payload
    },
    SET_TAGS(state, payload) {
      state.tags = payload
    },
    SET_TAGS_SELECTIONS(state, payload) {
      state.tags_selections = payload
    },
  },
  actions: {
    async getUsersMe({ commit, state }, { setResult=true, cb }) {
      return await Api()
          .get('/users/me')
          .then((response) => {
              if (setResult) {
                  commit('SET_USER', response.data)
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
  async createTag({ commit }, { payload, cb }) {
    return await Api()
        .post('/tags', payload)
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
  async getAllTags({ commit, state }, { setResult=true, cb }) {
    return await Api()
        .get(`/tags?page=${state.pageNumber}`)
        .then((response) => {
            if (setResult) {
                commit('SET_TAGS', response.data.results)
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
  async createTagSelection({ commit }, { payload, cb }) {
    return await Api()
        .post('/tags/selections', payload)
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
  async updateTagSelection({ commit }, { id, payload, cb }) {
    return await Api()
        .put(`/tags/selections/${id}/`, payload)
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
  async getAllTagSelections({ commit, state }, { setResult=true, cb }) {
    return await Api()
        .get(`/tags/selections?page=${state.pageNumber}`)
        .then((response) => {
            if (setResult) {
                commit('SET_TAGS_SELECTIONS', response.data.results)
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
  },
  async signupUser({ commit }, { payload, cb }) {
    return await Api(false)
        .post('/signup', payload)
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
  async loginUser({ commit }, { payload, cb }) {
    return await Api(false)
        .post('auth/token/', payload)
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
  
  },
  modules: {
  }
})
