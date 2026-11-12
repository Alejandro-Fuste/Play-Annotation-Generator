# Play-Annotation-Generator Annotation Review — SplitZone_256

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_256`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `0` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `0` | `0` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `0` | `Group` | 12 | START | 13 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 12 | START | 13 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 12 | START | 13 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 12 | START | 13 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 12 | START | 13 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 12 | START | 13 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 12 | START | 13 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 12 | START | 20 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 12 | START | 13 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 12 | START | 13 | 134 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 132 | START | 132 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `13` | `13` | 133 | START | 133 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `12` | 135 | START | 141 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 135 | START | 135 | 196 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 135 | START | 146 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `19` | `19` | 135 | START | 135 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 135 | START | 135 | 213 |
| ✅ EXACT | `Action_SnapReceive` | QB | `0` | `0` | 143 | END | 132 | 143 |
| ✅ EXACT | `Action_Handoff` | QB | `0` | `0` | 150 | START | 150 | 159 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `7` | 160 | START | 160 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 132 | 143 | 12 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 160 | 176 | 17 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 159 | 147 | inferred_complete_timeline |
| `Action_BallCarry` | 160 | 298 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–218
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 157 | 26 | inferred_complete_timeline |
| `Action_None` | 168 | 185 | 18 | inferred_complete_timeline |
| `Action_None` | 187 | 218 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 13–285
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 132 | 120 | inferred_complete_timeline |
| `Action_SplitBlock` | 133 | 151 | 19 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 233 | 60 | inferred_complete_timeline |
| `Action_None` | 234 | 285 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–207
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 134 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 196 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 206 | 207 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 13–221
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 133 | 121 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 151 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 167 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 181 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 202 | 204 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 207 | 221 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 13–147
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 147 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–261
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 134 | 115 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 221 | 233 | 13 | inferred_complete_timeline |
| `Action_None` | 234 | 261 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–256
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 134 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 213 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 232 | 13 | inferred_complete_timeline |
| `Action_None` | 235 | 240 | 6 | inferred_complete_timeline |
| `Action_None` | 242 | 256 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 179 | 48 | inferred_complete_timeline |
| `Action_None` | 181 | 299 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–191
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 191 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 13–202
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 196 | 65 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 159 | 28 | inferred_complete_timeline |
| `Action_None` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–286
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 174 | 43 | inferred_complete_timeline |
| `Action_None` | 194 | 286 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–207
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 85 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 131 | 45 | inferred_complete_timeline |
| `Action_None` | 132 | 178 | 47 | inferred_complete_timeline |
| `Action_None` | 183 | 207 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 227 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 131 | 119 | inferred_complete_timeline |
| `Action_None` | 132 | 299 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 13–299 | 243 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 153–156 | 4 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 165–299 | 135 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 194–238 | 45 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 208–268 | 61 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 239–277 | 39 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 242–271 | 30 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 135 != Inferred start 146
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 44 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 99 frames exceeds threshold 90 frames [start=135, end=233].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [132–143], lower_priority='Action_ZoneBlock' annotated_start=135, effective_Action_ZoneBlock_start=144.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 99 frames exceeds threshold 90 frames [start=135, end=233].
- ⚠️ Action 'Action_None' range [160-176] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-105] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-287] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-178] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [160-298] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-232] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-256] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-174] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-286] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [141-151] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [202-204] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [207-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [133-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-285] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [206-207] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-157] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-196] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [132-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-238] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-268] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-277] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>