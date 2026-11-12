# Play-Annotation-Generator Annotation Review — SplitZone_304

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_304`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 124
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 25
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `6` | `6` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `29` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 100 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 101 | START | 101 | 114 |
| ✅ EXACT | `Action_SplitBlock` | TE | `5` | `5` | 109 | START | 109 | 147 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 113 | START | 113 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `17` | 113 | START | 115 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 113 | START | 113 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 113 | START | 113 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `21` | 113 | START | 113 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 114 | END | 101 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `6` | `6` | 115 | START | 115 | 136 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `12` | `12` | 116 | START | 116 | 126 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 127 | START | 127 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `12` | `12` | 143 | START | 143 | 177 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `29` | `26` | 144 | START | 144 | 157 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_SnapReceive` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_None` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 116 | 126 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 127 | 141 | 15 | inferred_complete_timeline |
| `Action_None` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 143 | 177 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 179 | 389 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PressEdge` | 115 | 136 | 22 | inferred_complete_timeline |
| `Action_PressEdge` | 142 | 176 | 35 | inferred_complete_timeline |
| `Action_None` | 177 | 361 | 185 | inferred_complete_timeline |
| `Action_None` | 367 | 368 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–338
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 166 | 66 | inferred_complete_timeline |
| `Action_None` | 168 | 292 | 125 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |
| `Action_None` | 302 | 329 | 28 | inferred_complete_timeline |
| `Action_None` | 333 | 338 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 216 | 116 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_None` | 221 | 389 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_SplitBlock` | 109 | 147 | 39 | inferred_complete_timeline |
| `Action_None` | 148 | 317 | 170 | inferred_complete_timeline |
| `Action_None` | 319 | 326 | 8 | inferred_complete_timeline |
| `Action_None` | 328 | 335 | 8 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 389 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–135
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 135 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 152 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 158 | 161 | 4 | inferred_complete_timeline |
| `Action_None` | 162 | 389 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_BallSnap` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 115 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 139 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 161 | 21 | inferred_complete_timeline |
| `Action_None` | 162 | 170 | 9 | inferred_complete_timeline |
| `Action_None` | 191 | 389 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 143 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 166 | 66 | inferred_complete_timeline |
| `Action_None` | 173 | 389 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 317 | 217 | inferred_complete_timeline |
| `Action_None` | 319 | 322 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 137 | 37 | inferred_complete_timeline |
| `Action_None` | 140 | 300 | 161 | inferred_complete_timeline |
| `Action_None` | 303 | 389 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 231 | 131 | inferred_complete_timeline |
| `Action_None` | 233 | 273 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 377 | 277 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 389 | 289 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 248 | 148 | inferred_complete_timeline |
| `Action_None` | 254 | 384 | 131 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_None` | 101 | 184 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 10–20 | 8 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 11–45 | 23 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 23–43 | 13 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 112–389 | 256 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 144–178 | 30 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 153–389 | 237 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 187–389 | 203 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 191–389 | 198 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 207–389 | 137 | 8 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 234–243 | 10 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 248–250 | 3 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 263–269 | 7 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 284–389 | 106 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 312–346 | 16 | 4 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 330–333 | 4 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 341–347 | 7 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 358–389 | 32 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 360–370 | 9 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 381–389 | 7 | 2 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 381–389 | 9 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 389–389 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [101–114], lower_priority='Action_ZoneBlock' annotated_start=113, effective_Action_ZoneBlock_start=115.
- ⚠️ Action 'Action_None' range [101-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-216] for track '2' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-300] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-389] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-317] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-335] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [115-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-361] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-166] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-389] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-292] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-338] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [143-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-317] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-377] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-384] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [101-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '17' starts at frame 115, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [115-115] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-231] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-273] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-152] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [154-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-118] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-139] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [113-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-27] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-45] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-32] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-43] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-125] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-389] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '26' starts at frame 158, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [158-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-178] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-231] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-243] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-314] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-337] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-346] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-347] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-366] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-383] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-389] for track '43' has 3 frames without a visible bounding box.
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

</details>