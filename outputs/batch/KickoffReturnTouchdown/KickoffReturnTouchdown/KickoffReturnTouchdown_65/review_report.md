# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_65`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 79
- **Ball Tracks:** 0
- **Action Segments:** 301
- **Validation Warnings:** 406
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 286
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `42` | `35` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `42` | `35` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `42` | `35` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `0` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `11` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `12` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `13` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `14` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `2` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 23 | START | 23 | 100 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 101 | START | 101 | 105 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `42` | `35` | 205 | START | 205 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `42` | `35` | 239 | START | 241 | 300 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `42` | `35` | 616 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_KickApproach` | 23 | 100 | 78 | inferred_complete_timeline |
| `Action_KickBall` | 101 | 105 | 5 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 169 | 42 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 78 | 56 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 102 | 8 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 78 | 56 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–108
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 72 | 50 | inferred_complete_timeline |
| `Action_None` | 74 | 85 | 12 | inferred_complete_timeline |
| `Action_None` | 91 | 103 | 13 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 71 | 49 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 91 | 3 | inferred_complete_timeline |
| `Action_None` | 96 | 105 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–592
- **Visible Samples:** 562

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 147 | 125 | inferred_complete_timeline |
| `Action_None` | 149 | 167 | 19 | inferred_complete_timeline |
| `Action_None` | 171 | 192 | 22 | inferred_complete_timeline |
| `Action_None` | 197 | 217 | 21 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 540 | 303 | inferred_complete_timeline |
| `Action_None` | 545 | 552 | 8 | inferred_complete_timeline |
| `Action_None` | 554 | 592 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 76 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 144 | 122 | inferred_complete_timeline |
| `Action_None` | 150 | 152 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 242 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 194 | 172 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–445
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 237 | 215 | inferred_complete_timeline |
| `Action_None` | 261 | 278 | 18 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |
| `Action_None` | 296 | 445 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 525 | 503 | inferred_complete_timeline |
| `Action_None` | 533 | 539 | 7 | inferred_complete_timeline |
| `Action_None` | 545 | 617 | 73 | inferred_complete_timeline |
| `Action_None` | 619 | 629 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 157 | 135 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 235 | 45 | inferred_complete_timeline |
| `Action_None` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_None` | 249 | 349 | 101 | inferred_complete_timeline |
| `Action_None` | 356 | 397 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 154 | 132 | inferred_complete_timeline |
| `Action_None` | 156 | 160 | 5 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 192 | 213 | 22 | inferred_complete_timeline |
| `Action_None` | 219 | 224 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 160 | 138 | inferred_complete_timeline |
| `Action_None` | 163 | 246 | 84 | inferred_complete_timeline |
| `Action_None` | 318 | 323 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 112 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 130 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_None` | 23 | 224 | 202 | inferred_complete_timeline |
| `Action_None` | 230 | 244 | 15 | inferred_complete_timeline |
| `Action_None` | 246 | 249 | 4 | inferred_complete_timeline |
| `Action_None` | 291 | 294 | 4 | inferred_complete_timeline |
| `Action_None` | 296 | 308 | 13 | inferred_complete_timeline |
| `Action_None` | 312 | 347 | 36 | inferred_complete_timeline |
| `Action_None` | 358 | 478 | 121 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 93–629 | 445 | 6 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 98–106 | 8 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 113–596 | 444 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 117–629 | 497 | 8 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 132–144 | 7 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 143–400 | 246 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 145–313 | 91 | 9 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 145–629 | 479 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 160–465 | 297 | 6 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 161–285 | 120 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 163–251 | 72 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 172–629 | 377 | 6 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 188–267 | 76 | 3 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 188–552 | 342 | 10 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 194–456 | 260 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 209–213 | 5 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 231–237 | 6 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 236–629 | 391 | 3 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 236–355 | 111 | 5 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 292–629 | 314 | 6 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 298–300 | 3 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 304–488 | 154 | 7 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 305–314 | 10 | 1 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 311–628 | 215 | 15 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 316–361 | 41 | 2 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 330–625 | 252 | 8 | Undefined position; Undefined team |
| `48` | `66` | Position_Unknown | Team_Unknown | 333–583 | 221 | 6 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 355–629 | 246 | 9 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 383–385 | 3 | 1 | Undefined position; Undefined team |
| `51` | `72` | Position_Unknown | Team_Unknown | 389–607 | 196 | 5 | Undefined position; Undefined team |
| `52` | `75` | Position_Unknown | Team_Unknown | 426–523 | 41 | 3 | Undefined position; Undefined team |
| `53` | `79` | Position_Unknown | Team_Unknown | 447–529 | 59 | 8 | Undefined position; Undefined team |
| `54` | `80` | Position_Unknown | Team_Unknown | 461–625 | 149 | 7 | Undefined position; Undefined team |
| `55` | `81` | Position_Unknown | Team_Unknown | 462–463 | 2 | 1 | Undefined position; Undefined team |
| `56` | `82` | Position_Unknown | Team_Unknown | 475–490 | 8 | 3 | Undefined position; Undefined team |
| `57` | `83` | Position_Unknown | Team_Unknown | 477–544 | 68 | 1 | Undefined position; Undefined team |
| `58` | `84` | Position_Unknown | Team_Unknown | 489–493 | 5 | 1 | Undefined position; Undefined team |
| `59` | `85` | Position_Unknown | Team_Unknown | 496–499 | 4 | 1 | Undefined position; Undefined team |
| `60` | `88` | Position_Unknown | Team_Unknown | 499–502 | 4 | 1 | Undefined position; Undefined team |
| `61` | `89` | Position_Unknown | Team_Unknown | 499–542 | 18 | 4 | Undefined position; Undefined team |
| `62` | `95` | Position_Unknown | Team_Unknown | 518–617 | 72 | 4 | Undefined position; Undefined team |
| `63` | `96` | Position_Unknown | Team_Unknown | 519–530 | 10 | 2 | Undefined position; Undefined team |
| `64` | `100` | Position_Unknown | Team_Unknown | 525–528 | 4 | 1 | Undefined position; Undefined team |
| `65` | `102` | Position_Unknown | Team_Unknown | 531–534 | 4 | 1 | Undefined position; Undefined team |
| `66` | `104` | Position_Unknown | Team_Unknown | 540–543 | 4 | 1 | Undefined position; Undefined team |
| `67` | `105` | Position_Unknown | Team_Unknown | 542–549 | 4 | 2 | Undefined position; Undefined team |
| `68` | `106` | Position_Unknown | Team_Unknown | 542–547 | 5 | 2 | Undefined position; Undefined team |
| `69` | `111` | Position_Unknown | Team_Unknown | 550–551 | 2 | 1 | Undefined position; Undefined team |
| `70` | `113` | Position_Unknown | Team_Unknown | 554–629 | 74 | 2 | Undefined position; Undefined team |
| `71` | `115` | Position_Unknown | Team_Unknown | 559–567 | 9 | 1 | Undefined position; Undefined team |
| `72` | `116` | Position_Unknown | Team_Unknown | 565–569 | 5 | 1 | Undefined position; Undefined team |
| `73` | `117` | Position_Unknown | Team_Unknown | 569–570 | 2 | 1 | Undefined position; Undefined team |
| `74` | `121` | Position_Unknown | Team_Unknown | 596–629 | 34 | 1 | Undefined position; Undefined team |
| `75` | `122` | Position_Unknown | Team_Unknown | 612–615 | 4 | 1 | Undefined position; Undefined team |
| `76` | `123` | Position_Unknown | Team_Unknown | 612–617 | 6 | 1 | Undefined position; Undefined team |
| `77` | `124` | Position_Unknown | Team_Unknown | 615–617 | 3 | 1 | Undefined position; Undefined team |
| `78` | `125` | Position_Unknown | Team_Unknown | 618–619 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `42` (7 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `42` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 63 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 63 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 126 |
| Missing visible bounding boxes during action | 278 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '35' has invalid range: start=616, end=552. Clamping end to start.
- ⚠️ Action 'Action_None' range [23-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-278] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-445] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-525] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-539] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-617] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-71] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-105] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-112] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-130] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-224] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-308] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-347] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-478] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-157] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-349] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-397] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-213] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-224] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-160] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-246] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-323] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-147] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-192] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-217] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-540] for track '10' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-552] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-592] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-85] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-144] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-102] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-143] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-249] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-409] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-442] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-498] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-589] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-596] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-237] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-278] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-306] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-343] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-282] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-320] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-394] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-159] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-228] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-283] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-417] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-437] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-479] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-629] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-172] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-294] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-323] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-452] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-465] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-241] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-285] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-283] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-472] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-487] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-500] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-231] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-267] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-204] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [205-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-238] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [241-300] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [304-314] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-353] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [355-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [383-489] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [498-500] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [502-552] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-451] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-245] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-465] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-629] for track '39' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-288] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-294] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-312] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-347] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-467] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-473] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-476] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-559] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-629] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-315] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-410] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-446] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-471] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-488] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-314] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-347] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-467] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-510] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-520] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-553] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-575] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-611] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-619] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-354] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-405] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-417] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-491] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-500] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-509] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-625] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-361] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-487] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-534] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-562] for track '48' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-573] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-583] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-489] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-498] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-507] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-523] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-530] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-542] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-611] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-617] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-629] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-478] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-589] for track '51' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-607] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-429] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-463] for track '52' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-523] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-450] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-485] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-508] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-522] for track '53' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-529] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-552] for track '54' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-574] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-607] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [614-620] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-477] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-483] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-544] for track '57' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-493] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-515] for track '61' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-542] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-522] for track '62' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-529] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-617] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-530] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-528] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-543] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-549] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-544] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '69' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-557] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-629] for track '70' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-567] for track '71' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-569] for track '72' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-570] for track '73' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-615] for track '75' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-617] for track '76' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-617] for track '77' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '78' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '69' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '69' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '70' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '70' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '71' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '71' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '72' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '72' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '73' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '73' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '74' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '74' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '75' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '75' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '76' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '76' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '77' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '77' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '78' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '78' has undefined team_side. Will map to Team_Unknown.

</details>