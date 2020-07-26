import MainHeader from './MainHeader.js'
import MainBody from './MainBody.js'
import MainFooter from './MainFooter.js'

const MainContent = Vue.component ("main-content", {
    template: `
    
    <div id="main-content">
    <main-header></main-header>
    <main-body></main-body>
    <main-footer></main-footer>
    </div>
    
    `
})

export default MainContent