from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    cv = {
        "nom": "Simone F.",
        "titre": "Etudiante à l'EFREI Paris | Future Data Engineer", 
        "presentation": [
            "Après 5 ans d’expérience au sein de différents services marketing, j’ai développé un réel intérêt pour l’analyse et l’exploitation des données.",
            "Cette évolution m’a conduite à faire une reconversion vers les métiers de la data.",
            "J’intègre ainsi le Mastère Data Engineering et Intelligence Artificielle de l’EFREI et je suis à la recherche d’une entreprise pouvant m’accueillir dans le cadre d’une alternance de 2 ans à partir de septembre 2026.",
            "Sérieuse, impliquée et à l’aise avec l’analyse de données, je cherche une entreprise où je pourrai apprendre et progresser dans les domaines techniques de la DATA."
        ],
        "experiences": [
            {
                "poste": "Traffic Manager",
                "entreprise": "Ornikar",
                "periode": "2024 – 2026 | CDI",
                "missions": [
                    "Analyse des données web et mobile pour le suivi de la performance produit",
                    "Création de dashboards de pilotage et suivi des KPI",
                    "Analyse statistique des performances et identification d’axes d’optimisation",
                    "Conception et analyse d’A/B tests sur les campagnes"
                ],
                "technos": "BigQuery, Looker Studio, Google Ads, AB Tasty, Suite Office"
            },
            {
                "poste": "Consultante SEA",
                "entreprise": "Agence KLH",
                "periode": "2023 – 2024 | CDI",
                "missions": [
                    "Analyse des données de performance de clients e-commerce",
                    "Interprétation des résultats et recommandations d’optimisation",
                    "Collaboration avec équipes marketing et data"
                ],
                "technos": "Excel macros, GSheet, Google Ads, Google Analytics"
            },
            {
                "poste": "Consultante SEA",
                "entreprise": "Agence Artefact",
                "periode": "2021 – 2023 | CDI",
                "missions": [
                    "Analyse de données marketing multi-marchés, 15 pays",
                    "Création de dashboards automatisés de suivi de performance",
                    "Structuration et exploitation des données pour recommandations business",
                    "Travail en transverse avec équipes data et clients"
                ],
                "technos": "Looker Studio, Excel macros, Google Ads, Suite Office"
            },
            {
                "poste": "Cheffe de projet SEO/SEA",
                "entreprise": "Bouygues Telecom",
                "periode": "2019 – 2021 | Alternance",
                "missions": [
                    "Analyse des performances digitales paid et organique",
                    "Suivi des KPI et contribution aux bilans de performance",
                    "Construction de reportings et recommandations d’optimisation",
                    "Coordination d’agences et formation des équipes internes"
                ],
                "technos": "Excel, GSheet, Search Ads 360, Google Analytics, SEMRush, Google Search Console, Google Ads"
            }
        ],
        "hard_skills": [
            "SQL",
            "PostgreSQL",
            "BigQuery",
            "Power BI",
            "Statistiques inférentielles",
            "Notions algorithmiques en Python 3",
            "Excel macros",
            "GSheet, TCD",
            "Looker Studio"
        ],
        "soft_skills": [
            "Capacité à chercher des solutions",
            "Curiosité et apprentissage continu",
            "Esprit analytique",
            "Rigueur et sens du détail"
        ],
        "langues": [
            "Portugais : Courant C2",
            "Espagnol : Courant C1",
            "Anglais : Professionnel B2"
        ],
        "formations": [
            {
                "ecole": "EFREI Paris",
                "periode": "2026 – 2028",
                "diplome": "Mastère Data Engineering et IA",
                "details": "Expérience professionnelle : alternance"
            },
            {
                "ecole": "Institut Léonard de Vinci",
                "periode": "2019-2021",
                "diplome": "Mastère Communication Digitale",
                "details": "Expérience professionnelle : alternance"
            },
            {
                "ecole": "IUT Cergy-Pontoise",
                "periode": "2018-2019",
                "diplome": "Licence Communication",
                "details": "Expérience professionnelle : alternance"
            },
            {
                "ecole": "Ecole Nationale de Commerce Bessières",
                "periode": "2016-2018",
                "diplome": "BTS Tourisme",
                "details": "Expérience professionnelle : stages à l'étranger (Espagne - Pamplona))"
            }
        ],
        "projets": [
            {
                "nom": "Lapikit.dev",
                "description": "Librairie de composants Svelte",
                "missions": [
                    "Extraction de données DDL sur NPM",
                    "Construction de dashboards de suivi",
                    "Analyse des usages de la communauté"
                ]
            }
        ],
        "certifications": [
            "Data Science - Udemy",
            "Google Analytics"
        ],
        "contact": {
            "email": "sidesousfernan@gmail.com",
            "discord": "@simonyinmine",
            "linkedin": "https://bit.ly/linkedInSimone",
            "github": "https://github.com/fersimone"
        }
    }

    return render_template("index.html", cv=cv)


#if __name__ == "__main__":
#    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)