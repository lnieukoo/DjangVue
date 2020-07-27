import MainContent from './components/MainContent.js'
import store from './store.js'

const app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
    },
    store
  });