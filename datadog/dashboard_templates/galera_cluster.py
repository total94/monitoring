title = 'Galera Cluster'
description = 'Galera Cluster metrics'

graphs = [
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "avg:mysql.performance.digest_95th_percentile.avg_us{$env,$host,$customerid} by {host} / 1000",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "bars",
                    "style": {
                        "palette": "warm"
                    }
                }
            ]
        },
        'title': '95th Percentile Query Response Time (ms)',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "avg:system.load.1{$env,$host,$customerid} by {host}",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "line"
                }
            ]
        },
        'title': 'Load Average',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "avg:system.cpu.user{$env,$customerid,$host} by {host}",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "line"
                }
            ]
        },
        'title': 'CPU %usr',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "avg:system.cpu.iowait{$env,$customerid,$host} by {host}",
                    "conditional_formats": [],
                    "type": "line",
                    "aggregator": "avg"
                }
            ]
        },
        'title': 'CPU %iowait',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "avg:system.mem.pct_usable{$env,$customerid,$host} by {host} * 100",
                    "aggregator": "avg",
                    "style": {
                        "palette": "warm",
                        "width": "normal"
                    },
                    "type": "line",
                    "conditional_formats": []
                }
            ]
        },
        'title': 'Memory Free (%)',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "( avg:system.disk.free{device:/,$env,$customerid,$host} by {host} / avg:system.disk.total{device:/,$env,$customerid,$host} by {host} ) * 100",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "bars"
                }
            ]
        },
        'title': 'Disk Free / (%)',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "( avg:system.disk.free{device:/var/log/mysql,$env,$customerid,$host} by {host} / avg:system.disk.total{device:/var/log/mysql,$env,$customerid,$host} by {host} ) * 100",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "bars"
                }
            ]
        },
        'title': 'Disk Free /var/log/mysql (%)',
    },
    {
        'definition': {
            "viz": "timeseries",
            "requests": [
                {
                    "q": "( avg:system.disk.free{device:/var/lib/mysql,$env,$customerid,$host} by {host} / avg:system.disk.total{device:/var/lib/mysql,$env,$customerid,$host} by {host} ) * 100",
                    "aggregator": "avg",
                    "conditional_formats": [],
                    "type": "bars"
                }
            ]
        },
        'title': 'Disk Free /var/lib/mysql (%)',
    }
]
