# Play-Annotation-Generator Annotation Review — JetSweep_199

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_199`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `7` | `6` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Toss` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `7` | `6` | 35 | START | 35 | 93 |
| ✅ EXACT | `Action_BallSnap` | RG | `21` | `20` | 70 | START | 70 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `1` | `0` | 72 | START | 72 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `13` | 72 | START | 72 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `17` | 72 | START | 72 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 72 | START | 72 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 72 | START | 72 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `22` | `21` | 72 | START | 72 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 81 | END | 70 | 81 |
| ✅ EXACT | `Action_Toss` | QB | `11` | `10` | 89 | START | 89 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `7` | `6` | 94 | START | 94 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_None` | 82 | 88 | 7 | inferred_complete_timeline |
| `Action_Toss` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 256 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 141 | 72 | inferred_complete_timeline |
| `Action_None` | 147 | 152 | 6 | inferred_complete_timeline |
| `Action_None` | 160 | 221 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 269 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_JetMotion` | 35 | 93 | 59 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 153 | 60 | inferred_complete_timeline |
| `Action_BallCarry` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_LeadBlock` | 72 | 152 | 81 | inferred_complete_timeline |
| `Action_LeadBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 181 | 11 | inferred_complete_timeline |
| `Action_None` | 183 | 232 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 83 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 97 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 109 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 100 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 71 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 145 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 147 | 170 | 24 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 90 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 100 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 112 | 43 | inferred_complete_timeline |
| `Action_None` | 114 | 241 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 132 | 63 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 218 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 139 | 70 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 169 | 25 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 104 | 35 | inferred_complete_timeline |
| `Action_None` | 106 | 133 | 28 | inferred_complete_timeline |
| `Action_None` | 137 | 269 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 224 | 155 | inferred_complete_timeline |
| `Action_None` | 227 | 232 | 6 | inferred_complete_timeline |
| `Action_None` | 241 | 244 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 169 | 100 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 137 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 170 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 174 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_None` | 70 | 147 | 78 | inferred_complete_timeline |
| `Action_None` | 149 | 166 | 18 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 174 | 197 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–269 | 164 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 125–232 | 108 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 139–140 | 2 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 142–269 | 125 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 170–217 | 48 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 173–269 | 97 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 400: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '0' (TE) duration 99 frames exceeds threshold 90 frames [start=72, end=170].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 99 frames exceeds threshold 90 frames [start=72, end=170].
- ⚠️ Action 'Action_LeadBlock' range [72-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [160-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [165-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-224] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-244] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-172] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-169] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-256] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-269] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-218] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-83] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-112] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-241] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-145] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [147-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-97] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-115] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-217] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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