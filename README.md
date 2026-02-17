#### 📁 Estrutura
```sh
phase3-epitope-vaccine-design/
│
├── app/
│   ├── pipeline.py
│   ├── epitope_prediction.py
│   ├── filtering.py
│   ├── vaccine_builder.py
│   ├── config.py
│   └── utils.py
│
├── data/
│   └── candidate_proteins.fasta
│
├── results/
│
├── logs/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

```

#### ▶️ Como Executar

- 1️⃣ Coloque o FASTA aqui:
```sh
data/candidate_proteins.fasta
```

- 2️⃣ Build
```sh
docker build -t phase3-pipeline .
```

- 3️⃣ Run
```sh
docker run -v $(pwd)/data:/app/data \
           -v $(pwd)/results:/app/results \
           -v $(pwd)/logs:/app/logs \
           phase3-pipeline
```
ou:
```sh
docker-compose up --build
```

📊 Output Final
```sh
results/multi_epitope_vaccine.fasta
logs/pipeline.log
```
