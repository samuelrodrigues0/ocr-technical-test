import cv2
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path

class ImageHandler:
    """Classe responsavel por carregar imagens/pdfs e realizar o pré-processamento"""

    def __init__(self, file_path : Path):
        if not isinstance(file_path, Path):
            raise TypeError(f"Esperado Path, tipo recebido: {type(file_path)}")
        if not file_path.exists():
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado")

        self.file_path : Path = file_path
        self.images : list[np.ndarray] = self._load()
        self.preprocessed_images : list[np.ndarray] | None = None
    
    @property
    def file_extension(self) -> str:
        """Retorna a extensão do arquivo"""
        return self.file_path.suffix.lower()

    def preprocess(self) -> list[np.ndarray]:
        """Para cada imagem, aplica transformação para escala cinza e depois realiza transformação binária"""
        self.preprocessed_images = self._apply_gray(self.images)
        self.preprocessed_images = self._apply_binary(self.preprocessed_images, 200, 255)
        return self.preprocessed_images
    
    def _load(self) -> list[np.ndarray]:
        """Carrega o arquivo através do endereço e retorna a lista com imagens"""
        if self.file_extension == ".pdf":
            return self._convert_pdf_to_images()
        elif self.file_extension in [".jpg", ".jpeg", ".png"]:
            image = cv2.imread(str(self.file_path))
            if image is None:
                raise OSError(f"Não foi possível carregar a imagem do caminho: {self.file_path}")
            return [image]
        else:
            raise ValueError(f"Extensão '{self.file_extension}' não suportada. Use jpeg, jpg, png ou pdf")  
        
    def _convert_pdf_to_images(self) -> list[np.ndarray]:
        """Converte as folhas do pdf em lista de imagens numpy"""
        try:
            pillow_images = convert_from_path(str(self.file_path))
        except Exception as e:
            raise RuntimeError(f"Falha ao converter PDF '{self.file_path}': {e}")
        
        if not pillow_images:
            raise RuntimeError(f"Nenhuma página extraída de '{self.file_path}'")

        return [cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) for image in pillow_images]

    def _apply_gray(self, images : list[np.ndarray]) -> list[np.ndarray]:
        """Aplica escala cinza para cada imagem da lista"""
        return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in images]

    def _apply_binary(self, images : list[np.ndarray], threshold : int, max_value : int) -> list[np.ndarray]:
        """Aplica binarização para cada imagem da lista"""
        return [cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY)[1] for image in images]