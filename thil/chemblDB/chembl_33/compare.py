import pandas as pd

def extract_unique_molecules(file_main: str, file_compare: str) -> pd.DataFrame:
    """
    Extrai as moléculas que estão no arquivo `file_main` mas não no arquivo `file_compare`.

    Args:
    - file_main (str): Caminho do arquivo principal TSV.
    - file_compare (str): Caminho do arquivo TSV para comparação.

    Returns:
    - DataFrame: DataFrame contendo molregno e canonical_smiles das moléculas únicas.
    """
    df_main = pd.read_csv(file_main, sep="\t")
    df_compare = pd.read_csv(file_compare, sep="\t")

    # Encontra os molregnos que estão apenas no arquivo principal
    unique_molregnos = set(df_main['molregno']) - set(df_compare['molregno'])

    # Filtra o DataFrame principal para obter apenas as linhas com molregnos únicos
    unique_molecules = df_main[df_main['molregno'].isin(unique_molregnos)]

    return unique_molecules[['molregno', 'canonical_smiles']]

if __name__ == "__main__":
    # Define os caminhos dos arquivos
    file_main = "./filtered_chembl_33.tsv"
    file_compare = "./filtered_chembl_33_IC50.tsv"

    # Extraia moléculas únicas
    unique_molecules_df = extract_unique_molecules(file_main, file_compare)

    # Salva o resultado em um arquivo TSV
    output_file = "./compare_chembl33_and_chembl33_IC50.tsv"
    unique_molecules_df.to_csv(output_file, sep="\t", index=False)
