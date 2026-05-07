# config/lab.py - LAB environment configurations
# Replace the URLs below with your own internal service URLs

LAB_ENVIRONMENTS = [
    {
        "name": "Lab AWS",
        "services": [
            {
                "name": "Alertmanager",
                "url": "https://alertmanager.lab-aws.example.com/#/alerts",
                "image": "static/logos/alertmanager.png",
                "icon": "🚨"
            },
            {
                "name": "Artifactory",
                "url": "https://artifactory.lab-aws.example.com/ui/",
                "image": "static/logos/jfrog.png",
                "icon": "📦"
            },
            {
                "name": "Gangway (K8s Access)",
                "url": "https://gangway.lab-aws.example.com/",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.lab-aws.example.com",
                "image": "static/logos",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.lab-aws.example.com/",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Jenkins",
                "url": "https://jenkins.lab-aws.example.com/",
                "image": "static/logos/jenkins1.png",
                "icon": "⚙️"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.lab-aws.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.lab-aws.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.lab-aws.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "Thanos",
                "url": "https://thanos.lab-aws.example.com/",
                "image": "static/logos/thanos1.png",
                "icon": "💎"
            },
            {
                "name": "HZ4global",
                "url": "https://hz4global.lab-aws.example.com",
                "image": "static/logos",
                "icon": "🔧"
            },
            {
                "name": "AWS",
                "url": "https://YOUR_AWS_ACCOUNT_ID.signin.aws.amazon.com/console",
                "image": "static/logos/aws.png",
                "icon": "🔧"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/lab-aws",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
        ]
    },
    {
        "name": "Lab ECX",
        "services": [
            {
                "name": "Alertmanager",
                "url": "https://alertmanager.lab-ecx.example.com/#/alerts",
                "image": "static/logos/alertmanager.png",
                "icon": "🚨"
            },
            {
                "name": "Gangway (K8s Access)",
                "url": "https://gangway.lab-ecx.example.com/",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.lab-ecx.example.com/",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.lab-ecx.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.lab-ecx.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.lab-ecx.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "HZ4global",
                "url": "https://hz4global.lab-ecx.example.com",
                "image": "static/logos",
                "icon": "🔧"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.lab-ecx.example.com",
                "image": "static/logos",
                "icon": "🔑"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/lab-ecx",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
        ]
    },
    {
        "name": "Lab Cloud",
        "services": [
            {
                "name": "Artifactory (Registry)",
                "url": "https://registry.lab-cloud.example.com/ui/",
                "image": "static/logos/jfrog.png",
                "icon": "📦"
            },
            {
                "name": "K8s Access",
                "url": "https://your-wiki.example.com/pages/viewpage.action?pageId=YOUR_PAGE_ID",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.lab-cloud.example.com",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Jenkins",
                "url": "https://jenkins.lab-cloud.example.com/",
                "image": "static/logos/Jenkins.png",
                "icon": "⚙️"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.lab-cloud.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.lab-cloud.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "Vault",
                "url": "https://vault.lab-cloud.example.com/ui/",
                "image": "static/logos/vault.png",
                "icon": "🔐"
            },
            {
                "name": "HZ4global",
                "url": "https://hz4global.lab-cloud.example.com",
                "image": "static/logos",
                "icon": "🔧"
            },
            {
                "name": "AWS-Keycloak",
                "url": "https://keycloak.lab-cloud.example.com/auth/realms/master/protocol/saml/clients/amazon-aws",
                "image": "static/logos/aws.png",
                "icon": "🔧"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.lab-cloud.example.com/",
                "image": "static/logos",
                "icon": "🔑"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/lab-cloud",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
        ]
    },
]
