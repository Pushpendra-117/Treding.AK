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