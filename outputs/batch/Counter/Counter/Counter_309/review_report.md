# Play-Annotation-Generator Annotation Review — Counter_309

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_309`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 71
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 209
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_PullBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB1 | offense | `10` | `9` |
| ✅ EXACT | `Action_Handoff` | QB1 | offense | `10` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `10` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 41 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `20` | `19` | 42 | START | 127 | 127 |
| ⚠️ START CHANGED | `Action_DownBlock` | RT | `18` | `17` | 47 | START | 55 | 91 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `20` | `19` | 47 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_PullBlock` | LG | `21` | `20` | 47 | START | 127 | 127 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `4` | `3` | 47 | START | 47 | 91 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `13` | `12` | 54 | START | 54 | 82 |
| ✅ EXACT | `Action_SnapReceive` | QB1 | `10` | `9` | 56 | END | 42 | 56 |
| ✅ EXACT | `Action_Handoff` | QB1 | `10` | `9` | 67 | START | 67 | 82 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `12` | 83 | START | 83 | 134 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 56 | 15 | inferred_complete_timeline |
| `Action_None` | 57 | 66 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_None` | 83 | 134 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 54 | 82 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 83 | 134 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_None` | 42 | 109 | 68 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 47 | 91 | 45 | inferred_complete_timeline |
| `Action_None` | 92 | 122 | 31 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 127–134
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PullBlock` | 127 | 127 | 1 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 127–134
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 127 | 127 | 1 | inferred_complete_timeline |
| `Action_None` | 128 | 134 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 75 | 34 | inferred_complete_timeline |
| `Action_None` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_None` | 95 | 100 | 6 | inferred_complete_timeline |
| `Action_None` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 126 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 55–134
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 55 | 91 | 37 | inferred_complete_timeline |
| `Action_None` | 92 | 134 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 126 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–96
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 41 | 39 | inferred_complete_timeline |
| `Action_None` | 42 | 96 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–126
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 41 | 29 | inferred_complete_timeline |
| `Action_None` | 42 | 126 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 126 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 134 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 92 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–2
- **Visible Samples:** 3

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 23 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 37 | 6 | inferred_complete_timeline |
| `Action_None` | 45 | 126 | 82 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 38–121
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 42 | 121 | 80 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 127–134 | 8 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 127–134 | 8 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 127–134 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 127–217 | 11 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 216–539 | 285 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `37` | `38` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `38` | `39` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `39` | `40` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `40` | `41` | Position_Unknown | Team_Unknown | 258–539 | 281 | 2 | Undefined position; Undefined team |
| `41` | `42` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `42` | `43` | Position_Unknown | Team_Unknown | 258–539 | 280 | 2 | Undefined position; Undefined team |
| `43` | `44` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `44` | `45` | Position_Unknown | Team_Unknown | 258–507 | 250 | 1 | Undefined position; Undefined team |
| `45` | `46` | Position_Unknown | Team_Unknown | 258–539 | 269 | 4 | Undefined position; Undefined team |
| `46` | `47` | Position_Unknown | Team_Unknown | 258–539 | 276 | 3 | Undefined position; Undefined team |
| `47` | `48` | Position_Unknown | Team_Unknown | 258–539 | 278 | 2 | Undefined position; Undefined team |
| `48` | `49` | Position_Unknown | Team_Unknown | 258–520 | 260 | 3 | Undefined position; Undefined team |
| `49` | `50` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `50` | `51` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `51` | `52` | Position_Unknown | Team_Unknown | 258–446 | 189 | 1 | Undefined position; Undefined team |
| `52` | `53` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `53` | `54` | Position_Unknown | Team_Unknown | 258–432 | 175 | 1 | Undefined position; Undefined team |
| `54` | `55` | Position_Unknown | Team_Unknown | 258–539 | 273 | 2 | Undefined position; Undefined team |
| `55` | `56` | Position_Unknown | Team_Unknown | 258–539 | 281 | 2 | Undefined position; Undefined team |
| `56` | `57` | Position_Unknown | Team_Unknown | 258–404 | 147 | 1 | Undefined position; Undefined team |
| `57` | `58` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `58` | `59` | Position_Unknown | Team_Unknown | 258–271 | 14 | 1 | Undefined position; Undefined team |
| `59` | `60` | Position_Unknown | Team_Unknown | 258–539 | 282 | 1 | Undefined position; Undefined team |
| `60` | `61` | Position_Unknown | Team_Unknown | 264–539 | 272 | 3 | Undefined position; Undefined team |
| `61` | `63` | Position_Unknown | Team_Unknown | 279–539 | 261 | 1 | Undefined position; Undefined team |
| `62` | `64` | Position_Unknown | Team_Unknown | 299–300 | 2 | 1 | Undefined position; Undefined team |
| `63` | `65` | Position_Unknown | Team_Unknown | 406–412 | 7 | 1 | Undefined position; Undefined team |
| `64` | `66` | Position_Unknown | Team_Unknown | 421–528 | 83 | 7 | Undefined position; Undefined team |
| `65` | `68` | Position_Unknown | Team_Unknown | 429–539 | 111 | 1 | Undefined position; Undefined team |
| `66` | `70` | Position_Unknown | Team_Unknown | 455–539 | 72 | 3 | Undefined position; Undefined team |
| `67` | `77` | Position_Unknown | Team_Unknown | 499–500 | 2 | 1 | Undefined position; Undefined team |
| `68` | `80` | Position_Unknown | Team_Unknown | 525–539 | 12 | 2 | Undefined position; Undefined team |
| `69` | `81` | Position_Unknown | Team_Unknown | 529–539 | 11 | 1 | Undefined position; Undefined team |
| `70` | `82` | Position_Unknown | Team_Unknown | 529–539 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (C): Annotated start 42 != Inferred start 127
- ⚠️ `Action_DownBlock` for actor_track_id `18` (RT): Annotated start 47 != Inferred start 55
- ❌ Missing segment for action `Action_DownBlock` on target `20` (C)
- ⚠️ `Action_PullBlock` for actor_track_id `21` (LG): Annotated start 47 != Inferred start 127

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 51 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 51 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 102 |
| Missing visible bounding boxes during action | 100 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 620: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '19' has invalid range: start=127, end=56. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '19' has invalid range: start=127, end=91. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [127–127], lower_priority='Action_DownBlock' annotated_start=127, effective_Action_DownBlock_start=128.
- ⚠️ Segment 'Action_PullBlock' for track '20' has invalid range: start=127, end=91. Clamping end to start.
- ⚠️ Action 'Action_None' range [42-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-134] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-35] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-109] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-134] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-27] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-37] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [83-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-539] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-509] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-431] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-507] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-474] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-494] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-443] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-501] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-539] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-407] for track '47' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-343] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-517] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-520] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-446] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-539] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-432] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-438] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-539] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-536] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-404] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-539] for track '57' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-539] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-427] for track '60' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-488] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '63' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-430] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-437] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-441] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-497] for track '64' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-509] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-528] for track '64' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-456] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-529] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-539] for track '66' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-534] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-539] for track '70' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>