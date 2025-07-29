<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Stock & Crypto Tracker</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #4361ee;
            --success: #2ecc71;
            --danger: #e74c3c;
            --warning: #f39c12;
            --dark: #2c3e50;
            --light: #f8f9fa;
            --white: #ffffff;
            --gray: #7f8c8d;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        .navbar {
            background: var(--primary);
            padding: 1rem;
            display: flex;
            justify-content: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            display: flex;
            gap: 1.5rem;
        }

        .nav-item {
            color: white;
            text-decoration: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .nav-item:hover {
            background: rgba(255,255,255,0.2);
        }

        .nav-item.active {
            background: rgba(255,255,255,0.3);
        }

        .main-content {
            padding: 1rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .card {
            background: var(--white);
            border-radius: 0.75rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .section-title {
            color: var(--primary);
            font-size: 1.3rem;
            margin: 0 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .data-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }

        .data-card {
            background: var(--white);
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            padding: 1rem;
            transition: all 0.3s ease;
            border-left: 4px solid var(--primary);
        }

        .data-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        }

        .stock-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }

        .ticker {
            font-weight: 600;
            color: var(--primary);
            font-size: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .price {
            font-weight: 700;
            font-size: 1.1rem;
        }

        .up { color: var(--success); }
        .down { color: var(--danger); }
        .neutral { color: var(--warning); }

        .change {
            font-size: 0.85rem;
            padding: 0.2rem 0.5rem;
            border-radius: 0.25rem;
            background-color: rgba(46, 204, 113, 0.1);
        }

        .down .change {
            background-color: rgba(231, 76, 60, 0.1);
        }

        .neutral .change {
            background-color: rgba(243, 156, 18, 0.1);
        }

        .volume {
            font-size: 0.8rem;
            color: var(--gray);
            margin-top: 0.25rem;
        }

        .company-info {
            margin-top: 0.75rem;
            padding-top: 0.75rem;
            border-top: 1px dashed #eee;
            font-size: 0.85rem;
        }

        .info-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.25rem;
        }

        .info-label {
            color: var(--gray);
        }

        .info-value {
            font-weight: 500;
        }

        .positive { color: var(--success); }
        .negative { color: var(--danger); }
        .neutral { color: var(--warning); }

        .news-card {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .news-title {
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--primary);
            flex-grow: 1;
        }

        .news-source {
            font-size: 0.8rem;
            color: var(--gray);
            margin-top: auto;
        }

        .video-container {
            position: relative;
            padding-bottom: 56.25%;
            height: 0;
            overflow: hidden;
            border-radius: 0.5rem;
            margin-top: 1rem;
        }

        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }

        @media (max-width: 768px) {
            .data-grid {
                grid-template-columns: 1fr;
            }
            
            .nav-container {
                gap: 0.75rem;
            }
            
            .nav-item {
                padding: 0.5rem;
                font-size: 0.9rem;
            }
        }

        /* Loading animation */
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }

        .loading {
            animation: pulse 1.5s infinite;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hidden {
            display: none;
        }

        .logo {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--primary);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="nav-container">
            <a href="#" class="nav-item active" onclick="showTab('market')">
                <i class="fas fa-chart-line"></i> Market Data
            </a>
            <a href="#" class="nav-item" onclick="showTab('news')">
                <i class="fas fa-newspaper"></i> News & Videos
            </a>
        </div>
    </div>

    <div class="main-content">
        <!-- Market Data Tab -->
        <div id="market-tab">
            <div class="card">
                <h2 class="section-title">
                    <i class="fas fa-rupee-sign"></i> NSE/BSE Stocks
                </h2>
                <div id="stocks" class="data-grid loading">
                    Loading stock data...
                </div>
            </div>

            <div class="card">
                <h2 class="section-title">
                    <i class="fab fa-bitcoin"></i> Top Cryptocurrencies
                </h2>
                <div id="crypto" class="data-grid loading">
                    Loading crypto data...
                </div>
            </div>
        </div>

        <!-- News & Videos Tab -->
        <div id="news-tab" class="hidden">
            <div class="card">
                <h2 class="section-title">
                    <i class="fas fa-business-time"></i> Financial News
                </h2>
                <div id="news" class="data-grid loading">
                    Loading news...
                </div>
            </div>

            <div class="card">
                <h2 class="section-title">
                    <i class="fab fa-youtube"></i> Market Updates
                </h2>
                <div id="youtube" class="loading">
                    Loading videos...
                </div>
            </div>
        </div>
    </div>

    <script>
        // Configuration
        const config = {
            newsApiKey: 'b8448e802b2941be863de893a9f60d68',
            alphaVantageKey: '6AFY4VTCLQ050BBM',
            companies: [
                { symbol: 'RELIANCE.BSE', name: 'Reliance Industries' },
                { symbol: 'TCS.BSE', name: 'Tata Consultancy Services' },
                { symbol: 'HDFCBANK.BSE', name: 'HDFC Bank' },
                { symbol: 'INFY.BSE', name: 'Infosys' },
                { symbol: 'SBIN.BSE', name: 'State Bank of India' }
            ],
            cryptoLimit: 10,
            newsLimit: 8
        };

        // Tab navigation
        function showTab(tabName) {
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            event.target.classList.add('active');

            document.getElementById('market-tab').classList.add('hidden');
            document.getElementById('news-tab').classList.add('hidden');
            document.getElementById(`${tabName}-tab`).classList.remove('hidden');
        }

        // Fetch Stock Data
        async function fetchStocks() {
            const container = document.getElementById('stocks');
            container.classList.remove('loading');
            
            let html = '';
            
            for (const company of config.companies) {
                try {
                    const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${company.symbol}&apikey=${config.alphaVantageKey}`);
                    const data = await response.json();
                    const stock = data['Global Quote'];
                    
                    if (stock) {
                        const changePercent = parseFloat(stock['10. change percent'].replace('%', ''));
                        const health = getCompanyHealth(company.symbol.split('.')[0]);
                        
                        html += `
                            <div class="data-card">
                                <div class="stock-header">
                                    <span class="ticker">
                                        <span class="logo">${company.symbol[0]}</span>
                                        ${company.symbol.split('.')[0]}
                                    </span>
                                    <span class="price ${getChangeClass(changePercent)}">
                                        ₹${parseFloat(stock['05. price']).toLocaleString('en-IN')}
                                    </span>
                                </div>
                                
                                <div class="${getChangeClass(changePercent)} change">
                                    ${changePercent >= 0 ? '+' : ''}${changePercent.toFixed(2)}%
                                </div>
                                
                                <div class="volume">
                                    Volume: ${parseInt(stock['06. volume']).toLocaleString('en-IN')}
                                </div>
                                
                                <div class="company-info">
                                    <div class="info-item">
                                        <span class="info-label">Health:</span>
                                        <span class="info-value ${health.sentiment}">${health.financialHealth}</span>
                                    </div>
                                    <div class="info-item">
                                        <span class="info-label">Cash:</span>
                                        <span class="info-value">${health.cashReserves}</span>
                                    </div>
                                    <div class="info-item">
                                        <span class="info-label">Recent:</span>
                                        <span class="info-value">${health.recentEvents[0]}</span>
                                    </div>
                                </div>
                            </div>
                        `;
                    }
                } catch (error) {
                    console.error("Error fetching stock:", error);
                    html += `
                        <div class="data-card">
                            <div class="stock-header">
                                <span class="ticker">${company.symbol.split('.')[0]}</span>
                                <span class="price neutral">N/A</span>
                            </div>
                            <div class="volume">Data unavailable</div>
                        </div>
                    `;
                }
            }
            
            container.innerHTML = html || '<div class="data-card">Failed to load stock data</div>';
        }

        // Get company health data
        function getCompanyHealth(ticker) {
            const healthData = {
                'RELIANCE': {
                    financialHealth: 'Strong (AAA)',
                    cashReserves: '₹2.5L Cr',
                    recentEvents: ['Jio 5G expansion', 'Retail growth'],
                    sentiment: 'positive'
                },
                'TCS': {
                    financialHealth: 'Excellent (AA+)',
                    cashReserves: '₹78K Cr',
                    recentEvents: ['Hiring 40K freshers', '$2B deal'],
                    sentiment: 'positive'
                },
                'HDFCBANK': {
                    financialHealth: 'Stable (AA)',
                    cashReserves: '₹1.2L Cr',
                    recentEvents: ['HDFC merger complete'],
                    sentiment: 'neutral'
                },
                'INFY': {
                    financialHealth: 'Good (A+)',
                    cashReserves: '₹65K Cr',
                    recentEvents: ['Q3 results beat estimates'],
                    sentiment: 'neutral'
                },
                'SBIN': {
                    financialHealth: 'Improving (A)',
                    cashReserves: '₹95K Cr',
                    recentEvents: ['Digital growth 35%'],
                    sentiment: 'positive'
                }
            };
            return healthData[ticker] || {};
        }

        // Get change class
        function getChangeClass(percent) {
            if (percent > 0) return 'up';
            if (percent < 0) return 'down';
            return 'neutral';
        }

        // Fetch Crypto Data
        async function fetchCrypto() {
            const container = document.getElementById('crypto');
            container.classList.remove('loading');
            
            try {
                const response = await fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=${config.cryptoLimit}`);
                const coins = await response.json();
                
                let html = '';
                coins.forEach(coin => {
                    const change = coin.price_change_percentage_24h;
                    html += `
                        <div class="data-card">
                            <div class="stock-header">
                                <span class="ticker">
                                    <img src="${coin.image}" width="20" height="20" style="border-radius:50%;" alt="${coin.name}">
                                    ${coin.symbol.toUpperCase()}
                                </span>
                                <span class="price ${getChangeClass(change)}">
                                    $${coin.current_price.toLocaleString('en-US', {maximumFractionDigits: 2})}
                                </span>
                            </div>
                            
                            <div class="${getChangeClass(change)} change">
                                ${change >= 0 ? '+' : ''}${change.toFixed(2)}%
                            </div>
                            
                            <div class="company-info">
                                <div class="info-item">
                                    <span class="info-label">Market Cap:</span>
                                    <span class="info-value">$${(coin.market_cap/1000000000).toFixed(2)}B</span>
                                </div>
                                <div class="info-item">
                                    <span class="info-label">24h Vol:</span>
                                    <span class="info-value">$${(coin.total_volume/1000000000).toFixed(2)}B</span>
                                </div>
                            </div>
                        </div>
                    `;
                });
                
                container.innerHTML = html;
            } catch (error) {
                console.error("Error fetching crypto:", error);
                container.innerHTML = '<div class="data-card">Failed to load crypto data</div>';
            }
        }

        // Fetch Financial News
        async function fetchNews() {
            const container = document.getElementById('news');
            container.classList.remove('loading');
            
            try {
                // Fetch general business news
                const newsResponse = await fetch(`https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=${config.newsLimit}&apiKey=${config.newsApiKey}`);
                const newsData = await newsResponse.json();
                
                // Fetch company-specific news
                let companyNews = [];
                for (const company of config.companies) {
                    const name = company.name.split(' ')[0]; // Get first word of company name
                    const response = await fetch(`https://newsapi.org/v2/everything?q=${encodeURIComponent(name)}+AND+(protest OR layoff OR deal OR results OR financial)&sortBy=relevancy&pageSize=2&apiKey=${config.newsApiKey}`);
                    const data = await response.json();
                    if (data.articles) companyNews = [...companyNews, ...data.articles];
                }
                
                // Combine and deduplicate
                const allArticles = [...newsData.articles, ...companyNews];
                const uniqueArticles = allArticles.filter((article, index, self) =>
                    index === self.findIndex(a => a.title === article.title)
                ).slice(0, config.newsLimit);
                
                let html = '';
                uniqueArticles.forEach(article => {
                    // Find related companies
                    const relatedCompanies = config.companies.filter(company => 
                        article.title.includes(company.symbol.split('.')[0]) || 
                        article.title.includes(company.name.split(' ')[0])
                    ).map(c => c.symbol.split('.')[0]);
                    
                    // Highlight keywords
                    let title = article.title;
                    const keywords = {
                        'protest': 'danger',
                        'layoff': 'danger',
                        'strike': 'danger',
                        'deal': 'success',
                        'profit': 'success',
                        'growth': 'success',
                        'merge': 'warning'
                    };
                    
                    Object.keys(keywords).forEach(word => {
                        const regex = new RegExp(word, 'gi');
                        title = title.replace(regex, `<span class="${keywords[word]}">${word}</span>`);
                    });
                    
                    html += `
                        <div class="data-card news-card">
                            <a href="${article.url}" target="_blank" class="news-title">${title}</a>
                            <div class="company-info" style="margin-top:0.5rem;">
                                ${relatedCompanies.map(c => `<span class="event-tag">${c}</span>`).join('')}
                            </div>
                            <div class="news-source">
                                ${article.source?.name || 'Unknown'} • 
                                ${new Date(article.publishedAt).toLocaleString('en-IN')}
                            </div>
                        </div>
                    `;
                });
                
                container.innerHTML = html;
            } catch (error) {
                console.error("Error fetching news:", error);
                container.innerHTML = `
                    <div class="data-card">
                        <div class="news-title">Failed to load news</div>
                        <div class="news-source">Please try again later</div>
                    </div>
                `;
            }
        }

        // Fetch YouTube Videos
        async function fetchYouTube() {
            const container = document.getElementById('youtube');
            container.classList.remove('loading');
            
            try {
                // In a real app, use YouTube API
                const videos = [
                    {
                        title: "Market Live Updates",
                        id: "dQw4w9WgXcQ",
                        channel: "Financial News"
                    },
                    {
                        title: "Stock Market Analysis",
                        id: "dQw4w9WgXcQ",
                        channel: "Investor Channel"
                    }
                ];
                
                let html = '<div class="data-grid">';
                videos.forEach(video => {
                    html += `
                        <div class="data-card">
                            <div class="news-title">${video.title}</div>
                            <div class="video-container">
                                <iframe src="https://www.youtube.com/embed/${video.id}" 
                                        title="${video.title}" allowfullscreen></iframe>
                            </div>
                            <div class="news-source">${video.channel}</div>
                        </div>
                    `;
                });
                html += '</div>';
                
                container.innerHTML = html;
            } catch (error) {
                console.error("Error fetching videos:", error);
                container.innerHTML = `
                    <div class="data-card">
                        <div class="news-title">Failed to load videos</div>
                        <div class="news-source">Please try again later</div>
                    </div>
                `;
            }
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            fetchStocks();
            fetchCrypto();
            fetchNews();
            fetchYouTube();
            
            // Refresh data every 5 minutes
            setInterval(fetchStocks, 300000);
            setInterval(fetchCrypto, 300000);
            setInterval(fetchNews, 300000);
        });
    </script>
</body>
</html>