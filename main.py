import os
import argparse
from pathlib import Path
from tesseract_ocr import image_handler, text_extractor

def main():
    # Gerenciamento dos argumentos passados via cli
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Caminho do arquivo .jpg, .png, .jpeg, ou .pdf")
    parser.add_argument(
        "--output", 
        type=str, 
        choices=["cli", "txt", "both"], 
        default="cli", 
        help="Especifica como o texto deve ser tratado. {cli : Texto no console; txt : Salvo em arquivo txt; both: Ambos}")
    
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path("outputs")

    # Tenta abrir o arquivo e faz tratamentos de arquivo não encontrado ou com extensão não suportada.
    try:
        images = image_handler.ImageHandler(input_path)
    except FileNotFoundError:
        print(f"Arquivo {input_path} não encontrado, verifique o endereço.")
        return
    except ValueError:
        print(f'Extensão de arquivo {input_path.suffix} não suportado. Apenas .jpg, .jpeg, .png e .pdf')
        return

    # Aplica escala cinza e transformação binária na imagem
    images = images.preprocess()

    ocr_processor = text_extractor.TextExtractor('por+eng')
    texts_from_images = [ocr_processor.extract(image) for image in images]

    # Em caso de entrada em .pdf, multiplas imagens serão processadas, de acordo com as páginas
    for idx, text in enumerate(texts_from_images):
        if args.output in ("cli", "both"):
            print(text)

        if args.output in ("txt", "both"):
            print(f"Arquivos salvos em '{output_path.resolve()}'")
            out_filename = f"{input_path.stem}_{idx}.txt" if len(texts_from_images) > 1 else f"{input_path.stem}.txt"
            ocr_processor.save_to_file(text, output_path / out_filename)


if __name__ == "__main__":
    main()