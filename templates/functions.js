

const tableHeader = document.getElementById('table-header');
const tbody = document.getElementById('table-body');
const count=document.getElementById('count');
const textID=document.getElementById('codeData')
const resultdiv=document.getElementById('result');
const search=document.getElementById('search_word');


function showSearchWord(){
    removeresult();
    var search=document.getElementById('search_word');
    search.style.display = 'block';
    var search_word=document.getElementById('word_input');
    search_word.textContent='';
    search_word.value='';
}

function encodeText(text) {
    var utf8Bytes = new TextEncoder().encode(text);
    var base64EncodedData = btoa(String.fromCharCode.apply(null,utf8Bytes));
    var myEncodedData = encodeURIComponent(base64EncodedData);
    return myEncodedData
};

function customAjax(url, requestData, successCallback, errorCallback) {
    $.ajax({
        url: url,
        method: 'POST',
        dataType: 'json',
        data: JSON.stringify(requestData),
        contentType: 'application/json',
        success: function (data) {
            if (data.code === 200) {
                //select querry success:show data
                console.log(data);
                successCallback(data);
            } else {
                errorCallback(data.data);
                console.error('Error：', data.data);
            }

        },
        error: function (data) {
            // error: show error message
            console.error('Error：', data.data);
            errorCallback(data.data);
        }
    });
}
function cleanFile() {
    const text=textID.value;
    const encodedData = encodeText(text);
    const param={
        text:encodedData,
    };
    console.log(param);
    customAjax('api/cleanText', param, showrText, showerror);
}


function separate() {
    const text=document.getElementById('codeData').value;
    const encodedData = encodeText(text);
    const param={
        text:encodedData,
    };
    console.log(param);
    customAjax('api/separateToSentence', param, showtable, showerror);
}
function countWord() {
    const text=document.getElementById('codeData').value;
    const encodedData = encodeText(text);
    const param={
        text:encodedData,
    };
    console.log(param);
    customAjax('api/countWord', param, showtable, showerror);
}
function findWord() {
    const text=document.getElementById('codeData').value;
    const encodedData = encodeText(text);
    const word = document.getElementById('word_input').value;
    const param={
        word:word,
        text:encodedData,
    };
    console.log(param);
    customAjax('api/findWord', param, showwordResult, showerror);
}

function countCharacters() {
    const text=document.getElementById('codeData').value;
    const encodedData = encodeText(text);
    const param={
        text:encodedData,
    };
    console.log(param);
    customAjax('api/countCharacters', param, showtable, showerror);
}

function dectectEnglish() {
    const text=textID.value;
    const encodedData = encodeText(text);
    const param={
        text:encodedData,
    };
    console.log(param);
    customAjax('api/dectectEnglish', param, showrText, showerror);
}
function showerror(error){
    removeresult();
    const resultdiv=document.getElementById('result');
    const errordiv=document.createElement('error');
    errordiv.textContent="Error:"+error;
    errordiv.className ='error';
    resultdiv.append(errordiv);
}

function showrText(text){
    text=text.data
    removeresult();
    const textdiv=document.createElement('div');
    textdiv.className ='result_text'
    textdiv.textContent=text;
    resultdiv.append(textdiv);
}
function removeresult(){
    let nums=count.querySelector('span');
    resultdiv.innerHTML='';
    tableHeader.innerHTML = '';
    tbody.innerHTML = '';
    nums.textContent='';

    search.style.display = 'none';
}
function addtable(data){
    console.log(data)
    let nums=count.querySelector('span');

    const headerRow = document.createElement('tr');
    nums.textContent=data.total;
    data=data.data;
    for (const key in data[0]) {
        const th = document.createElement('th');
        th.textContent = key;
        headerRow.appendChild(th);
    }
    tableHeader.appendChild(headerRow);
    data.forEach(data => {
        const row = document.createElement('tr');
        for (const key in data) {
            const td = document.createElement('td');
            td.textContent = data[key];
            row.appendChild(td);
        }
        tbody.appendChild(row);
    });
}
function showtable(data) {
    removeresult();
    addtable(data);
}
function showwordResult(data){
    const resultdiv=document.getElementById('result');
    resultdiv.innerHTML='';
    const count=document.getElementById('count');
    let nums=count.querySelector('span');
    const tableHeader = document.getElementById('table-header');
    tableHeader.innerHTML = '';
    const tbody = document.getElementById('table-body');
    tbody.innerHTML = '';
    const headerRow = document.createElement('tr');

    nums.textContent=data.total;
    data=data.data;
    for (const key in data) {
        const th = document.createElement('th');
        th.textContent = key;
        headerRow.appendChild(th);
    }
    tableHeader.appendChild(headerRow);
    const row = document.createElement('tr');
    for (const key in data) {
        const td = document.createElement('td');
        td.textContent = data[key];
        row.appendChild(td);
    }
    tbody.appendChild(row);
}
