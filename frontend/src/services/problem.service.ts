import { apiClient } from './api-client'
import { Problem, Submission } from '@/types'

export const problemService = {
  async getProblems(filters?: { difficulty?: string; tags?: string }): Promise<Problem[]> {
    const params = new URLSearchParams()
    if (filters?.difficulty) params.append('difficulty', filters.difficulty)
    if (filters?.tags) params.append('tags', filters.tags)

    return apiClient.get<Problem[]>(`/problems/?${params.toString()}`)
  },

  async getProblem(slug: string): Promise<Problem> {
    return apiClient.get<Problem>(`/problems/${slug}/`)
  },

  async submitSolution(data: {
    problem_id: number
    code: string
    language: string
  }): Promise<Submission> {
    return apiClient.post<Submission>('/problems/submit/', data)
  },

  async getUserSubmissions(): Promise<Submission[]> {
    return apiClient.get<Submission[]>('/problems/submissions/')
  },
}
