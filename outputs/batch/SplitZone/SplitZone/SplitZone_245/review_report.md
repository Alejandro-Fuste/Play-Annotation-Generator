# Play-Annotation-Generator Annotation Review — SplitZone_245

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_245`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 4 | START | 5 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `1` | `Group` | 4 | START | 5 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 4 | START | 5 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 4 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 4 | START | 5 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 4 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 4 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `2` | `Group` | 4 | START | 5 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 4 | START | 5 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 4 | START | 5 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 4 | START | 5 | 64 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `12` | `12` | 62 | START | 62 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 65 | START | 65 | 184 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `17` | 65 | START | 65 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 65 | START | 65 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | C | `2` | `2` | 65 | START | 65 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 65 | START | 65 | 184 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `1` | `1` | 74 | START | 74 | 184 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 78 | END | 62 | 78 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `5` | 86 | START | 86 | 97 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `15` | `15` | 98 | START | 103 | 248 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 184 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–248
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 96 | 92 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 248 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 5–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 202 | 141 | inferred_complete_timeline |
| `Action_None` | 206 | 254 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–170
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 170 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 73 | 69 | inferred_complete_timeline |
| `Action_SplitBlock` | 74 | 184 | 111 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 93 | 32 | inferred_complete_timeline |
| `Action_None` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 133 | 13 | inferred_complete_timeline |
| `Action_None` | 170 | 269 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–263
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 184 | 120 | inferred_complete_timeline |
| `Action_None` | 185 | 221 | 37 | inferred_complete_timeline |
| `Action_None` | 228 | 263 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 184 | 120 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 5–142
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 142 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 85 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 110 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 184 | 51 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 269 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 64 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 184 | 120 | inferred_complete_timeline |
| `Action_None` | 185 | 269 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 153 | 92 | inferred_complete_timeline |
| `Action_None` | 194 | 235 | 42 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–172
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 127 | 66 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 172 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 232 | 171 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 5–116
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 107 | 46 | inferred_complete_timeline |
| `Action_None` | 110 | 116 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 5–155
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 62 | 78 | 17 | inferred_complete_timeline |
| `Action_None` | 79 | 155 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 208 | 147 | inferred_complete_timeline |
| `Action_None` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–261
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 137 | 76 | inferred_complete_timeline |
| `Action_None` | 146 | 247 | 102 | inferred_complete_timeline |
| `Action_None` | 256 | 261 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 269 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 61 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 210 | 149 | inferred_complete_timeline |
| `Action_None` | 213 | 215 | 3 | inferred_complete_timeline |
| `Action_None` | 217 | 228 | 12 | inferred_complete_timeline |
| `Action_None` | 232 | 269 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 116–253 | 122 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 138–269 | 131 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 165–168 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 244–261 | 16 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `15` (RB): Annotated start 98 != Inferred start 103

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 47 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 120 frames exceeds threshold 90 frames [start=65, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (LG) duration 120 frames exceeds threshold 90 frames [start=65, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 120 frames exceeds threshold 90 frames [start=65, end=184].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 120 frames exceeds threshold 90 frames [start=65, end=184].
- ⚠️ Action 'Action_None' range [62-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-247] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-170] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-127] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-232] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-263] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-93] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-133] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-155] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-110] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 185, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [185-187] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-107] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-131] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-253] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-164] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-269] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '28' has 1 frames without a visible bounding box.
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

</details>