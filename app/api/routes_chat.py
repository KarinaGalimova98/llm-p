from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_chat_usecase, get_current_user_id
from app.core.errors import ExternalServiceError
from app.schemas.chat import ChatMessagePublic, ChatRequest, ChatResponse
from app.usecases.chat import ChatUseCase

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(
    data: ChatRequest,
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
) -> ChatResponse:
    try:
        answer = await usecase.ask(
            user_id=user_id,
            prompt=data.prompt,
            system=data.system,
            max_history=data.max_history,
            temperature=data.temperature,
        )
        return ChatResponse(answer=answer)
    except ExternalServiceError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc


@router.get("/history", response_model=list[ChatMessagePublic])
async def get_history(
    limit: int = Query(default=50, ge=1, le=200),
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
) -> list[ChatMessagePublic]:
    items = await usecase.get_history(user_id=user_id, limit=limit)
    return [ChatMessagePublic.model_validate(item) for item in items]


@router.delete("/history")
async def delete_history(
    user_id: int = Depends(get_current_user_id),
    usecase: ChatUseCase = Depends(get_chat_usecase),
) -> dict[str, str]:
    await usecase.clear_history(user_id=user_id)
    return {"detail": "History deleted"}