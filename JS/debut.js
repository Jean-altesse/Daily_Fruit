console.log(document)

let btn = document.querySelector('#btn')

let pass = document.querySelector('#pass')
console.log(pass)

let nom = document.querySelector('#name')
console.log(nom)

let tel = document.querySelector('#tel')
console.log(tel)

let cpass = document.querySelector('#c-pass')
console.log(cpass)

btn.addEventListener('click', function(){
localStorage.setItem('nom',nom.value)
localStorage.setItem('motdepass',pass.value)
localStorage.setItem('confirme',cpass.value)
localStorage.setItem('telephone',tel.value)

})

