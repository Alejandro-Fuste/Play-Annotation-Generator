# Play-Annotation-Generator Annotation Review — JetSweep_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_117`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 83
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 4
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | LG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 127 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `20` | `19` | 123 | START | 123 | 142 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `17` | `16` | 126 | START | N/A | N/A |
| ✅ EXACT | `Action_LeadBlock` | RB | `3` | `2` | 128 | START | 128 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 128 | START | 128 | 178 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `11` | `10` | 128 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `17` | `16` | 128 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `7` | 128 | START | 128 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 128 | START | 128 | 178 |
| ✅ EXACT | `Action_SnapReceive` | LG | `11` | `10` | 139 | END | 126 | 139 |
| ✅ EXACT | `Action_Toss` | LG | `11` | `10` | 141 | START | 141 | 151 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `20` | `19` | 152 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 178 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_LeadBlock` | 128 | 178 | 51 | inferred_complete_timeline |
| `Action_None` | 179 | 213 | 35 | inferred_complete_timeline |
| `Action_None` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 168 | 43 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 161 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 178 | 51 | inferred_complete_timeline |
| `Action_None` | 179 | 188 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_SnapReceive` | 126 | 139 | 14 | inferred_complete_timeline |
| `Action_None` | 140 | 140 | 1 | inferred_complete_timeline |
| `Action_Toss` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_None` | 152 | 190 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–34
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 178 | 51 | inferred_complete_timeline |
| `Action_None` | 179 | 200 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 128 | 178 | 51 | inferred_complete_timeline |
| `Action_None` | 179 | 249 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 221 | 96 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 299 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 142 | 17 | inferred_complete_timeline |
| `Action_None` | 144 | 176 | 33 | inferred_complete_timeline |
| `Action_None` | 179 | 215 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 188 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 190 | 65 | inferred_complete_timeline |
| `Action_None` | 193 | 298 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 185 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 151 | 26 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 167 | 42 | inferred_complete_timeline |
| `Action_None` | 171 | 299 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_None` | 126 | 129 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–144 | 145 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–189 | 182 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 123–149 | 26 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 129–299 | 169 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 133–155 | 8 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 153–255 | 103 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 156–297 | 137 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 183–185 | 3 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 184–220 | 7 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 189–299 | 110 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 194–299 | 106 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 194–206 | 8 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 200–299 | 98 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 218–288 | 71 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 228–299 | 72 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 251–253 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `20` (2 segments found)
- ❌ Missing segment for action `Action_BallSnap` on target `17` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (LG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 235: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '10' has invalid range: start=128, end=125. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=126, end=34. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '16' has invalid range: start=128, end=34. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '19' has invalid range: start=152, end=149. Clamping end to start.
- ⚠️ Action 'Action_None' range [126-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-213] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-298] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-190] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-215] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-221] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-125] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-189] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [123-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [144-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-255] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-182] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-297] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-218] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-288] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>