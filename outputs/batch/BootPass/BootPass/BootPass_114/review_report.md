# Play-Annotation-Generator Annotation Review — BootPass_114

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_114`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 92
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 4
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE4 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `18` | `18` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_FakeHandoff` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_BootAway` | LT | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | LT | offense | `4` | `4` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `29` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE4 | `20` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 37 | START | 37 | 68 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LG | `12` | `12` | 63 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `15` | `15` | 63 | START | 63 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `18` | `18` | 63 | START | 63 | 70 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `19` | `19` | 63 | START | 69 | 88 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LT | `4` | `4` | 63 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | LT | `4` | `4` | 68 | END | 37 | 68 |
| ✅ EXACT | `Action_FakeHandoff` | LT | `4` | `4` | 78 | START | 78 | 96 |
| ✅ EXACT | `Action_BootAway` | LT | `4` | `4` | 97 | START | 97 | 114 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | LT | `4` | `4` | 145 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `29` | `25` | 194 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 46 | 103 | 58 | inferred_complete_timeline |
| `Action_None` | 110 | 299 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 154 | 118 | inferred_complete_timeline |
| `Action_None` | 156 | 249 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 118 | 82 | inferred_complete_timeline |
| `Action_None` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>TE4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 138 | 102 | inferred_complete_timeline |
| `Action_None` | 145 | 153 | 9 | inferred_complete_timeline |
| `Action_None` | 156 | 166 | 11 | inferred_complete_timeline |
| `Action_None` | 169 | 216 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_None` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_FakeHandoff` | 78 | 96 | 19 | inferred_complete_timeline |
| `Action_BootAway` | 97 | 114 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–62
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 68 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 88 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 62 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 78 | 96 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_RunBlock` | 63 | 97 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 114 | 201 | 88 | inferred_complete_timeline |
| `Action_RunBlock` | 203 | 299 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 125 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 86 | 50 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 119 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 299 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 105 | 69 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 129 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 250 | 214 | inferred_complete_timeline |
| `Action_None` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 278 | 20 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 133 | 97 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 299 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 112 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–290
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 152 | 116 | inferred_complete_timeline |
| `Action_None` | 161 | 284 | 124 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 107 | 71 | inferred_complete_timeline |
| `Action_None` | 109 | 149 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 208 | 172 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 69–118 | 47 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–133 | 43 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 104–299 | 194 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 110–112 | 3 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 159–299 | 141 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 161–299 | 134 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 164–299 | 127 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 220–299 | 80 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 239–290 | 52 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 248–294 | 47 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 255–285 | 31 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunBlock` on target `12` (LG)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `19` (C): Annotated start 63 != Inferred start 69
- ❌ Missing segment for action `Action_RunBlock` on target `4` (LT)
- ❌ Missing segment for action `Action_ThrowPass` on target `4` (LT)
- ❌ Missing segment for action `Action_SecureCatch` on target `25` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 95, Column 'Run Flat Route': Could not parse frame number from 'Drag' in entry 'Drag,21'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 208: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_RunBlock' for track '4' has invalid range: start=63, end=36. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '4' has invalid range: start=145, end=114. Clamping end to start.
- ⚠️ Segment 'Action_RunBlock' for track '12' has invalid range: start=63, end=62. Clamping end to start.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [37–68], lower_priority='Action_RunBlock' annotated_start=63, effective_Action_RunBlock_start=69.
- ⚠️ Segment 'Action_SecureCatch' for track '25' has invalid range: start=194, end=112. Clamping end to start.
- ⚠️ Action 'Action_None' range [37-112] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-149] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-125] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-152] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-284] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [97-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-154] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-249] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-250] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-278] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-105] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-299] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-97] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [114-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [203-299] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [63-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [78-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-88] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-138] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-103] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-235] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-279] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-225] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-290] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-294] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-285] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>