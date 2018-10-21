(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((< x 0) -1)
    (else 0))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) b) 
    ((= n 2) (square b))
    ((even? n) (square (pow b (/ n 2))))
    (else (* (square (pow b (/ (- n 1) 2))) b)))
)

(define (ordered? s)
  (cond
    ((null? (cdr s)) True)
    ((< (cadr s) (car s)) False)
    (else (ordered? (cdr s))))
)

(define (empty? s) (null? s))

(define (add s v)
    (cond
      ((empty? s) (list v))
      ((= (car s) v) s)
      ((< v (car s)) (append (list v) s))
      (else (append (list (car s)) (add (cdr s) v))))
    )

; Sets as sorted lists
(define (contains? s v)
    (cond
      ((empty? s) False)
      ((= (car s) v) True)
      (else (contains? (cdr s) v)))
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
    (cond
      ((or (empty? s) (empty? t)) ())
      ((= (car s) (car t)) (append (list (car s)) (intersect (cdr s) (cdr t))))
      ((< (car s) (car t)) (append (car s) (intersect (cdr s) t)))
      (else (append (car t) (intersect s (cdr t)))))
    )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond
      ((empty? s) t)
      ((empty? t) s)
      ((= (car s) (car t)) (append (list (car s)) (union (cdr s) (cdr t))))
      ((< (car s) (car t)) (append (list (car s)) (union (cdr s) t)))
      (else (append (list (car t)) (union s (cdr t))))
      )
    )