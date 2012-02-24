HNCrawl
=======

*A [`scrapy`][scrapy]-based [Hacker News][hn] crawler.*

**Introduction**

HNCrawl is a tiny, simple [`scrapy`][scrapy]-based crawler which grabs the html 
content of pages linked to the front page of hacker news.

## Examples

### Installation

    $ pip install scrapy
    $ git clone git@github.com:mvanveen/hncrawl.git
    
### Scraping

**Note**: Please be sure to keep in mind that the [`Crawl-Delay`][crawl] value set in the HN [`robots.txt`][robots] file is set to **30 seconds**.  **Please be sure to avoid using the scraper more than once per 30 seconds!**
    
**Scrape the links from the front page of HN**    
    
    $ scrapy crawl hnspider

**Scrape items and return json summary of items scraped into `items.json`**

    $ scrapy crawl alias_scrape -o items.json -t json
    
## Output

Here is an example file hierarchy.  Folders are a hex digest
of the SHA1 hash of the hacker news item url.


     ├── out
     │   ├── 000f86c7547b47a700dee0879a0fe08b4597360f
     │   │   └── html
     │   ├── 0190cbad182ab3bc9a92482d169f38e363ca3c57
     │   │   └── html
     │   ├── 02bae9642c8dd4b75a593c1c42beff62824ee8fc
     │   │   └── html
     │   ├── 05c1460571f0ac45f77bf2ecbd3cba8b85c20621
     │   │   └── html
     │   ├── 0b1587a3dbe9996d10a0fd3250f75462ebd59a0b
     │   │   └── html
     │   ├── 0c5c67585004e03341e6a87d2db5257b93337b86
     │   │   └── 

The JSON summary of news items look like this:

	{'title': u'EFF Wins Protection for Time Zone Database',
	 'url': u'https://www.eff.org/press/releases/eff-wins-protection-time-zone-database'}

## Dependencies

- [scrapy][scrapy]
- [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)

## License

HNCrawl is MIT licensed.

[crawl]: http://en.wikipedia.org/wiki/Robots_exclusion_standard#Crawl-delay_directive
[hn]: http://news.ycombinator.com
[robots]: http://news.ycombinator.com/robots.txt
[scrapy]: http://scrapy.org/
