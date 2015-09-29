#lang racket
(require picturing-programs)

(define (nearest-pot x)
  (expt 2
        (ceiling (/ (log x) (log 2)))))

(define (image-to-pot-dimensions img)
  (place-image/align img
                     0 0
                     'left 'top
                     (rectangle (nearest-pot (image-width img))
                                (nearest-pot (image-height img))
                                'outline
                                (color 0 0 0 0))))

(define (convert-image path)
  (save-image (image-to-pot-dimensions (bitmap/file path)) path))

(convert-image (vector-ref (current-command-line-arguments) 0))