# Changelog

## [1.13.0](https://github.com/rak200/.github/compare/1.12.0...1.13.0) (2026-08-14)


### Features

* CodeQL runs on the JS side, as the RFC decided and this file never did ([#38](https://github.com/rak200/.github/issues/38)) ([ab5b924](https://github.com/rak200/.github/commit/ab5b924f33c40010b0a651564cd654adada0c4b1))

## [1.12.0](https://github.com/rak200/.github/compare/1.11.1...1.12.0) (2026-08-13)


### Features

* the PR title is checked, because the title is the commit ([#36](https://github.com/rak200/.github/issues/36)) ([fb17904](https://github.com/rak200/.github/commit/fb1790482105d6ebe4da6cf2a72b513470ad754d))

## [1.11.1](https://github.com/rak200/.github/compare/1.11.0...1.11.1) (2026-08-06)


### Reverts

* drop the reusable auto-merge workflow and put the branch rules back in one ruleset ([#28](https://github.com/rak200/.github/issues/28)) ([c9412d0](https://github.com/rak200/.github/commit/c9412d05b9da8e3a536810a9ac3e4a8c9faa2542))

## [1.11.0](https://github.com/rak200/.github/compare/1.10.0...1.11.0) (2026-08-06)


### Features

* merge the baseline bump without a human, and split the branch ruleset to allow it ([#24](https://github.com/rak200/.github/issues/24)) ([1c646f7](https://github.com/rak200/.github/commit/1c646f7727fbd308612720e6b8d38aac27a7728b))

## [1.10.0](https://github.com/rak200/.github/compare/1.9.1...1.10.0) (2026-08-03)


### Features

* a stale pipeline pin is a finding, not a habit ([#21](https://github.com/rak200/.github/issues/21)) ([ae5c8ca](https://github.com/rak200/.github/commit/ae5c8ca22e58c2b7aa915d83494fffb565b60020))


### Bug Fixes

* restore the reusable release workflow, and assert every pinned one is callable ([#22](https://github.com/rak200/.github/issues/22)) ([2918f43](https://github.com/rak200/.github/commit/2918f43d1267dd24e0a7e4acccdf908d07d4d0a6))

## [1.9.1](https://github.com/rak200/.github/compare/1.9.0...1.9.1) (2026-08-03)


### Bug Fixes

* the mutation filter skipped every JavaScript source ([#19](https://github.com/rak200/.github/issues/19)) ([f65ec54](https://github.com/rak200/.github/commit/f65ec549e95541fdfc35201cd01285305ca8856e))

## [1.9.0](https://github.com/rak200/.github/compare/1.8.1...1.9.0) (2026-08-03)


### Features

* the language pipelines take a variant, so the -config packages can use them ([#17](https://github.com/rak200/.github/issues/17)) ([25e4688](https://github.com/rak200/.github/commit/25e4688fdd0ceb66836cd990f959c9bf6a7b4353))

## [1.8.1](https://github.com/rak200/.github/compare/1.8.0...1.8.1) (2026-08-03)


### Bug Fixes

* assert the validate verb before publishing, not at the last step ([#14](https://github.com/rak200/.github/issues/14)) ([5162a29](https://github.com/rak200/.github/commit/5162a293fb7a556fe1ebb7625d19a72c8850ecfc))
