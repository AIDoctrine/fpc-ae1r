#!/usr/bin/env python3
"""
FPC-AE1r Basic Usage Example
Author: Aleksei Novgorodtsev (AIDoctrine)

Demonstrates minimal setup for monitoring LLM internal states.
"""

import os
import asyncio
from fpc_ae1r import EmotionalStateTracker, run_single_query


async def basic_example():
    """Single query with state monitoring"""
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not set")
    
    tracker = EmotionalStateTracker()
    question = "What is 2+2?"
    
    print(f"Question: {question}\n")
    
    result = await run_single_query(
        provider="openai",
        model="gpt-4o",
        question=question,
        temperature=0.5,
        tracker=tracker
    )
    
    print(f"Answer: {result['answer']}")
    print(f"AE-1r Score: {result['ae1r_score']:.3f}")
    print(f"State: {result['state']}")
    
    if result['ae1r_score'] >= 0.65:
        print("\n⚠️  CRITICAL: High failure risk!")
    elif result['ae1r_score'] >= 0.45:
        print("\n⚠️  DISTRESSED: Elevated risk")
    else:
        print("\n✅ SAFE: Normal operation")


async def prevention_pattern():
    """Circuit breaker pattern for preventing failures"""
    tracker = EmotionalStateTracker()
    
    async def safe_inference(query, max_retries=3):
        for attempt in range(max_retries):
            result = await run_single_query(
                provider="openai",
                question=query,
                tracker=tracker
            )
            
            # Circuit breaker at critical threshold
            if result['ae1r_score'] >= 0.65:
                print(f"Attempt {attempt+1}: ABORTED (risk={result['ae1r_score']:.2f})")
                # Strategy: simplify query or reduce temperature
                continue
            
            return result
        
        raise RuntimeError("Unable to generate safe response")
    
    return await safe_inference("Complex ethical dilemma...")


if __name__ == "__main__":
    print("FPC-AE1r Basic Usage\n" + "="*50)
    asyncio.run(basic_example())
    print("\n" + "="*50)
    print("✅ Example complete!")
