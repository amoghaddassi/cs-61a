;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>
(define (tree r)
 (if (< r 10) (begin (forward r) (backward r))
  (begin (forward (/ r 4))
   (right 30)
   (tree (/ r 2))
   (left 50)
   (tree (/ r 2))
   (right 20)
  (backward (/ r 4)))))

(define (tree-spiral size)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45)
 (tree size)
 (right 45))

(define root3 1.7320508)

(define (triangle x y s)
 (penup)
 (setposition x y)
 (pendown)
 (repeat-circle )
 (right 30)
 (forward s)
 (right 120)
 (forward s)
 (right 120)
 (forward s)
 (right 90)
 (penup))

(define (sierpinski x y s depth)
 (if (= depth 0) nil
  (begin
   (triangle x y s)
   (sierpinski x y (/ s 2) (- depth 1))
   (sierpinski (+ x (/ s 4)) (+ y (* (/ root3 4) s)) (/ s 2) (- depth 1))
   (sierpinski (+ x (/ s 2)) y (/ s 2) (- depth 1)))))

(define (sierpinski-invert x y s depth)
 (if (= depth 0) nil
  (begin
   (triangle x y s)
   (sierpinski-invert x y (/ s 2) (- depth 1))
   (sierpinski-invert (- x (/ s 4)) (- y (* (/ root3 4) s)) (/ s 2) (- depth 1))
   (sierpinski-invert (- x (/ s 2)) y (/ s 2) (- depth 1)))))


(define (hexagon x y s)
 (define depth 5)
 (begin
  (sierpinski x y s depth)
  (sierpinski (+ x (/ s 2)) (+ y (* (/ root3 2) s)) s depth)
  (sierpinski (- x (* s .5)) (+ y (* (/ root3 2) s)) s depth)
  (right 180)
  (sierpinski-invert (+ x s) (+ y (* root3 s)) s depth)
  (sierpinski-invert (+ x (* s 1.5)) (+ y (* (/ root3 2) s)) s depth)
  (sierpinski-invert (+ x (/ s 2)) (+ y (* (/ root3 2) s)) s depth)
  (right 180)))

(define (draw)
 (speed 10)
 (bgcolor (rgb 0 0 .3))
 (color (rgb .5 .5 0))
 (tree-spiral 300)
 ()
 (exitonclick))
(draw)