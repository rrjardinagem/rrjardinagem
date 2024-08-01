import os

def rename_images(directory, prefix='formaçao_de_jardim'):
    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        print(f"O diretório {directory} não existe.")
        return
    
    # Lista todos os arquivos no diretório
    files = os.listdir(directory)
    
    # Filtra apenas os arquivos de imagem (jpg, jpeg, png, gif)
    image_files = [f for f in files if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    # Ordena os arquivos para garantir uma sequência consistente
    image_files.sort()

    # Renomeia os arquivos de imagem em sequência
    for index, filename in enumerate(image_files, start=1):
        # Obtém a extensão do arquivo
        file_extension = os.path.splitext(filename)[1]
        
        # Novo nome do arquivo
        new_name = f"{prefix}{index}{file_extension}"
        
        # Caminho completo para o arquivo antigo e novo
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Renomeia o arquivo
        os.rename(old_file, new_file)
        print(f"Renomeado: {old_file} -> {new_file}")

# Exemplo de uso
directory_path = './images/formaçao_de_jardim'  # Substitua pelo caminho da sua pasta de imagens

rename_images(directory_path)
