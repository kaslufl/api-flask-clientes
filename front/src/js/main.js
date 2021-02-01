const codigo = document.querySelector("#codigo")

const showData = (result)=>{
    for(const campo in result){
        if(document.querySelector("#"+campo)){
            document.querySelector("#"+campo).value = result[campo]
        }
    }
}

codigo.addEventListener("blur",(e)=>{
    let search = codigo.value
    const options = {
        method: 'GET',
        mode: 'cors',
        cache: 'default'
    }
    
    fetch(`http://127.0.0.1:5000/cliente/${search}`, options)
    .then(response =>{ response.json()
        .then( data => showData(data))
    })
    .catch(e => console.log('Erro: ' + e, message))
})