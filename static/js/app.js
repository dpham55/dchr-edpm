var chapters = instantsearch({
  appId: 'Y2PPY80XX6',
  apiKey: '72b0a96c4af167f1cabb785757b0cb37',
  indexName: 'Chapters',
  searchFunction: function(helper) {
    var searchResults = document.getElementById('search-results');
    var isearchResults = document.getElementById('i-search-results');
    if (helper.state.query ===''){
      searchResults.style.display="none";
      isearchResults.style.display="none";
      return;
    }
    var query = chapters.helper.state.query;
    issuances.helper.setQuery(query);
    issuances.helper.search();
    helper.search();
    searchResults.style.display="block";
    isearchResults.style.display="block";
  },
  searchParameters: {
    attributesToSnippet: ["content:50"],
    snippetEllipsisText: '...',
    hitsPerPage: 2
  }
});

var issuances = instantsearch({
  appId: 'Y2PPY80XX6',
  apiKey: '72b0a96c4af167f1cabb785757b0cb37',
  indexName: 'Issuances',
  searchParameters: {
    attributesToSnippet: ["contents:50"],
    snippetEllipsisText: '...',
    hitsPerPage: 2
  }
});

var chaptersHits = instantsearch.widgets.hits({
  container: document.querySelector('#chapters'),
  templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "We could not find <em>\"{{query}}\"</em> in any chapters",
    }
});

var issuancesHits = instantsearch.widgets.hits({
  container: document.querySelector('#issuances'),
  templates: {
      item: document.getElementById('hit-template-i').innerHTML,
      empty: "We could not find <em>\"{{query}}\"</em> in any issuances",
    }
});

var searchBox = instantsearch.widgets.searchBox({
  container: document.querySelector('#search-input'),
  magnifier: false,
  loadingIndicator: true,
});

chapters.addWidget(chaptersHits);
chapters.addWidget(searchBox);
issuances.addWidget(issuancesHits);
issuances.start();
chapters.start();
