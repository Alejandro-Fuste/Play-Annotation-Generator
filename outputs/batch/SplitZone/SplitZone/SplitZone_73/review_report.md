# Play-Annotation-Generator Annotation Review — SplitZone_73

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_73`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 47
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 11 | START | 12 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 11 | START | 12 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 11 | START | 12 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 11 | START | 12 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 11 | START | 12 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 11 | START | 12 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 11 | START | 12 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 11 | START | 12 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 11 | START | 12 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 11 | START | 12 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 11 | START | 12 | 155 |
| ✅ EXACT | `Action_BallSnap` | C | `2` | `2` | 124 | START | 124 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `11` | 129 | START | 129 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `19` | 129 | START | 129 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `2` | `2` | 129 | START | 142 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 129 | START | 129 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 129 | START | 129 | 161 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `1` | `1` | 130 | START | 130 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 141 | END | 124 | 141 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 144 | START | 144 | 155 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `7` | `7` | 156 | START | 158 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 226 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–248
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_SnapReceive` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 248 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 155 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 158 | 299 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 12–207
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 207 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 175 | 52 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 299 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 12–258
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 129 | 118 | inferred_complete_timeline |
| `Action_SplitBlock` | 130 | 226 | 97 | inferred_complete_timeline |
| `Action_None` | 227 | 258 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 128 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 161 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 226 | 64 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 128 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 156 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 226 | 67 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 124 | 141 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 192 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 226 | 19 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 12–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 128 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 219 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 226 | 6 | inferred_complete_timeline |
| `Action_None` | 227 | 234 | 8 | inferred_complete_timeline |
| `Action_None` | 236 | 299 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–290
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 128 | 117 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 226 | 98 | inferred_complete_timeline |
| `Action_None` | 227 | 290 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 215 | 92 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 12–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 219 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 290 | 167 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 12–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 299 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–285
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 123 | 112 | inferred_complete_timeline |
| `Action_None` | 124 | 285 | 162 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `28` | Position_Unknown | Team_Unknown | 196–199 | 4 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 233–236 | 4 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 249–250 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 256–257 | 2 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 275–282 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `7` (RB): Annotated start 156 != Inferred start 158

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 30 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (C) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [124–141], lower_priority='Action_ZoneBlock' annotated_start=129, effective_Action_ZoneBlock_start=142.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
- ⚠️ Action 'Action_None' range [227-258] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-192] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-196] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [198-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-299] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-215] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-290] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-226] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-290] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-219] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-175] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-156] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-282] for track '26' has 1 frames without a visible bounding box.
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