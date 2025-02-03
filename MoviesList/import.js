// import.js
const { CosmosClient } = require("@azure/cosmos");

// Substitua pelos seus dados
const endpoint = "<your_cosmos_db_endpoint>";
const key = "<your_cosmos_db_key>";
const databaseId = "<your_database_id>";
const containerId = "<your_container_id>";
const filePath = "./movies.json";

const client = new CosmosClient({ endpoint, key });

async function importData() {
  try {
    const database = client.database(databaseId);
    const container = database.container(containerId);

    const fs = require("fs");
    const data = JSON.parse(fs.readFileSync(filePath, "utf8"));

    for (const item of data) {
      await container.items.upsert(item);
      console.log(`Item ${item.id} importado com sucesso.`);
    }

    console.log("Importação concluída!");
  } catch (error) {
    console.error("Erro ao importar dados:", error);
  }
}

importData();