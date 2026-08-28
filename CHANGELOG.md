# Changelog

## [1.16.1](https://github.com/rak200/.github/compare/1.16.0...1.16.1) (2026-08-28)


### Bug Fixes

* two gates were green because they could not fail ([#58](https://github.com/rak200/.github/issues/58)) ([e63d96d](https://github.com/rak200/.github/commit/e63d96d3dc8b757101508709d9d2fcc8c3fe4aa4))

## [1.16.0](https://github.com/rak200/.github/compare/1.15.0...1.16.0) (2026-08-27)


### Features

* the gate inventory is derived from the workflows, not maintained beside them ([#52](https://github.com/rak200/.github/issues/52)) ([3f0db67](https://github.com/rak200/.github/commit/3f0db67a5ab22bc5c499187229d249cea764a8d4))

## [1.15.0](https://github.com/rak200/.github/compare/1.14.0...1.15.0) (2026-08-25)


### Features

* the ruleset read-back compares, and ships beside what it compares against ([#50](https://github.com/rak200/.github/issues/50)) ([72090c8](https://github.com/rak200/.github/commit/72090c8764fed8234d752b1bff00fa3420b7fe21))

## [1.14.0](https://github.com/rak200/.github/compare/1.13.1...1.14.0) (2026-08-25)


### Features

* declare the four ruleset parameters GitHub was injecting ([#48](https://github.com/rak200/.github/issues/48)) ([87ac093](https://github.com/rak200/.github/commit/87ac093867c37c0fd7d67fe9463618252d9a5bbd))

## [1.13.1](https://github.com/rak200/.github/compare/1.13.0...1.13.1) (2026-08-15)


### Bug Fixes

* the gitleaks step pins its scanner and stops failing to comment ([#40](https://github.com/rak200/.github/issues/40)) ([974e717](https://github.com/rak200/.github/commit/974e717b1b1fd120d95d3d600855bf83913ef279))

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
