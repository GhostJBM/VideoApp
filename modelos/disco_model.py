from pydantic import BaseModel, Field, EmailStr

class Disco:
    codigo: str = Field(...,min_length=8, max_length=8, description="codigo de identificacion unico de la entidad")
    nome: str = Field(...,min_length=8, max_length=66, description="Titulo o nombre de la pelicula")
    sinopsis: str = Field(..., min_length=16, max_length=256, description="sinopsis de la pelicula")
    director: str = Field(...,min_length=4, max_length=66, description="Nombre del director de la pelicula")
    duracion: int = Field(...,ge=1, le=2, description="Tiempo de duracion de la pelicula")
    temanio: int = Field(...,ge=1, le=5, description="Tamaño de la pelicula en GB")
    precio_venta: int = Field(..., ge=100, le=500, description="Precio al que se vende el disco digital")
    precio_renta: int = Field(..., ge=50, le=70, description="Precio al que se renta el disco digital")

    model_config={
        "json_Schema_extra":{
            "example":{
                "name": "Lilo & Stitch",
                "sinopsis": "Una niño hawaiana llamada Lilo adopta un cachorro alienigena que ayuda a reconponer su"
                            "familia. Eso si, no sin antes sembrar el caos en las islas hawaianas con comicas travesuras",
                 "director": "Dean Fleischer Camp",
                 "temanio": 3,
                 "precio_venta": 400,
                 "precio_renta": 70,
                 "codigo": "cod-100",
            }
        }
    }