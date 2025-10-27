#lang racket

(define graph (make-hash
  (list [cons 's (list [cons 'a 3] [cons 'b 2])]
        [cons 'a (cons 'd 4)]
        [cons 'b (list [cons 'c 6] [cons 'e 4])]
        [cons 'c (cons 'g 1)]
        [cons 'd (cons 'f 5)]
        [cons 'e (cons 'g 2)]
        [cons 'f (cons 'g 7)]
        [cons 'g '()])))

(define heuristic (make-hash
  (list [cons 's 7]
        [cons 'a 6]
        [cons 'b 5]
        [cons 'c 2]
        [cons 'd 6]
        [cons 'e 1]
        [cons 'f 5]
        [cons 'g 0])))

(define (getConnectedNodes graph x)
    (cond
     [(hash-has-key? graph x) (hash-ref graph x)]
      [else #f]))

(define (getHeuristic heuristic x)
  (cond
    [(hash-has-key? heuristic x) (hash-ref heuristic x)]
    [else #f]))

(define (bfs #:start start
             #:goal goal
             #:graph graph)
  (cond
    [(and (hash? graph)
          (hash-has-key? graph start)
          (hash-has-key? graph goal))
     (let ([found_nodes    (make-hash)]
           [visited_nodes (make-hash)])
      (found_nodes))]
    [else (error "Invalid args")]))

(bfs #:graph graph
     #:start 's
     #:goal 'g)
