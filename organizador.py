from pathlib import Path
import shutil

from pathlib import Path
import shutil


def organizar_arquivos():
    pasta_origem = Path("origem")
    """ 
    Também podemos passar um caminho para uma pasta fora do diretório do script, por exemplo a de Downloads
    #PASTA_ORIGEM = Path(r"C:\Users\SeuUsuario\Downloads")
    
    """
    
    mapeamento = {
        ".jpg": "Imagens",
        ".jpeg": "Imagens",
        ".png": "Imagens",

        ".pdf": "Documentos",
        ".docx": "Documentos",
        ".txt": "Documentos",

        ".mp4": "Videos",
        ".mkv": "Videos",

        ".zip": "Compactados",
        ".rar": "Compactados"
    }

    
    for item in pasta_origem.iterdir():
        if item.is_file():
            extensao = item.suffix.lower()

            
            if extensao in mapeamento:
                pasta_destino = pasta_origem / mapeamento[extensao]

                
                pasta_destino.mkdir(exist_ok=True)

                destino_final = pasta_destino / item.name

                # Evita sobrescrever arquivos com o mesmo nome
                contador = 1
                while destino_final.exists():
                    novo_nome = f"{item.stem}_{contador}{item.suffix}"
                    destino_final = pasta_destino / novo_nome
                    contador += 1

                
                shutil.move(str(item), str(destino_final))
                print(f"Movido: {item.name} → {destino_final}")

            else:
                print(f"Ignorado (extensão não mapeada): {item.name}")


if __name__ == "__main__":
    organizar_arquivos()