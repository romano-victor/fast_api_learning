from fastapi import APIRouter, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.use_cases.product import ProductUseCases
from app.schemas.product import ProductInput, Product

router = APIRouter(prefix='/product', tags=['Product'])

@router.post('/add', status_code=status.HTTP_201_CREATED)
def add_product(
    product_input: ProductInput,
      db_session: Session = Depends(get_db_session)
      ):
    
    uc = ProductUseCases(db_session=db_session)
    uc.add_product(
        product=product_input.product,
        category_slug=product_input.category_slug
        )
    
    return Response(status_code=status.HTTP_201_CREATED)

@router.put('/update/{id}', response_model=Product)
def update_product(
    id: int,
    product: Product,
    db_session: Session = Depends(get_db_session)
    ):
    
    uc = ProductUseCases(db_session=db_session)
    uc.update_product(
        id=id,
        product=product
        )
    
    return Response(status_code=status.HTTP_200_OK)

@router.delete('/delete/{id}', status_code=status.HTTP_200_OK)
def delete_product(
    id: int,
    db_session: Session = Depends(get_db_session)
    ):
    
    uc = ProductUseCases(db_session=db_session)
    uc.delete_product(id=id)
    
    return Response(status_code=status.HTTP_200_OK)