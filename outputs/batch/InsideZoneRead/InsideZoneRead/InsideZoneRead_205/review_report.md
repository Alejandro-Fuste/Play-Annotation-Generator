# Play-Annotation-Generator Annotation Review — InsideZoneRead_205

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_205`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 8
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 32
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `19` | `17` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `19` | `17` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 165 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `19` | `17` | 460 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `1` | `0` | 463 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `12` | `11` | 463 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `16` | `15` | 463 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `6` | `5` | 463 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Position_Unknown | `19` | `17` | 479 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | Position_Unknown | `19` | `17` | 484 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `19` | `17` | 514 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 543 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 182 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 89 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 104 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 32 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 70 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 153 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 168 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 182 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 239 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 121 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 239 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 178 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 226 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 183 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 226 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 194 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–8 | 9 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–194 | 161 | 7 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 81–239 | 154 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 104–239 | 119 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 128–237 | 107 | 3 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 130–169 | 40 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 156–213 | 49 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 180–239 | 60 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 189–239 | 6 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 199–239 | 41 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 216–227 | 12 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `19` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `1` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `16` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `6` (RT)
- ❌ Missing segment for action `Action_SnapReceive` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_ReadDefender` on target `17` (Position_Unknown)
- ❌ Missing segment for action `Action_BallCarry` on target `17` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 9 |
| Other | 11 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 410: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '0' has invalid range: start=463, end=123. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '5' has invalid range: start=463, end=126. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=463, end=182. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '15' has invalid range: start=463, end=70. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=460, end=239. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=460, end=239. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '17' has invalid range: start=484, end=239. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=514, end=239. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-194] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-226] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-182] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-183] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-67] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-184] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-32] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-162] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-214] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-223] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-233] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-227] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Action event 'Action_BallSnap' has invalid start frame 460. Video range is [0, 239].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 463. Video range is [0, 239].
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 479. Video range is [0, 239].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 484. Video range is [0, 239].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 514. Video range is [0, 239].
- ⚠️ Action event 'Action_None' has invalid start frame 543. Video range is [0, 239].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_205'; source metadata written as null.

</details>