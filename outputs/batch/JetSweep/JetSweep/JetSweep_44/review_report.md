# Play-Annotation-Generator Annotation Review — JetSweep_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_44`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `6` | `5` |
| ✅ EXACT | `Action_BallSnap` | SAF2 | defense | `4` | `3` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `6` | `5` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 76 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `6` | `5` | 59 | START | 59 | 105 |
| ✅ EXACT | `Action_BallSnap` | SAF2 | `4` | `3` | 77 | START | 77 | 91 |
| ✅ EXACT | `Action_LeadBlock` | RB | `11` | `10` | 79 | START | 79 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 79 | START | 79 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 79 | START | 79 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 79 | START | 79 | 79 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 91 | END | 77 | 91 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 96 | START | 96 | 105 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `6` | `5` | 106 | START | 106 | 111 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `18` | `17` | 110 | START | 110 | 146 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_SnapReceive` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_None` | 92 | 95 | 4 | inferred_complete_timeline |
| `Action_Toss` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_None` | 106 | 259 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 125 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–254
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_JetMotion` | 59 | 105 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 115 | 254 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 200 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 108 | 32 | inferred_complete_timeline |
| `Action_None` | 112 | 153 | 42 | inferred_complete_timeline |
| `Action_None` | 156 | 208 | 53 | inferred_complete_timeline |
| `Action_None` | 216 | 269 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 114 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 139 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 146 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 208 | 62 | inferred_complete_timeline |
| `Action_None` | 212 | 269 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 146 | 35 | inferred_complete_timeline |
| `Action_None` | 147 | 155 | 9 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 225 | 53 | inferred_complete_timeline |
| `Action_None` | 227 | 269 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 100 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 146 | 28 | inferred_complete_timeline |
| `Action_None` | 147 | 255 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 105 | 29 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 100 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 218 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 102 | 26 | inferred_complete_timeline |
| `Action_None` | 105 | 165 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 203 | 127 | inferred_complete_timeline |
| `Action_None` | 208 | 269 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 240 | 164 | inferred_complete_timeline |
| `Action_None` | 245 | 248 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_None` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_BallSnap` | 77 | 91 | 15 | inferred_complete_timeline |
| `Action_None` | 92 | 269 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–269 | 270 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 18–269 | 240 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 39–132 | 83 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 99–110 | 8 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 121–269 | 142 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 139–269 | 131 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 145–269 | 98 | 3 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 149–186 | 31 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 176–183 | 7 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 179–269 | 91 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 182–245 | 64 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 218–238 | 21 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 223–265 | 42 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 90: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 90: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [77-200] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-153] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-208] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-254] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [79-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-165] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-255] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '18' starts at frame 79, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [79-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '18' starts at frame 147, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [147-208] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-30] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-120] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-132] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-155] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-186] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-245] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-242] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-265] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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