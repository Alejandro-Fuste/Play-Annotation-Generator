# Play-Annotation-Generator Annotation Review — SplitZone_229

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_229`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 169
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `19` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | defense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 15 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 60 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 66 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 79 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 120 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 121 | START | 121 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 124 | START | 126 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 124 | START | 124 | 138 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `19` | `16` | 124 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 125 | END | 121 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LB1 | `9` | `9` | 139 | START | 139 | 161 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `13` | 155 | START | 155 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `4` | 162 | START | 162 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 227 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 15–166
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 17 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 120 | 52 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_None` | 126 | 154 | 29 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 161 | 7 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 182 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 215 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 221 | 235 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 240 | 299 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 283 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 60–299
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 60 | 88 | 29 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 150 | 5 | inferred_complete_timeline |
| `Action_None` | 154 | 171 | 18 | inferred_complete_timeline |
| `Action_None` | 174 | 193 | 20 | inferred_complete_timeline |
| `Action_None` | 196 | 248 | 53 | inferred_complete_timeline |
| `Action_None` | 252 | 288 | 37 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 169 | 49 | inferred_complete_timeline |
| `Action_None` | 174 | 182 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 66–299
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 66 | 123 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 217 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_None` | 228 | 278 | 51 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 125 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 163 | 169 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 196 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 79–83
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 79 | 83 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 238 | 118 | inferred_complete_timeline |
| `Action_None` | 240 | 244 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_SplitBlock` | 139 | 161 | 23 | inferred_complete_timeline |
| `Action_SplitBlock` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 180 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 182 | 190 | 9 | inferred_complete_timeline |
| `Action_SplitBlock` | 202 | 215 | 14 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–168
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 91 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 120 | 1 | inferred_complete_timeline |
| `Action_None` | 121 | 124 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 292 | 172 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_None` | 121 | 215 | 95 | inferred_complete_timeline |
| `Action_None` | 217 | 220 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 237 | 9 | inferred_complete_timeline |
| `Action_None` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–170 | 161 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 152–298 | 111 | 6 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 163–292 | 52 | 4 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 164–169 | 6 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 164–210 | 11 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 164–281 | 65 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 168–296 | 129 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 168–171 | 4 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 185–247 | 38 | 5 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 187–189 | 3 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 201–240 | 38 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 202–299 | 86 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 222–225 | 4 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 228–255 | 21 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 239–243 | 5 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 241–299 | 47 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 244–269 | 20 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 248–250 | 3 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 253–299 | 47 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 267–299 | 22 | 3 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 267–299 | 32 | 2 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 268–276 | 9 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 289–291 | 3 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (8 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (RG)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 104 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 460: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [121–125], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=126.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LT) duration 104 frames exceeds threshold 90 frames [start=124, end=227].
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=124, end=83. Clamping end to start.
- ⚠️ Action 'Action_None' range [121-149] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-292] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-182] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [187-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-215] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [221-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-283] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [139-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [165-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [182-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [202-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-238] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [126-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [136-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [163-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-176] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [181-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [193-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-7] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-91] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-88] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-248] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-138] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [201-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-278] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-214] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-253] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-211] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-247] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-235] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-255] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-250] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-283] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-294] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-271] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-283] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-276] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-299] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>