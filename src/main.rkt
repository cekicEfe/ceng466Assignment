#lang racket

(define graph (list [list "s" 7 (cons "a" 3) (cons "b" 2)]
                    [list "a" 6 (cons "d" 4)]
                    [list "b" 5 (cons "c" 6) (cons "e" 4)]
                    [list "c" 2 (cons "g" 1)]
                    [list "d" 6 (cons "f" 5)]
                    [list "e" 1 (cons "g" 2)]
                    [list "f" 5 (cons "g" 7)]
                    [list "g" 0 '()]))

(define (getNode x graph)
  (let ([maybePair (assoc x graph)])
    (cond
      [(pair? maybePair)(cddr maybePair)]
      [else (error "Does not exist")])))

;(define (getHeuristicValue x graph)
;  )

(define (getConnectedNodes x graph)
  (let ([graph_pair (getNode x graph)])
    (cddr graph_pair)))

(display (getNode "s" graph))
;(display (getConnectedNodes "s" graph))
