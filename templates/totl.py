<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Stocks & Crypto Tracker</title>
    <style>
        :root {
            --primary-color: #4361ee;
            --green: #2ecc71;
            --red: #e74c3c;
            --text-color: #2c3e50;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --border-radius: 12px;
            --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .navbar {
            background-color: var(--primary-color);
            padding: 15px;
            display: flex;
            justify-content: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .nav-options {
            display: flex;
            gap: 20px;
        }

        .nav-option {
            color: white;
            text-decoration: none;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 6px;
            transition: background-color 0.3s;
        }

        .nav-option:hover {
            background-color: rgba(255, 255, 255, 0.2);
        }

        .nav-option.active {
            background-color: rgba(255, 255, 255, 0.3);
        }

        .main-content {
            padding: 15px;
        }

        .container {
            max-width: 100%;
            background: var(--card-bg);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            margin-bottom: 20px;
        }

        h2 {
            color: var(--primary-color);
            font-size: 1.3rem;
            margin-top: 0;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 1px solid #eee;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .stock, .crypto {
            margin-bottom: 20px;
        }

        .ticker {
            font-weight: 600;
            color: var(--primary-color);
            font-size: 0.95rem;
        }

        .price {
            font-weight: 700;
            font-size: 1rem;
        }

        .up {
            color: var(--green);
        }

        .down {
            color: var(--red);
        }

        .volume {
            font-size: 0.8rem;
            color: #7f8c8d;
            margin-top: 2px;
        }

        .data-item {
            padding: 10px 0;
            border-bottom: 1px dashed #ecf0f1;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 8px;
        }

        .data-item:last-child {
            border-bottom: none;
        }

        .change-percent {
            font-size: 0.85rem;
            padding: 2px 6px;
            border-radius: 4px;
            background-color: rgba(46, 204, 113, 0.1);
        }

        .down .change-percent {
            background-color: rgba(231, 76, 60, 0.1);
        }

        .news-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .news-item {
            background: var(--card-bg);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 15px;
            transition: transform 0.3s;
        }

        .news-item:hover {
            transform: translateY(-5px);
        }

        .news-title {
            font-weight: 600;
            margin-bottom: 8px;
            color: var(--primary-color);
        }

        .news-source {
            font-size: 0.8rem;
            color: #7f8c8d;
            margin-top: 5px;
        }

        .youtube-container {
            margin-top: 20px;
        }

        .youtube-video {
            width: 100%;
            aspect-ratio: 16/9;
            border-radius: var(--border-radius);
            border: none;
        }

        @media (max-width: 600px) {
            .main-content {
                padding: 10px;
            }
            
            .container {
                padding: 15px;
            }
            
            h2 {
                font-size: 1.1rem;
            }
            
            .price {
                font-size: 0.9rem;
            }

            .nav-options {
                gap: 10px;
            }

            .nav-option {
                padding: 6px 12px;
                font-size: 0.9rem;
            }

            .news-container {
                grid-template-columns: 1fr;
            }
        }

        /* Loading animation */
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }

        #stocks.loading, #crypto.loading, #news.loading, #youtube.loading {
            animation: pulse 1.5s infinite;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="nav-options">
            <a href="#" class="nav-option active" onclick="showTab('market')">Live Market Data</a>
            <a href="#" class="nav-option" onclick="showTab('news')">Stock Market News & Videos</a>
        </div>
    </div>

    <div class="main-content">
        <!-- Market Data Tab -->
        <div id="market-tab">
            <div class="container">
                <h2>📊 Live Stock Prices (NSE/BSE)</h2>
                <div id="stocks" class="stock loading">
                    Loading stock data...
                </div>

                <h2>₿ Top 10 Cryptocurrencies</h2>
                <div id="crypto" class="crypto loading">
                    Loading crypto data...
                </div>
            </div>
        </div>

        <!-- News & Videos Tab -->
        <div id="news-tab" class="hidden">
            <div class="container">
                <h2>📰 Latest Stock Market News</h2>
                <div id="news" class="loading">
                    Loading news...
                </div>

                <h2>▶️ Live Market Updates on YouTube</h2>
                <div id="youtube" class="youtube-container loading">
                    Loading YouTube videos...
                </div>
            </div>
        </div>
    </div>

    <script>
        // Tab navigation
        function showTab(tabName) {
            document.querySelectorAll('.nav-option').forEach(option => {
                option.classList.remove('active');
            });
            event.target.classList.add('active');

            document.getElementById('market-tab').classList.add('hidden');
            document.getElementById('news-tab').classList.add('hidden');
            document.getElementById(`${tabName}-tab`).classList.remove('hidden');
        }

        // Fetch Stock Data (Using Alpha Vantage API)
        async function fetchStocks() {
            const stocksElement = document.getElementById('stocks');
            stocksElement.classList.remove('loading');
            
            const symbols = ['RELIANCE.BSE', 'TCS.BSE', 'HDFCBANK.BSE', 'INFY.BSE', 'SBIN.BSE'];
            let html = '';
            
            for (const symbol of symbols) {
                try {
                    const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=6AFY4VTCLQ050BBM`);
                    const data = await response.json();
                    const stock = data['Global Quote'];
                    
                    if (stock) {
                        const changePercent = parseFloat(stock['10. change percent'].replace('%', ''));
                        html += `
                            <div class="data-item">
                                <span class="ticker">${symbol.split('.')[0]}</span>
                                <span class="price ${changePercent >= 0 ? 'up' : 'down'}">₹${stock['05. price']}</span>
                                <span class="${changePercent >= 0 ? 'up' : 'down'} change-percent">${changePercent >= 0 ? '+' : ''}${changePercent}%</span>
                                <div class="volume">Volume: ${stock['06. volume']}</div>
                            </div>
                        `;
                    }
                } catch (error) {
                    console.error("Error fetching stock:", error);
                    html += `<div class="data-item">${symbol.split('.')[0]}: Data Error</div>`;
                }
            }
            
            stocksElement.innerHTML = html || "<div class='data-item'>Failed to load stocks. Try later.</div>";
        }

        // Fetch Crypto Data (Using CoinGecko API)
        async function fetchCrypto() {
            const cryptoElement = document.getElementById('crypto');
            cryptoElement.classList.remove('loading');
            
            try {
                const response = await fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10');
                const coins = await response.json();
                let html = '';
                
                coins.forEach(coin => {
                    const change = coin.price_change_percentage_24h;
                    html += `
                        <div class="data-item">
                            <span class="ticker">${coin.symbol.toUpperCase()}</span>
                            <span class="price ${change >= 0 ? 'up' : 'down'}">$${coin.current_price.toLocaleString()}</span>
                            <span class="${change >= 0 ? 'up' : 'down'} change-percent">${change >= 0 ? '+' : ''}${change.toFixed(2)}%</span>
                            <div class="volume">Vol: $${coin.total_volume.toLocaleString()}</div>
                        </div>
                    `;
                });
                
                cryptoElement.innerHTML = html;
            } catch (error) {
                cryptoElement.innerHTML = "<div class='data-item'>Failed to load crypto. Try later.</div>";
            }
        }

        // Fetch Market News using NewsAPI
        async function fetchNews() {
            const newsElement = document.getElementById('news');
            newsElement.classList.remove('loading');
            
            try {
                // Using your NewsAPI key for Indian business news
                const response = await fetch('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b8448e802b2941be863de893a9f60d68');
                const data = await response.json();
                
                if(data.status === "error") {
                    throw new Error(data.message);
                }
                
                let html = '<div class="news-container">';
                data.articles.slice(0, 5).forEach(article => {
                    html += `
                        <div class="news-item">
                            <div class="news-title"><a href="${article.url}" target="_blank">${article.title}</a></div>
                            <div class="news-source">${article.source.name} • ${new Date(article.publishedAt).toLocaleString()}</div>
                        </div>
                    `;
                });
                html += '</div>';
                
                newsElement.innerHTML = html;
            } catch (error) {
                console.error("NewsAPI Error:", error);
                // Fallback to mock data if API fails
                const mockNews = [
                    {
                        title: "Sensex jumps 500 points as banking stocks rally",
                        url: "#",
                        source: { name: "Economic Times" },
                        publishedAt: new Date().toISOString()
                    },
                    {
                        title: "RBI announces new measures to boost liquidity",
                        url: "#",
                        source: { name: "Business Standard" },
                        publishedAt: new Date().toISOString()
                    }
                ];
                
                let html = '<div class="news-container">';
                mockNews.forEach(article => {
                    html += `
                        <div class="news-item">
                            <div class="news-title"><a href="${article.url}" target="_blank">${article.title}</a></div>
                            <div class="news-source">${article.source.name} • ${new Date(article.publishedAt).toLocaleString()}</div>
                        </div>
                    `;
                });
                html += '</div>';
                
                newsElement.innerHTML = html + `<div class="data-item">Note: Using sample data as API request failed. Error: ${error.message}</div>`;
            }
        }

        // Fetch YouTube Videos
        async function fetchYouTube() {
            const youtubeElement = document.getElementById('youtube');
            youtubeElement.classList.remove('loading');
            
            try {
                // In a real app, you would use the YouTube API here
                // This is a mock implementation with placeholder videos
                const mockVideos = [
                    {
                        title: "Market Live: Sensex, Nifty Today | Stock Market Updates",
                        id: "dQw4w9WgXcQ" // Placeholder ID
                    },
                    {
                        title: "Today's Top Stocks to Watch | Market Analysis",
                        id: "dQw4w9WgXcQ" // Placeholder ID
                    }
                ];
                
                let html = '<div class="news-container">';
                mockVideos.forEach(video => {
                    html += `
                        <div class="news-item">
                            <div class="news-title">${video.title}</div>
                            <iframe class="youtube-video" src="https://www.youtube.com/embed/${video.id}" 
                                    title="${video.title}" frameborder="0" 
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                    allowfullscreen></iframe>
                        </div>
                    `;
                });
                html += '</div>';
                
                youtubeElement.innerHTML = html;
            } catch (error) {
                youtubeElement.innerHTML = "<div class='data-item'>Failed to load videos. Try later.</div>";
            }
        }

        // Initial fetch
        fetchStocks();
        fetchCrypto();
        fetchNews();
        fetchYouTube();
        
        // Refresh data periodically
        setInterval(fetchStocks, 5000);
        setInterval(fetchCrypto, 5000);
        setInterval(fetchNews, 30000);
        setInterval(fetchYouTube, 30000);
    </script>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TradeX - Modern Trading Platform</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6c5ce7;
            --secondary: #a29bfe;
            --dark: #2d3436;
            --light: #f5f6fa;
            --success: #00b894;
            --danger: #d63031;
            --warning: #fdcb6e;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Montserrat', sans-serif;
        }

        body {
            background-color: #1a1a2e;
            color: var(--light);
            overflow-x: hidden;
        }

        .app-container {
            display: grid;
            grid-template-columns: 250px 1fr;
            min-height: 100vh;
        }

        /* Sidebar Styles */
        .sidebar {
            background-color: #16213e;
            padding: 2rem 1rem;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        .logo {
            display: flex;
            align-items: center;
            margin-bottom: 2rem;
            padding-left: 1rem;
        }

        .logo-icon {
            font-size: 2rem;
            color: var(--primary);
            margin-right: 0.5rem;
        }

        .logo-text {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .nav-menu {
            list-style: none;
        }

        .nav-item {
            margin-bottom: 0.5rem;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .nav-item:hover {
            background-color: rgba(108, 92, 231, 0.2);
        }

        .nav-item.active {
            background-color: var(--primary);
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            color: var(--light);
            text-decoration: none;
            font-weight: 500;
        }

        .nav-icon {
            margin-right: 0.75rem;
            font-size: 1.25rem;
        }

        /* Main Content Styles */
        .main-content {
            padding: 2rem;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }

        .page-title {
            font-size: 1.75rem;
            font-weight: 600;
        }

        .user-profile {
            display: flex;
            align-items: center;
        }

        .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 0.75rem;
            object-fit: cover;
            border: 2px solid var(--primary);
        }

        .username {
            font-weight: 500;
        }

        /* Dashboard Grid */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .card {
            background-color: #16213e;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .card-title {
            font-size: 1rem;
            font-weight: 500;
            color: var(--secondary);
        }

        .card-value {
            font-size: 1.75rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .card-change {
            display: flex;
            align-items: center;
            font-size: 0.875rem;
        }

        .change-up {
            color: var(--success);
        }

        .change-down {
            color: var(--danger);
        }

        /* Chart Container */
        .chart-container {
            background-color: #16213e;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            height: 400px;
        }

        .chart-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }

        .chart-title {
            font-size: 1.25rem;
            font-weight: 600;
        }

        .chart-actions {
            display: flex;
            gap: 0.5rem;
        }

        .timeframe-btn {
            background-color: rgba(108, 92, 231, 0.2);
            border: none;
            color: var(--light);
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.875rem;
            transition: background-color 0.3s ease;
        }

        .timeframe-btn.active {
            background-color: var(--primary);
        }

        .timeframe-btn:hover {
            background-color: rgba(108, 92, 231, 0.4);
        }

        /* Trading Pairs */
        .trading-pairs {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .pair-card {
            background-color: #16213e;
            border-radius: 8px;
            padding: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }

        .pair-card:hover {
            border-color: var(--primary);
            transform: translateY(-3px);
        }

        .pair-card.active {
            border-color: var(--primary);
            background-color: rgba(108, 92, 231, 0.2);
        }

        .pair-name {
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .pair-price {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .pair-change {
            font-size: 0.875rem;
        }

        /* Order Form */
        .order-form {
            background-color: #16213e;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .form-header {
            display: flex;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .form-tab {
            padding: 0.75rem 1.5rem;
            cursor: pointer;
            font-weight: 500;
            position: relative;
        }

        .form-tab.active {
            color: var(--primary);
        }

        .form-tab.active::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0;
            width: 100%;
            height: 2px;
            background-color: var(--primary);
        }

        .form-group {
            margin-bottom: 1.25rem;
        }

        .form-label {
            display: block;
            margin-bottom: 0.5rem;
            font-size: 0.875rem;
            color: var(--secondary);
        }

        .form-input {
            width: 100%;
            padding: 0.75rem 1rem;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 6px;
            color: var(--light);
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }

        .form-input:focus {
            outline: none;
            border-color: var(--primary);
        }

        .form-row {
            display: flex;
            gap: 1rem;
        }

        .form-col {
            flex: 1;
        }

        .btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background-color: #5649d1;
            transform: translateY(-2px);
        }

        .btn-outline {
            background-color: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
        }

        .btn-outline:hover {
            background-color: rgba(108, 92, 231, 0.2);
        }

        /* Responsive Adjustments */
        @media (max-width: 1200px) {
            .dashboard-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .trading-pairs {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        @media (max-width: 992px) {
            .app-container {
                grid-template-columns: 1fr;
            }
            
            .sidebar {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
            
            .trading-pairs {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .form-row {
                flex-direction: column;
                gap: 1.25rem;
            }
        }

        @media (max-width: 576px) {
            .trading-pairs {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="logo">
                <span class="logo-icon">📈</span>
                <span class="logo-text">TradeX</span>
            </div>
            <ul class="nav-menu">
                <li class="nav-item active">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">🏠</span>
                        <span>Dashboard</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">💹</span>
                        <span>Markets</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">💰</span>
                        <span>Portfolio</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">⚙️</span>
                        <span>Settings</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">📊</span>
                        <span>Analytics</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <span class="nav-icon">🔒</span>
                        <span>Security</span>
                    </a>
                </li>
            </ul>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="header">
                <h1 class="page-title">Trading Dashboard</h1>
                <div class="user-profile">
                    <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="User" class="user-avatar">
                    <span class="username">Jessica Parker</span>
                </div>
            </header>

            <!-- Dashboard Stats -->
            <div class="dashboard-grid">
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-title">Portfolio Value</h3>
                        <span>💰</span>
                    </div>
                    <h2 class="card-value">$24,589.42</h2>
                    <div class="card-change change-up">
                        <span>↑ 2.4%</span>
                        <span>($589.42)</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-title">Available Balance</h3>
                        <span>💳</span>
                    </div>
                    <h2 class="card-value">$5,420.00</h2>
                    <div class="card-change change-up">
                        <span>↑ 1.2%</span>
                        <span>($64.20)</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-title">24h Profit/Loss</h3>
                        <span>📉</span>
                    </div>
                    <h2 class="card-value">$842.50</h2>
                    <div class="card-change change-down">
                        <span>↓ 1.8%</span>
                        <span>($154.30)</span>
                    </div>
                </div>
            </div>

            <!-- Trading Chart -->
            <div class="chart-container">
                <div class="chart-header">
                    <h2 class="chart-title">BTC/USDT</h2>
                    <div class="chart-actions">
                        <button class="timeframe-btn active">1H</button>
                        <button class="timeframe-btn">4H</button>
                        <button class="timeframe-btn">1D</button>
                        <button class="timeframe-btn">1W</button>
                        <button class="timeframe-btn">1M</button>
                    </div>
                </div>
                <div id="trading-chart" style="height: 320px;">
                    <!-- Chart will be rendered here -->
                    <div style="display: flex; justify-content: center; align-items: center; height: 100%; color: var(--secondary);">
                        Trading Chart Placeholder (would connect to TradingView or similar API)
                    </div>
                </div>
            </div>

            <!-- Trading Pairs -->
            <div class="trading-pairs">
                <div class="pair-card active">
                    <div class="pair-name">BTC/USDT</div>
                    <div class="pair-price">$42,589.32</div>
                    <div class="pair-change change-up">+2.4%</div>
                </div>
                <div class="pair-card">
                    <div class="pair-name">ETH/USDT</div>
                    <div class="pair-price">$2,345.67</div>
                    <div class="pair-change change-up">+1.8%</div>
                </div>
                <div class="pair-card">
                    <div class="pair-name">SOL/USDT</div>
                    <div class="pair-price">$98.76</div>
                    <div class="pair-change change-down">-0.8%</div>
                </div>
                <div class="pair-card">
                    <div class="pair-name">ADA/USDT</div>
                    <div class="pair-price">$0.4567</div>
                    <div class="pair-change change-up">+3.2%</div>
                </div>
            </div>

            <!-- Order Form -->
            <div class="order-form">
                <div class="form-header">
                    <div class="form-tab active">Buy</div>
                    <div class="form-tab">Sell</div>
                    <div class="form-tab">Limit</div>
                    <div class="form-tab">Stop</div>
                </div>
                <form id="trade-form">
                    <div class="form-row">
                        <div class="form-col">
                            <div class="form-group">
                                <label for="order-type" class="form-label">Order Type</label>
                                <select id="order-type" class="form-input">
                                    <option value="market">Market</option>
                                    <option value="limit">Limit</option>
                                    <option value="stop">Stop-Limit</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="amount" class="form-label">Amount (BTC)</label>
                                <input type="number" id="amount" class="form-input" placeholder="0.00">
                            </div>
                        </div>
                        <div class="form-col">
                            <div class="form-group">
                                <label for="price" class="form-label">Price (USDT)</label>
                                <input type="number" id="price" class="form-input" placeholder="0.00">
                            </div>
                            <div class="form-group">
                                <label for="total" class="form-label">Total (USDT)</label>
                                <input type="number" id="total" class="form-input" placeholder="0.00" readonly>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Buy BTC</button>
                    </div>
                    <div class="form-group" style="text-align: center;">
                        <small style="color: var(--secondary);">Available: $5,420.00 USDT</small>
                    </div>
                </form>
            </div>
        </main>
    </div>

    <script>
        // Simple JavaScript for the trading platform
        document.addEventListener('DOMContentLoaded', function() {
            // Pair selection
            const pairCards = document.querySelectorAll('.pair-card');
            pairCards.forEach(card => {
                card.addEventListener('click', function() {
                    pairCards.forEach(c => c.classList.remove('active'));
                    this.classList.add('active');
                    document.querySelector('.chart-title').textContent = this.querySelector('.pair-name').textContent;
                });
            });

            // Timeframe selection
            const timeframeBtns = document.querySelectorAll('.timeframe-btn');
            timeframeBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    timeframeBtns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                });
            });

            // Form tabs
            const formTabs = document.querySelectorAll('.form-tab');
            formTabs.forEach(tab => {
                tab.addEventListener('click', function() {
                    formTabs.forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                });
            });

            // Calculate total when amount or price changes
            const amountInput = document.getElementById('amount');
            const priceInput = document.getElementById('price');
            const totalInput = document.getElementById('total');
            
            function calculateTotal() {
                const amount = parseFloat(amountInput.value) || 0;
                const price = parseFloat(priceInput.value) || 0;
                totalInput.value = (amount * price).toFixed(2);
            }
            
            amountInput.addEventListener('input', calculateTotal);
            priceInput.addEventListener('input', calculateTotal);

            // Form submission
            const tradeForm = document.getElementById('trade-form');
            tradeForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const amount = parseFloat(amountInput.value);
                const price = parseFloat(priceInput.value);
                
                if (!amount || !price) {
                    alert('Please enter valid amount and price');
                    return;
                }
                
                alert(`Order placed: ${amount} BTC at ${price} USDT\nTotal: ${amount * price} USDT`);
                tradeForm.reset();
                totalInput.value = '0.00';
            });
        });
    </script>
</body>
</html>