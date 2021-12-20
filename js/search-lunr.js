
const searchform = document.querySelector('.searchform')
const searchfield = document.querySelector('#lunrsearch')
const resultdiv = document.querySelector('#lunrsearchresults')
const searchcount = document.querySelector('.searchcount')

const idx = lunr(function () {
    this.ref('id')
    this.field('url')
    this.field('title', {boost: 10})
    this.field('tags')
    this.field('body')

    for (let key in window.store) {
        this.add({
            'id': key,
            'url': window.store[key].url,
            'title': window.store[key].title,
            'tags': window.store[key].tags,
            'body': window.store[key].body
        })
    }
});

const getTerm = function () {
    searchfield.addEventListener('keyup', function (event) {
        event.preventDefault();
        const query = this.value;
        doSearch(query);
    })
}

const doSearch = query => {
    const result = idx.search(query);
    resultdiv.innerHTML = '';
    searchcount.innerHTML = `Found ${result.length} records`;
    updateUrlParameter(query);
    showResults(result);
}

const showResults = (result) => {
    for (let item of result) {
        const ref = item.ref;
        const searchitem = document.createElement('div');
        searchitem.className = 'lunrsearchresult';
        searchitem.innerHTML = `
                <a class='title' href='${window.store[ref].url}'>${window.store[key].title}</a>
            `;

        resultdiv.appendChild(searchitem);
    }
}

const updateUrlParameter = (value) => {
    window.history.pushState('', '', `s=${encodeURIComponent(value)}`)
};

const getQuery = () => {
    const parser = document.createElement('a')
    parser.href = window.location.href

    if (parser.href.includes('=')) {
        const searchquery = decodeURIComponent(parser.href.substring(parser.href.indexOf('=') + 1));
        searchfield.setAttribute('value', searchquery);
        doSearch(searchquery);
    }
}
