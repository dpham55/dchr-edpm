      var chapters = instantsearch({
        appId: 'Y2PPY80XX6',
        apiKey: '72b0a96c4af167f1cabb785757b0cb37',
        indexName: 'Chapters',
        urlSync: true,
        searchFunction: function(helper) {
          var query = chapters.helper.state.query;
          issuances.helper.setQuery(query);
          issuances.helper.search();
          helper.search();
        },
        searchParameters: {
          attributesToSnippet: ["content:100"],
          snippetEllipsisText: '...',
          hitsPerPage: 50
        }
      });

      var issuances = instantsearch({
        appId: 'Y2PPY80XX6',
        apiKey: '72b0a96c4af167f1cabb785757b0cb37',
        indexName: 'Issuances',
        searchParameters: {
          attributesToSnippet: ["contents:100"],
          snippetEllipsisText: '...',
          hitsPerPage: 50
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

      var cRefList = instantsearch.widgets.refinementList({
        container: '#c-refinement-list',
        attributeName: 'chapter',
        templates: {
          header: 'Chapters'
        }
      });

      var iRefList = instantsearch.widgets.refinementList({
        container: '#i-refinement-list',
        attributeName: 'chapter_searchable',
        templates: {
          header: 'Chapters'
        }
      });

      chapters.addWidget(chaptersHits);
      chapters.addWidget(searchBox);
      chapters.addWidget(cRefList);
      issuances.addWidget(iRefList);
      issuances.addWidget(issuancesHits);
      issuances.start();
      chapters.start();