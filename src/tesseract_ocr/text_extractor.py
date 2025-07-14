import pytesseract
import numpy as np
from pathlib import Path

class TextExtractor:
    """Classe responsavel por processar as imagens pelo Tesseract e salvar em texto"""

    def __init__(self, language : str = 'por', config : str = ''):
        if not isinstance(language, str):
            raise TypeError(f"language deve ser str, não {type(language)}")
        if not isinstance(config, str):
            raise TypeError(f"config deve ser str, não {type(config)}")

        self.config = config
        self.language = language

    def extract(self, image : np.ndarray) -> str:
        """Extrai o texto da imagem"""
        if not isinstance(image, np.ndarray):
            raise TypeError(f"Esperado np.ndarray, recebeu {type(image)}")
        
        try:
            return pytesseract.image_to_string(image, lang=self.language, config=self.config)
        except pytesseract.TesseractError as e:
            raise RuntimeError(f"Falha na extração de texto: {e}")

    def save_to_file(self, text : str, path : Path):
        """Salva o texto em um arquivo de acordo com o endereço recebido"""
        if not isinstance(text, str):
            raise TypeError(f"text deve ser str, não {type(text)}")
        if not isinstance(path, Path):
            raise TypeError(f"path deve ser pathlib.Path, não {type(path)}")

        output_path = path
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as file_d:
                file_d.write(text)
        except OSError as e:
            raise RuntimeError(f"Não foi possível salvar em '{output_path}': {e}")

                