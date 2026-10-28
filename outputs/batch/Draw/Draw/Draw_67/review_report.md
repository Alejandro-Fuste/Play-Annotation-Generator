# Play-Annotation-Generator Annotation Review — Draw_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_67`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `16` | 26 | START | 26 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `16` | 29 | START | 41 | 51 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 40 | END | 26 | 40 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `14` | `13` | 48 | START | 48 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 78 | START | 78 | 105 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 141 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 47 | 7 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 48 | 77 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 105 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–130
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 74 | 49 | inferred_complete_timeline |
| `Action_None` | 80 | 99 | 20 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_None` | 125 | 130 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 187 | 162 | inferred_complete_timeline |
| `Action_None` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_None` | 204 | 211 | 8 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 213 | 188 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 106 | 81 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 35 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 70 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 105 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 151 | 126 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 204 | 16 | inferred_complete_timeline |
| `Action_None` | 208 | 218 | 11 | inferred_complete_timeline |
| `Action_None` | 221 | 222 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 197 | 172 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 106 | 81 | inferred_complete_timeline |
| `Action_None` | 110 | 120 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 142 | 19 | inferred_complete_timeline |
| `Action_None` | 144 | 153 | 10 | inferred_complete_timeline |
| `Action_None` | 155 | 157 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 225 | 200 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 232 | 234 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 239 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 78 | 53 | inferred_complete_timeline |
| `Action_None` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 112 | 133 | 22 | inferred_complete_timeline |
| `Action_None` | 139 | 157 | 19 | inferred_complete_timeline |
| `Action_None` | 174 | 213 | 40 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 110 | 85 | inferred_complete_timeline |
| `Action_None` | 113 | 239 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 173 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–163 | 164 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–239 | 235 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 39–48 | 10 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 39–115 | 38 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 39–211 | 160 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 39–97 | 54 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 60–211 | 58 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 115–132 | 18 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 126–205 | 54 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 129–218 | 69 | 8 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 138–239 | 77 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 140–148 | 6 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 146–219 | 42 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 147–239 | 90 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 163–239 | 69 | 5 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 183–216 | 13 | 3 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 183–234 | 40 | 3 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 218–234 | 17 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 222–239 | 16 | 2 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 232–239 | 7 | 2 | Undefined position; Undefined team |
| `37` | `41` | Position_Unknown | Team_Unknown | 232–239 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 134: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 134: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [26–40], lower_priority='Action_PassBlock' annotated_start=29, effective_Action_PassBlock_start=41.
- ⚠️ Action 'Action_None' range [26-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-197] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-110] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-142] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-151] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-213] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [78-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [162-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-110] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-157] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-213] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [32-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [38-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-70] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-105] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-99] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-211] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-81] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-93] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-142] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-211] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-239] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-201] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-229] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-234] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-239] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>