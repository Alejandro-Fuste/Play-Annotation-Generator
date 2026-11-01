# Play-Annotation-Generator Annotation Review — InsideZoneRead_202

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_202`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 143
- **Validation Warnings:** 150
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 118
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 3 | START | 3 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 3 | START | 3 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 3 | START | 3 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 3 | START | 3 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 3 | START | 3 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 3 | START | 3 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 3 | START | 3 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 3 | START | 3 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 3 | START | 3 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 3 | START | 3 | 25 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 26 | START | 26 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 29 | START | 29 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 29 | START | 40 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `19` | `18` | 29 | START | 29 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 29 | START | 29 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `22` | `21` | 29 | START | 29 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 39 | END | 26 | 39 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `16` | 43 | START | 43 | 55 |
| ✅ EXACT | `Action_BallCarry` | QB | `17` | `16` | 56 | START | 56 | 273 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–273
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 273 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 3–157
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 89 | 64 | inferred_complete_timeline |
| `Action_None` | 93 | 128 | 36 | inferred_complete_timeline |
| `Action_None` | 135 | 150 | 16 | inferred_complete_timeline |
| `Action_None` | 152 | 157 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–252
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 188 | 163 | inferred_complete_timeline |
| `Action_None` | 190 | 252 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 299 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 299 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 3–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 28 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 64 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 74 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 128 | 52 | inferred_complete_timeline |
| `Action_None` | 129 | 254 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–49
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 28 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 49 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 69 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 82 | 128 | 47 | inferred_complete_timeline |
| `Action_None` | 129 | 299 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 28 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 299 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 28 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 128 | 100 | inferred_complete_timeline |
| `Action_None` | 129 | 141 | 13 | inferred_complete_timeline |
| `Action_None` | 146 | 173 | 28 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 291 | 266 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 3–109
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 58 | 33 | inferred_complete_timeline |
| `Action_None` | 73 | 99 | 27 | inferred_complete_timeline |
| `Action_None` | 103 | 109 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 299 | 274 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–161
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 113 | 88 | inferred_complete_timeline |
| `Action_None` | 115 | 122 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 137 | 12 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 119 | 94 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 52 | 27 | inferred_complete_timeline |
| `Action_None` | 54 | 77 | 24 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–128
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 120 | 95 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 199 | 174 | inferred_complete_timeline |
| `Action_None` | 201 | 271 | 71 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 3–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 227 | 202 | inferred_complete_timeline |
| `Action_None` | 229 | 299 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–284
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 146 | 121 | inferred_complete_timeline |
| `Action_None` | 151 | 193 | 43 | inferred_complete_timeline |
| `Action_None` | 197 | 276 | 80 | inferred_complete_timeline |
| `Action_None` | 278 | 284 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 25 | 23 | inferred_complete_timeline |
| `Action_None` | 26 | 150 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 3–299 | 297 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 32–97 | 33 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 69–299 | 231 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 124–185 | 43 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 126–195 | 10 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 128–272 | 119 | 7 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 136–299 | 164 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 138–283 | 121 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 141–151 | 10 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 159–261 | 103 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 174–285 | 62 | 10 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 177–178 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 182–299 | 117 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 186–282 | 45 | 6 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 211–295 | 59 | 8 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 218–299 | 82 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 260–299 | 27 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 261–285 | 18 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 270–299 | 21 | 3 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 294–299 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 404: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [26–39], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=40.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 100 frames exceeds threshold 90 frames [start=29, end=128].
- ⚠️ Action 'Action_None' range [26-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-252] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-120] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-119] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-291] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-58] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-99] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-113] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-89] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-150] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-254] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-69] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [82-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-52] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-77] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-299] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-273] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-271] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-227] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-39] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-62] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-154] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-261] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-261] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-247] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-285] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-212] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-282] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-274] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-295] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>