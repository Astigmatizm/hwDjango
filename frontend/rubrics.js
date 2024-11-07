const domain = 'http://localhost:8000/api/';
// const list = document.getElementById('list');
const list = document.querySelector('#list');
const itemId = document.querySelector('#id');
const itemName = document.querySelector('#name');

const userName = 'admin4';
const password = 'qwerty123';
const credentials = window.btoa(`${userName}:${password}`);
// const result = await fetch(`${domain}rubrics/`, {
//     headers: { 'Authorization': `Basic ${credentials}` }
// }); 

async function loadItem(evt){
    evt.preventDefault();
    const result = await fetch(evt.target.href, {
        headers: { 'Authorization': `Basic ${credentials}` }
});

    
    if(result.ok){
        const data = await result.json();
        itemId.value = data.id;
        itemName.value = data.name;
    } else {
        console.log(result.statusText); 
    }
}

async function deleteItem(evt){ 
    evt.preventDefault();
    const result = await fetch(evt.target.href, {method: 'DELETE',
                                                    headers: { 'Authorization': `Basic ${credentials}`}
                                                });
    if (result.ok) {
        loadList();
    } else {
        console.log(result.statusText);
    }
}

async function loadList(){
    // const result = await fetch(`${domain}rubrics`)
    const result = await fetch(`${domain}rubrics`,{
        headers: { 'Authorization': `Basic ${credentials}` }
    }); 

    if(result.ok){
        const data = await result.json();
        let s = '<ul>', d
        for(let i = 0; i < data.length; i++) {
            d = data[i];
            s +=  `<li>${d.name}
                      <a href="${domain}rubrics/${id}/" class="detail">Вывести</a>
                      <a href="${domain}rubrics/${id}/" class="delete">Удалить</a>
                   </li>` 
        }
        s+='</ul>'
        
        list.innerHTML = s;
        /* Вывести в форму */
        let links = list.querySelectorAll('ul li a.detail');
        links.forEach((link) => {
            link.addEventListener('click', loadItem);
        });

        /* Удалить */
        links = list.querySelectorAll('ul li a.delete');
        links.forEach((link) => {
            link.addEventListener('click', deleteItem);
        });
    } else {
        window.alert(result.statusText)
    }
}

itemName.form.addEventListener('submit', async (evt) => {
    evt.preventDefault();
    let url, method;
    if (itemId.value){
        url = `${domain}rubrics/${itemId.value}/`;
        method = 'PUT';
    } else {
        url = `${domain}rubrics/`;
        method = 'POST';
    };
    const result = await fetch(url, {
        method: method,
        body: JSON.stringify({name: itemName.value }),
        headers: { 'Content-Type': 'application/json',
                    'Authorization': `Basic ${credentials}`}
    }); 
    if (result.ok){ 
        loadList()
        itemName.form.reset();
        itemId.value = '';
    } else {
        console.log(result.statusText);
    }
});

loadList(); 