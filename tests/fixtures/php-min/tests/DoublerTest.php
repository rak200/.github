<?php

declare(strict_types=1);

namespace Rak200\PhpMin\Tests;

use PHPUnit\Framework\TestCase;
use Rak200\PhpMin\Doubler;

/**
 * @internal
 *
 * @coversNothing
 */
final class DoublerTest extends TestCase
{
    public function testItDoublesAPositiveInteger(): void
    {
        // Three is chosen over two, and over any even number, on purpose: the division
        // mutant of `*` returns 1.5 here, which `strict_types` refuses against an `int`
        // return type. On an even input the same mutant returns a whole number and the
        // assertion has to catch it by value alone — thinner evidence for no gain.
        self::assertSame(6, Doubler::of(3));
    }

    public function testItDoublesANegativeInteger(): void
    {
        self::assertSame(-14, Doubler::of(-7));
    }

    public function testZeroDoublesToZero(): void
    {
        // The one input on which every arithmetic mutant agrees, asserted anyway: it is
        // the boundary a reader looks for, and leaving it out to keep the mutation score
        // honest would be optimising the fixture for its own score.
        self::assertSame(0, Doubler::of(0));
    }
}
