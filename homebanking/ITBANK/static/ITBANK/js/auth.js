//PARA PREVENIR QUE SE REDIRIJA TODO EL TIEMPO AL LOGIN PONER true
let isLogged = true;


if (window.location.pathname !== '/login.html') {
    if (!isLogged) {
        window.location.replace('/login.html')   
    } else{
        console.log('epico')
    }
}
const loginBtn = document.getElementById('login-button');

loginBtn.addEventListener('click', ()=>{
    window.location.replace('/index.html');
})