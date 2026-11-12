# Play-Annotation-Generator Annotation Review — SplitZone_157

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_157`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 76
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 12 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 12 | START | 13 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 12 | START | 13 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 12 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 12 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 12 | START | 13 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 12 | START | 13 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 12 | START | 13 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 12 | START | 13 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 12 | START | 13 | 79 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 77 | START | 77 | 88 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `15` | `15` | 80 | START | 80 | 203 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `17` | 80 | START | 89 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 80 | START | 80 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 80 | START | 80 | 203 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 80 | START | 80 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `7` | `7` | 85 | START | 85 | 153 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 88 | END | 77 | 88 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 93 | START | 93 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `17` | `17` | 98 | START | 98 | 115 |
| ✅ EXACT | `Action_BallCarry` | RB | `11` | `11` | 113 | START | 113 | 317 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 203 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–330
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 93 | 112 | 20 | inferred_complete_timeline |
| `Action_None` | 113 | 330 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 13–317
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 112 | 100 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 317 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–197
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 84 | 72 | inferred_complete_timeline |
| `Action_SplitBlock` | 85 | 153 | 69 | inferred_complete_timeline |
| `Action_SplitBlock` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_SplitBlock` | 178 | 197 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–344
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 151 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 203 | 40 | inferred_complete_timeline |
| `Action_None` | 204 | 344 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 203 | 124 | inferred_complete_timeline |
| `Action_None` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 13–145
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 88 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 98 | 115 | 18 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 121 | 145 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 203 | 124 | inferred_complete_timeline |
| `Action_None` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 79 | 67 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 203 | 124 | inferred_complete_timeline |
| `Action_None` | 204 | 359 | 156 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 141 | 65 | inferred_complete_timeline |
| `Action_None` | 144 | 359 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 248 | 172 | inferred_complete_timeline |
| `Action_None` | 250 | 359 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–134
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 134 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–108
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 108 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–359
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 281 | 205 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–356
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 356 | 280 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–227
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 139 | 63 | inferred_complete_timeline |
| `Action_None` | 143 | 154 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_None` | 173 | 219 | 47 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 13–183
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 183 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–266
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 76 | 64 | inferred_complete_timeline |
| `Action_None` | 77 | 266 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 13–359 | 347 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 107–112 | 6 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 116–359 | 244 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 148–359 | 212 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 167–359 | 193 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 181–359 | 159 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 183–359 | 177 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 226–359 | 132 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 272–274 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 273–359 | 86 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 296–297 | 2 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 321–358 | 38 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 334–352 | 9 | 2 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 80 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 316: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_ZoneBlock' annotated_start=80, effective_Action_ZoneBlock_start=89.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 124 frames exceeds threshold 90 frames [start=80, end=203].
- ⚠️ Action 'Action_None' range [77-248] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-141] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-134] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [85-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [157-158] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [161-168] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [178-197] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-219] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-356] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-281] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [98-115] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [121-145] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-330] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-344] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-359] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-359] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-358] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-340] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>