export interface User {
  id: number
  username: string
  email: string
  bio?: string
  avatar_url?: string
  created_at: string
}

export interface AuthTokens {
  access: string
  refresh: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
  password_confirm: string
}

export interface Problem {
  id: number
  title: string
  slug: string
  description: string
  difficulty: 'easy' | 'medium' | 'hard'
  tags: string[]
  examples: Array<{
    input: string
    output: string
    explanation?: string
  }>
  constraints: string
  starter_code: string
  hints: string[]
  created_at: string
  updated_at: string
}

export interface Submission {
  id: number
  problem: number
  problem_title: string
  username: string
  code: string
  language: string
  status: 'pending' | 'accepted' | 'wrong_answer' | 'error'
  runtime?: number
  memory?: number
  error_message?: string
  submitted_at: string
}

export interface ApiError {
  message: string
  errors?: Record<string, string[]>
}
