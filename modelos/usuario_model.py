from pydantic import BaseModel, Field, EmailStr

class Usuario(BaseModel):
    id: int = Field(..., ge=1, description="Identificador unico del usuario")
    name: str = Field(..., min_length=8, max_length=66, description="Nombre completo del usuario")
    email: EmailStr = Field(..., description="Correo electronico del usuario")
    password: str = Field(..., min_length=8, max_length=16, description="Contraseña del usuario")
    is_active: bool = Field(..., description="Estado del usuario, si esta activo o no")
    
    
    model_config={
        "json_Schema_extra":{
            "example":{
                "id": 1,
                "name": "Juan Perez",
                "email": "juan.perez@example.com",
                "password": "password123",
                "is_active": True
            }
        }
    }