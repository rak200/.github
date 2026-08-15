<?php

declare(strict_types=1);

namespace Rak200\PhpMin;

/**
 * The whole product of this fixture.
 *
 * Deliberately trivial, and deliberately not *empty*: the fixture has to pass a coverage
 * floor and a mutation floor, and both are vacuous over a package with no behaviour. One
 * expression with a handful of killable mutants is the smallest thing that makes
 * `coverage` and `mutation` mean something, which is the point of exercising them here.
 *
 * @author rak200 <rak.ricardo@windowslive.com>
 */
final class Doubler
{
    /**
     * Doubles an integer.
     *
     * Multiplication rather than `$value + $value`, because the mutants differ: `*` has a
     * division mutant that returns a float and therefore trips the `int` return type under
     * `strict_types`, so a single assertion kills it. Addition's mutants are subtler and
     * would need more test than this fixture is worth.
     */
    public static function of(int $value): int
    {
        return $value * 2;
    }
}
