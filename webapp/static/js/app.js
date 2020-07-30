import MainHeader from './components/MainHeader.js'
import MainBody from './components/MainBody.js'
import MainFooter from './components/MainFooter.js'
import store from './store.js'

const app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
    },
    store
  });