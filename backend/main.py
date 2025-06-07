from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from services.std_service import StdService
from typing import Dict, Any
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建 FastAPI 应用
app = FastAPI()

# 配置跨域资源共享
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化标准化服务
standardization_service = StdService()

class StandardizationRequest(BaseModel):
    """标准化请求模型"""
    text: str = Field(..., description="需要标准化的金融术语文本")
    embeddingOptions: Dict[str, str] = Field(
        default_factory=lambda: {
            "provider": "huggingface",
            "model": "BAAI/bge-m3"
        },
        description="嵌入模型配置选项"
    )

@app.post("/api/std")
async def standardize_terms(request: StandardizationRequest):
    """
    金融术语标准化接口
    
    Args:
        request: 包含文本和配置选项的请求体
        
    Returns:
        标准化结果列表
    """
    try:
        results = standardization_service.search_similar_terms(request.text)
        return {"results": results}
    except Exception as e:
        logger.error(f"标准化处理出错: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
