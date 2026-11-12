# Play-Annotation-Generator Annotation Review — SplitZone_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_117`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 40
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 20 | START | 21 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 20 | START | 21 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 20 | START | 21 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 20 | START | 21 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 20 | START | 21 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 20 | START | 21 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 20 | START | 21 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 20 | START | 21 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 20 | START | 21 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 20 | START | 21 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 20 | START | 21 | 128 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 126 | START | 126 | 143 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `5` | `5` | 129 | START | 129 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 129 | START | 144 | 158 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 129 | START | 129 | 239 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 129 | START | 129 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 129 | START | 129 | 206 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 129 | START | 129 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 143 | END | 126 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `18` | 153 | START | 153 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `12` | 164 | START | 164 | 306 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 239 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 21–324
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_None` | 144 | 152 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 153 | 163 | 11 | inferred_complete_timeline |
| `Action_None` | 164 | 324 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 21–323
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 163 | 143 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 306 | 143 | inferred_complete_timeline |
| `Action_BallCarry` | 308 | 323 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 128 | 108 | inferred_complete_timeline |
| `Action_SplitBlock` | 129 | 239 | 111 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 292 | 167 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 290 | 165 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 21–184
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 128 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 184 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 128 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 206 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 209 | 239 | 31 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_BallSnap` | 126 | 143 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 158 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 239 | 75 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 128 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 239 | 111 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 128 | 108 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 239 | 111 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–158
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 150 | 25 | inferred_complete_timeline |
| `Action_None` | 153 | 158 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 221 | 96 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 184 | 59 | inferred_complete_timeline |
| `Action_None` | 186 | 329 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 21–308
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 308 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 202 | 77 | inferred_complete_timeline |
| `Action_None` | 204 | 329 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 329 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 21–329
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_None` | 126 | 284 | 159 | inferred_complete_timeline |
| `Action_None` | 286 | 329 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 25–29 | 5 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 202–329 | 127 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 227–329 | 97 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 302–329 | 22 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 24 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [126–143], lower_priority='Action_ZoneBlock' annotated_start=129, effective_Action_ZoneBlock_start=144.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
- ⚠️ Action 'Action_None' range [126-290] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-308] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-184] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-306] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-323] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-324] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [209-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-29] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-253] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-323] for track '26' has 2 frames without a visible bounding box.
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

</details>