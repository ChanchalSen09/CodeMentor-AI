import { create } from 'zustand'
import { Problem, Submission } from '@/types'
import { problemService } from '@/services/problem.service'

interface ProblemState {
  problems: Problem[]
  currentProblem: Problem | null
  submissions: Submission[]
  isLoading: boolean
  error: string | null
  fetchProblems: (filters?: { difficulty?: string; tags?: string }) => Promise<void>
  fetchProblem: (slug: string) => Promise<void>
  submitSolution: (data: {
    problem_id: number
    code: string
    language: string
  }) => Promise<void>
  fetchUserSubmissions: () => Promise<void>
  clearError: () => void
}

export const useProblemStore = create<ProblemState>((set) => ({
  problems: [],
  currentProblem: null,
  submissions: [],
  isLoading: false,
  error: null,

  fetchProblems: async (filters) => {
    set({ isLoading: true, error: null })
    try {
      const problems = await problemService.getProblems(filters)
      set({ problems, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch problems'
      set({ error: message, isLoading: false })
    }
  },

  fetchProblem: async (slug) => {
    set({ isLoading: true, error: null })
    try {
      const problem = await problemService.getProblem(slug)
      set({ currentProblem: problem, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch problem'
      set({ error: message, isLoading: false })
    }
  },

  submitSolution: async (data) => {
    set({ isLoading: true, error: null })
    try {
      const submission = await problemService.submitSolution(data)
      set((state) => ({
        submissions: [submission, ...state.submissions],
        isLoading: false,
      }))
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to submit solution'
      set({ error: message, isLoading: false })
      throw error
    }
  },

  fetchUserSubmissions: async () => {
    set({ isLoading: true, error: null })
    try {
      const submissions = await problemService.getUserSubmissions()
      set({ submissions, isLoading: false })
    } catch (error) {
      const message = error instanceof Error ? error.message : 'Failed to fetch submissions'
      set({ error: message, isLoading: false })
    }
  },

  clearError: () => set({ error: null }),
}))
