# config/prod.py - PROD environment configurations
# Replace the URLs below with your own internal service URLs

PROD_ENVIRONMENTS = [
    {
        "name": "Prod AWS",
        "services": [
            {
                "name": "Alertmanager",
                "url": "https://alertmanager.prod-aws.example.com/",
                "image": "static/logos/alertmanager.png",
                "icon": "🚨"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/prod-aws",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
            {
                "name": "Artifactory",
                "url": "https://artifactory.prod-aws.example.com/ui",
                "image": "static/logos/jfrog.png",
                "icon": "📦"
            },
            {
                "name": "Gangway (K8s Access)",
                "url": "https://gangway.prod-aws.example.com/",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.prod-aws.example.com/",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Jenkins",
                "url": "https://jenkins.prod-aws.example.com/",
                "image": "static/logos/Jenkins.png",
                "icon": "⚙️"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.prod-aws.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.prod-aws.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.prod-aws.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "Thanos",
                "url": "https://thanos.prod-aws.example.com",
                "image": "static/logos/thanos.png",
                "icon": "💎"
            },
            {
                "name": "AWS",
                "url": "https://YOUR_AWS_ACCOUNT_ID.signin.aws.amazon.com/console",
                "image": "static/logos/aws.png",
                "icon": "🔧"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.prod-aws.example.com/",
                "image": "static/logos",
                "icon": "🔑"
            },
        ]
    },
    {
        "name": "Prod Cilium",
        "services": [
            {
                "name": "Alertmanager",
                "url": "https://alertmanager.prod-cilium.example.com/",
                "image": "static/logos/alertmanager.png",
                "icon": "🚨"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/prod-cilium",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
            {
                "name": "Gangway (K8s Access)",
                "url": "https://gangway.prod-cilium.example.com/",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.prod-cilium.example.com",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Kafdrop",
                "url": "https://kafdrop.prod-cilium.example.com/",
                "image": "static/logos/kafka.png",
                "icon": "📨"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.prod-cilium.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.prod-cilium.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.prod-cilium.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "HZ4global",
                "url": "https://hz4global.prod-cilium.example.com",
                "image": "static/logos",
                "icon": "🔧"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.prod-cilium.example.com/",
                "image": "static/logos",
                "icon": "🔑"
            },
        ]
    },
    {
        "name": "Prod Cloud",
        "services": [
            {
                "name": "Artifactory (Registry)",
                "url": "https://registry.prod-cloud.example.com/ui/",
                "image": "static/logos/jfrog.png",
                "icon": "📦"
            },
            {
                "name": "K8s Access",
                "url": "https://your-wiki.example.com/display/YOUR_SPACE/Get+access+to+PROD-CLOUD",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "BitBucket",
                "url": "https://your-bitbucket.example.com/projects/YOUR_PROJECT/repos/YOUR_REPO/browse/k8s-config/prod-cloud",
                "image": "static/logos/BitBucket.png",
                "icon": "🚨"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.prod-cloud.example.com",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Jenkins",
                "url": "https://jenkins.prod-cloud.example.com/",
                "image": "static/logos/Jenkins.png",
                "icon": "⚙️"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.prod-cloud.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.prod-cloud.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.prod-cloud.example.com/",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "Vault",
                "url": "https://vault.prod-cloud.example.com/ui/",
                "image": "static/logos/vault.png",
                "icon": "🔐"
            },
            {
                "name": "HZ4global",
                "url": "https://hz4global.prod-cloud.example.com/",
                "image": "static/logos",
                "icon": "🔧"
            },
            {
                "name": "AWS-Keycloak",
                "url": "https://keycloak.prod-cloud.example.com/auth/realms/master/protocol/saml/clients/amazon-aws",
                "image": "static/logos/aws.png",
                "icon": "🔧"
            },
            {
                "name": "Sealed Secrets",
                "url": "https://sealed-secrets-web.prod-cloud.example.com/",
                "image": "static/logos",
                "icon": "🔑"
            },
        ]
    },
    {
        "name": "Prod Lite",
        "services": [
            {
                "name": "K8s Access",
                "url": "https://your-wiki.example.com/display/YOUR_SPACE/Get+access+to+PROD-LITE",
                "image": "static/logos/k8s.png",
                "icon": "🔑"
            },
            {
                "name": "Grafana",
                "url": "https://grafana.prod-lite.example.com",
                "image": "static/logos/Grafana.png",
                "icon": "📊"
            },
            {
                "name": "Prometheus",
                "url": "https://prometheus.prod-lite.example.com",
                "image": "static/logos/Prometheus.png",
                "icon": "📝"
            },
            {
                "name": "Rundeck",
                "url": "https://rundeck.prod-lite.example.com",
                "image": "static/logos/rundeck.png",
                "icon": "🔧"
            },
            {
                "name": "Kibana",
                "url": "https://kibana.prod-lite.example.com/",
                "image": "static/logos/kibana.png",
                "icon": "🔍"
            },
            {
                "name": "Jenkins",
                "url": "https://jenkins.prod-lite.example.com/",
                "image": "static/logos/Jenkins.png",
                "icon": "⚙️"
            },
        ]
    },
]
