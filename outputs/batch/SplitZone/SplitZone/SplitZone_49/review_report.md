# Play-Annotation-Generator Annotation Review — SplitZone_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_49`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 92
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
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 37 | START | 37 | 54 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `11` | `11` | 40 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 40 | START | 40 | 67 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `20` | `20` | 40 | START | 40 | 71 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 40 | START | 40 | 174 |
| ✅ EXACT | `Action_SplitBlock` | TE | `2` | `2` | 46 | START | 46 | 174 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `11` | `11` | 54 | END | N/A | N/A |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `20` | `20` | 72 | START | 72 | 174 |
| ✅ EXACT | `Action_BallCarry` | QB | `19` | `19` | 107 | START | 107 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 174 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 36 | 3 | inferred_complete_timeline |
| `Action_None` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_None` | 42 | 59 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 231 | 195 | inferred_complete_timeline |
| `Action_None` | 236 | 244 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SplitBlock` | 46 | 174 | 129 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 71 | 32 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 72 | 174 | 103 | inferred_complete_timeline |
| `Action_None` | 175 | 192 | 18 | inferred_complete_timeline |
| `Action_None` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 54 | 18 | inferred_complete_timeline |
| `Action_None` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_None` | 79 | 98 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 67 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 84 | 174 | 91 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 174 | 135 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 106 | 70 | inferred_complete_timeline |
| `Action_None` | 110 | 138 | 29 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 192 | 48 | inferred_complete_timeline |
| `Action_None` | 194 | 299 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 83 | 47 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 192 | 156 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 137 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 260 | 224 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 77–299 | 212 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 79–107 | 28 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 97–100 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 97–178 | 82 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 109–299 | 191 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 133–299 | 113 | 13 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 146–161 | 14 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 159–164 | 6 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 161–296 | 136 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 204–299 | 92 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 205–226 | 16 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 263–299 | 37 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (C)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 100: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 135 frames exceeds threshold 90 frames [start=40, end=174].
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=40, end=36. Clamping end to start.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_ZoneBlock' annotated_start=40, effective_Action_ZoneBlock_start=55.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [37–54], lower_priority='Action_SnapReceive' annotated_start=37, effective_Action_SnapReceive_start=55.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 135 frames exceeds threshold 90 frames [start=40, end=174].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '20' (LG) duration 103 frames exceeds threshold 90 frames [start=72, end=174].
- ⚠️ Action 'Action_None' range [37-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-106] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-137] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-260] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-76] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [71-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [84-174] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [107-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [72-174] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-59] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-93] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-138] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-178] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-245] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-288] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-217] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-299] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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